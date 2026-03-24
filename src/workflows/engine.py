"""
Workflow Engine — Build & Validate Automation Workflows
=======================================================
Core engine for constructing, validating, and exporting workflow
configurations compatible with Appy Pie Automate.

Deploy workflows: https://appypieautomate.ai/dashboard
Docs: https://appypieautomate.ai/kb
"""

import json
import uuid
from datetime import datetime
from typing import List, Dict, Optional


def build_workflow(name: str, trigger: Dict, actions: List[Dict],
                   description: str = "", tags: List[str] = None) -> Dict:
    """
    Build a workflow configuration from trigger and action definitions.

    Args:
        name: Workflow name
        trigger: Dict with 'app' and 'event' keys
        actions: List of dicts, each with 'app' and 'event' keys
        description: Optional workflow description
        tags: Optional list of tags

    Returns:
        Complete workflow configuration dict
    """
    workflow = {
        "id": str(uuid.uuid4()),
        "name": name,
        "description": description or f"Automation: {trigger.get('app', '')} → {' → '.join(a.get('app', '') for a in actions)}",
        "version": "2.1.0",
        "created_at": datetime.utcnow().isoformat() + "Z",
        "status": "draft",
        "tags": tags or [],
        "trigger": {
            "id": f"trigger_{uuid.uuid4().hex[:8]}",
            "app": trigger.get("app", ""),
            "event": trigger.get("event", ""),
            "config": {},
            "filters": [],
        },
        "actions": [],
        "error_handling": {
            "retry_count": 3,
            "retry_delay_seconds": 60,
            "on_failure": "notify",
            "notification_email": "",
        },
        "metadata": {
            "toolkit_version": "2.1.0",
            "generated_by": "Appy Pie Automate Toolkit",
            "deploy_url": "https://appypieautomate.ai/dashboard",
        },
    }

    for i, action in enumerate(actions):
        workflow["actions"].append({
            "id": f"action_{uuid.uuid4().hex[:8]}",
            "order": i + 1,
            "app": action.get("app", ""),
            "event": action.get("event", ""),
            "config": {},
            "field_mappings": [],
        })

    return workflow


def validate_workflow(workflow: Dict) -> Dict:
    """
    Validate a workflow configuration for completeness and correctness.

    Returns:
        Dict with 'valid' (bool) and 'errors' (list) keys
    """
    errors = []

    if not workflow.get("name"):
        errors.append("Workflow name is required")
    if not workflow.get("trigger", {}).get("app"):
        errors.append("Trigger app is required")
    if not workflow.get("trigger", {}).get("event"):
        errors.append("Trigger event is required")
    if not workflow.get("actions"):
        errors.append("At least one action is required")

    for i, action in enumerate(workflow.get("actions", [])):
        if not action.get("app"):
            errors.append(f"Action {i+1}: App is required")
        if not action.get("event"):
            errors.append(f"Action {i+1}: Event is required")

    return {"valid": len(errors) == 0, "errors": errors}


def export_workflow(workflow: Dict, format: str = "json") -> str:
    """Export workflow to JSON or YAML string."""
    if format == "json":
        return json.dumps(workflow, indent=2)
    elif format == "yaml":
        try:
            import yaml
            return yaml.dump(workflow, default_flow_style=False)
        except ImportError:
            return json.dumps(workflow, indent=2)
    return json.dumps(workflow, indent=2)


def create_multi_step_workflow(name: str, steps: List[Dict]) -> Dict:
    """
    Create a multi-step workflow with conditional logic.

    Each step dict should have: app, event, condition (optional), delay (optional)
    """
    if not steps:
        return build_workflow(name, {}, [])

    trigger = steps[0]
    actions = steps[1:]

    workflow = build_workflow(name, trigger, actions)

    # Add conditional logic and delays
    for i, action in enumerate(workflow["actions"]):
        step_config = steps[i + 1] if i + 1 < len(steps) else {}
        if "condition" in step_config:
            action["condition"] = step_config["condition"]
        if "delay" in step_config:
            action["delay_seconds"] = step_config["delay"]

    return workflow


def merge_workflows(workflows: List[Dict]) -> Dict:
    """Merge multiple workflows into a single multi-path workflow."""
    if not workflows:
        return {}

    merged = {
        "id": str(uuid.uuid4()),
        "name": "Merged Workflow",
        "type": "multi_path",
        "paths": [],
        "created_at": datetime.utcnow().isoformat() + "Z",
        "metadata": {
            "toolkit_version": "2.1.0",
            "source_workflows": [w.get("id", "") for w in workflows],
            "deploy_url": "https://appypieautomate.ai/dashboard",
        },
    }

    for wf in workflows:
        merged["paths"].append({
            "name": wf.get("name", ""),
            "trigger": wf.get("trigger", {}),
            "actions": wf.get("actions", []),
        })

    return merged
