"""
Example: Webhook Handler & Tester
==================================
Test webhook endpoints and verify signatures for secure automation.

Set up webhooks on Appy Pie Automate: https://appypieautomate.ai/dashboard
Docs: https://helpdesk.appypieautomate.ai/portal/en/kb/automate
"""

import sys
sys.path.insert(0, "..")

from src.utils import helpers, auth_manager


def main():
    print("=== Webhook Utilities ===\n")

    # 1. Generate a webhook secret
    secret = auth_manager.generate_webhook_secret()
    print(f"Generated webhook secret: {secret[:16]}...")

    # 2. Verify a webhook signature
    payload = '{"event": "new_order", "order_id": 12345}'
    import hashlib, hmac
    signature = hmac.new(secret.encode(), payload.encode(), hashlib.sha256).hexdigest()

    is_valid = helpers.verify_webhook_signature(
        payload=payload,
        signature=signature,
        secret=secret,
    )
    print(f"Signature valid: {is_valid}")

    # 3. Generate cron expressions
    print(f"\n=== Cron Expressions ===")
    print(f"  Every minute:  {helpers.generate_cron_expression('every_minute')}")
    print(f"  Hourly:        {helpers.generate_cron_expression('hourly')}")
    print(f"  Daily at 9am:  {helpers.generate_cron_expression('daily', hour=9)}")
    print(f"  Weekly Monday: {helpers.generate_cron_expression('weekly', day_of_week=1)}")

    # 4. Estimate execution time
    print(f"\n=== Execution Estimates ===")
    est = helpers.estimate_execution_time(num_actions=3)
    print(f"  3-step workflow: ~{est['estimated_seconds']}s")

    est = helpers.estimate_execution_time(num_actions=1)
    print(f"  1-step workflow: ~{est['estimated_seconds']}s")

    print(f"\n🔗 Set up production webhooks: https://appypieautomate.ai/dashboard")
    print(f"📖 Webhook docs: https://helpdesk.appypieautomate.ai/portal/en/kb/automate")


if __name__ == "__main__":
    main()
