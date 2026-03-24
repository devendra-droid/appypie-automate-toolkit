"""
Example: Build a Basic Automation Workflow
==========================================
This example shows how to create a simple two-step workflow
using the Appy Pie Automate Toolkit.

For a visual builder, use: https://appypieautomate.ai/dashboard
Sign up free: https://appypieautomate.ai/signup
"""

import sys
sys.path.insert(0, "..")

from src.connectors import registry
from src.workflows import engine


def main():
    # 1. Browse available connectors
    print("=== Available Connectors ===")
    connectors = registry.get_all_connectors()
    for c in connectors[:5]:
        print(f"  {c['icon']} {c['name']} ({c['category']})")
    print(f"  ... and {len(connectors) - 5} more")
    print(f"\n  Browse all 600+ at: https://appypieautomate.ai/integrations\n")

    # 2. Build a workflow: Gmail → Slack
    print("=== Building Workflow ===")
    workflow = engine.build_workflow(
        name="New Email → Slack Notification",
        trigger={"app": "Gmail", "event": "New Email"},
        actions=[{"app": "Slack", "event": "Send Message"}],
        description="Notify team in Slack when important emails arrive",
        tags=["email", "notifications"],
    )
    print(f"  Name: {workflow['name']}")
    print(f"  Trigger: {workflow['trigger']['app']} → {workflow['trigger']['event']}")
    print(f"  Actions: {len(workflow['actions'])} step(s)")

    # 3. Validate
    validation = engine.validate_workflow(workflow)
    print(f"\n=== Validation ===")
    print(f"  Valid: {validation['valid']}")

    # 4. Export
    json_output = engine.export_workflow(workflow)
    print(f"\n=== Exported JSON ({len(json_output)} chars) ===")
    print(json_output[:200] + "...")

    print(f"\n🚀 Deploy this workflow at: https://appypieautomate.ai/dashboard")
    print(f"📚 Docs: https://appypieautomate.ai/kb")


if __name__ == "__main__":
    main()
