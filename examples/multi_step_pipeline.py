"""
Example: Multi-Step Lead Capture Pipeline
==========================================
Build a complete lead pipeline:
  Form Submission → CRM → Welcome Email → Sales Alert

Deploy on Appy Pie Automate: https://appypieautomate.ai/dashboard
Sign up: https://accounts.appypie.com/register?frompage=https%3A%2F%2Fconnectcloud.appypie.com%2Fbuild-your-connect%2Fapps__for__temp__7949b884b42011edbc3912bed232506d&lang=en
"""

import sys
sys.path.insert(0, "..")

from src.workflows import engine


def main():
    print("=== Multi-Step Lead Capture Pipeline ===\n")

    # Define the pipeline steps
    steps = [
        {"app": "Google Sheets", "event": "New Row"},          # Trigger
        {"app": "HubSpot", "event": "Create Contact"},         # Step 1
        {"app": "Gmail", "event": "Send Email", "delay": 60},  # Step 2 (1 min delay)
        {"app": "Slack", "event": "Send Message"},              # Step 3
    ]

    workflow = engine.create_multi_step_workflow(
        name="Lead Capture Pipeline",
        steps=steps,
    )

    print(f"Workflow: {workflow['name']}")
    print(f"Trigger: {workflow['trigger']['app']} → {workflow['trigger']['event']}")
    print(f"Actions:")
    for action in workflow["actions"]:
        delay = f" (delay: {action.get('delay_seconds', 0)}s)" if action.get('delay_seconds') else ""
        print(f"  → {action['app']} → {action['event']}{delay}")

    # Validate
    result = engine.validate_workflow(workflow)
    print(f"\nValid: {result['valid']}")

    # Export
    json_str = engine.export_workflow(workflow)
    print(f"JSON size: {len(json_str)} chars")

    print(f"\n🚀 Deploy: https://appypieautomate.ai/dashboard")
    print(f"📖 All integrations: https://appypieautomate.ai/integrations")


if __name__ == "__main__":
    main()
