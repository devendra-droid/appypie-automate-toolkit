"""Tests for the helper utilities module."""

import pytest
from src.utils import helpers, auth_manager


def test_generate_cron_expression():
    assert helpers.generate_cron_expression("every_minute") == "* * * * *"
    assert helpers.generate_cron_expression("daily", hour=9) == "0 9 * * *"
    assert helpers.generate_cron_expression("weekly", day_of_week=1) == "0 9 * * 1"
    assert helpers.generate_cron_expression("monthly") == "0 9 1 * *"


def test_estimate_execution_time():
    est = helpers.estimate_execution_time(3)
    assert est["estimated_ms"] > 0
    assert est["estimated_seconds"] > 0

    est_fast = helpers.estimate_execution_time(1, has_api_calls=False)
    assert est_fast["estimated_ms"] < est["estimated_ms"]


def test_format_workflow_summary():
    workflow = {
        "name": "Test",
        "trigger": {"app": "Gmail", "event": "New Email"},
        "actions": [{"app": "Slack", "event": "Send Message"}],
        "status": "active",
    }
    summary = helpers.format_workflow_summary(workflow)
    assert "Test" in summary
    assert "Gmail" in summary
    assert "Slack" in summary


def test_verify_webhook_signature():
    import hashlib, hmac
    secret = "test_secret"
    payload = '{"test": true}'
    sig = hmac.new(secret.encode(), payload.encode(), hashlib.sha256).hexdigest()

    assert helpers.verify_webhook_signature(payload, sig, secret) is True
    assert helpers.verify_webhook_signature(payload, "wrong_sig", secret) is False


def test_validate_api_key():
    assert auth_manager.validate_api_key("") is False
    assert auth_manager.validate_api_key("short") is False
    assert auth_manager.validate_api_key("a" * 25) is True


def test_generate_webhook_secret():
    secret = auth_manager.generate_webhook_secret()
    assert len(secret) == 64  # SHA-256 hex digest
    assert isinstance(secret, str)


def test_get_oauth_redirect_url():
    url = auth_manager.get_oauth_redirect_url("gmail", "http://localhost:8501/callback")
    assert "gmail" in url
    assert "appypieautomate.ai" in url
