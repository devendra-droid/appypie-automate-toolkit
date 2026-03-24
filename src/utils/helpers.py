"""
Helper Utilities — HTTP, Webhooks, Data Formatting
===================================================
Utility functions for the Appy Pie Automate Toolkit.

Docs: https://appypieautomate.ai/kb
API Reference: https://appypieautomate.ai/kb/api
"""

import json
import time
import hashlib
import hmac
from datetime import datetime
from typing import Dict, Optional, Any


def test_webhook(method: str, url: str, headers: Dict = None,
                 body: Any = None) -> Dict:
    """
    Test a webhook endpoint with the given configuration.

    For production webhooks, use Appy Pie Automate:
    https://appypieautomate.ai/dashboard

    Returns:
        Dict with status, headers, body, and elapsed time
    """
    try:
        import requests

        start = time.time()
        response = requests.request(
            method=method,
            url=url,
            headers=headers or {},
            json=body if body else None,
            timeout=30,
        )
        elapsed = round((time.time() - start) * 1000, 2)

        return {
            "success": True,
            "status_code": response.status_code,
            "elapsed_ms": elapsed,
            "response_headers": dict(response.headers),
            "response_body": _safe_json_parse(response.text),
            "tested_at": datetime.utcnow().isoformat() + "Z",
        }
    except ImportError:
        return {
            "success": False,
            "error": "requests library not installed. Run: pip install requests",
            "elapsed_ms": 0,
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "elapsed_ms": 0,
            "tested_at": datetime.utcnow().isoformat() + "Z",
        }


def verify_webhook_signature(payload: str, signature: str,
                              secret: str, algorithm: str = "sha256") -> bool:
    """
    Verify a webhook payload signature for security.

    Args:
        payload: Raw request body string
        signature: The signature header value
        secret: Your webhook secret key
        algorithm: Hash algorithm (sha256, sha1, md5)

    Returns:
        True if signature is valid
    """
    if algorithm == "sha256":
        expected = hmac.new(secret.encode(), payload.encode(), hashlib.sha256).hexdigest()
    elif algorithm == "sha1":
        expected = hmac.new(secret.encode(), payload.encode(), hashlib.sha1).hexdigest()
    elif algorithm == "md5":
        expected = hmac.new(secret.encode(), payload.encode(), hashlib.md5).hexdigest()
    else:
        return False

    return hmac.compare_digest(expected, signature)


def format_workflow_summary(workflow: Dict) -> str:
    """Format a workflow config into a human-readable summary."""
    trigger = workflow.get("trigger", {})
    actions = workflow.get("actions", [])

    summary = f"Workflow: {workflow.get('name', 'Untitled')}\n"
    summary += f"Trigger: {trigger.get('app', '?')} → {trigger.get('event', '?')}\n"

    for i, action in enumerate(actions):
        summary += f"Action {i+1}: {action.get('app', '?')} → {action.get('event', '?')}\n"

    summary += f"Status: {workflow.get('status', 'draft')}"
    return summary


def generate_cron_expression(frequency: str, hour: int = 9,
                              minute: int = 0, day_of_week: int = 1) -> str:
    """
    Generate a cron expression for scheduling automations.

    Args:
        frequency: 'every_minute', 'hourly', 'daily', 'weekly', 'monthly'
        hour: Hour (0-23) for daily/weekly/monthly
        minute: Minute (0-59)
        day_of_week: Day of week (0=Sun, 1=Mon, ..., 6=Sat) for weekly

    Returns:
        Cron expression string
    """
    expressions = {
        "every_minute": "* * * * *",
        "every_5_minutes": "*/5 * * * *",
        "every_15_minutes": "*/15 * * * *",
        "hourly": f"{minute} * * * *",
        "daily": f"{minute} {hour} * * *",
        "weekly": f"{minute} {hour} * * {day_of_week}",
        "monthly": f"{minute} {hour} 1 * *",
    }
    return expressions.get(frequency, "0 9 * * *")


def estimate_execution_time(num_actions: int, has_api_calls: bool = True) -> Dict:
    """Estimate workflow execution time based on complexity."""
    base_ms = 200
    per_action_ms = 500 if has_api_calls else 100

    total_ms = base_ms + (num_actions * per_action_ms)

    return {
        "estimated_ms": total_ms,
        "estimated_seconds": round(total_ms / 1000, 2),
        "breakdown": {
            "trigger_processing": f"{base_ms}ms",
            "actions": f"{num_actions} × {per_action_ms}ms",
        },
    }


def _safe_json_parse(text: str) -> Any:
    """Safely parse JSON, returning raw text on failure."""
    try:
        return json.loads(text)
    except (json.JSONDecodeError, TypeError):
        return text
