"""Tests for the workflow engine module."""

import json
import pytest
from src.workflows import engine


def test_build_workflow():
    workflow = engine.build_workflow(
        name="Test Workflow",
        trigger={"app": "Gmail", "event": "New Email"},
        actions=[{"app": "Slack", "event": "Send Message"}],
    )
    assert workflow["name"] == "Test Workflow"
    assert workflow["trigger"]["app"] == "Gmail"
    assert len(workflow["actions"]) == 1
    assert workflow["actions"][0]["app"] == "Slack"
    assert workflow["status"] == "draft"
    assert "id" in workflow


def test_build_workflow_multi_action():
    workflow = engine.build_workflow(
        name="Multi-Step",
        trigger={"app": "Shopify", "event": "New Order"},
        actions=[
            {"app": "Google Sheets", "event": "Create Row"},
            {"app": "Slack", "event": "Send Message"},
            {"app": "Gmail", "event": "Send Email"},
        ],
    )
    assert len(workflow["actions"]) == 3
    assert workflow["actions"][0]["order"] == 1
    assert workflow["actions"][2]["order"] == 3


def test_validate_workflow_valid():
    workflow = engine.build_workflow(
        name="Valid",
        trigger={"app": "Gmail", "event": "New Email"},
        actions=[{"app": "Slack", "event": "Send Message"}],
    )
    result = engine.validate_workflow(workflow)
    assert result["valid"] is True
    assert len(result["errors"]) == 0


def test_validate_workflow_missing_trigger():
    workflow = {"name": "Bad", "trigger": {"app": "", "event": ""}, "actions": [{"app": "Slack", "event": "Send"}]}
    result = engine.validate_workflow(workflow)
    assert result["valid"] is False
    assert len(result["errors"]) > 0


def test_validate_workflow_no_actions():
    workflow = {"name": "Empty", "trigger": {"app": "Gmail", "event": "New"}, "actions": []}
    result = engine.validate_workflow(workflow)
    assert result["valid"] is False


def test_export_workflow_json():
    workflow = engine.build_workflow(
        name="Export Test",
        trigger={"app": "Gmail", "event": "New Email"},
        actions=[{"app": "Slack", "event": "Send Message"}],
    )
    json_str = engine.export_workflow(workflow, "json")
    parsed = json.loads(json_str)
    assert parsed["name"] == "Export Test"


def test_create_multi_step_workflow():
    steps = [
        {"app": "Sheets", "event": "New Row"},
        {"app": "HubSpot", "event": "Create Contact"},
        {"app": "Gmail", "event": "Send Email", "delay": 60},
    ]
    workflow = engine.create_multi_step_workflow("Pipeline", steps)
    assert workflow["name"] == "Pipeline"
    assert len(workflow["actions"]) == 2
    assert workflow["actions"][1].get("delay_seconds") == 60


def test_merge_workflows():
    w1 = engine.build_workflow("W1", {"app": "A", "event": "E"}, [{"app": "B", "event": "F"}])
    w2 = engine.build_workflow("W2", {"app": "C", "event": "G"}, [{"app": "D", "event": "H"}])
    merged = engine.merge_workflows([w1, w2])
    assert merged["type"] == "multi_path"
    assert len(merged["paths"]) == 2
