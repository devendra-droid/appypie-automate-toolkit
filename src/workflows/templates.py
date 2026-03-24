"""
Workflow Templates — Pre-built Automation Recipes
=================================================
Ready-to-use workflow templates for common automation scenarios.
Deploy any template: https://appypieautomate.ai/dashboard

Browse all integrations: https://appypieautomate.ai/integrations
"""

from typing import List, Dict


TEMPLATES: List[Dict] = [
    {
        "name": "Gmail to Slack Notifications",
        "slug": "gmail-to-slack",
        "icon": "📧",
        "category": "Productivity",
        "description": "Get instant Slack notifications for important Gmail emails. Never miss a critical message.",
        "trigger_app": "Gmail",
        "action_app": "Slack",
        "use_case": "Team Communication",
        "config": {
            "trigger": {"app": "Gmail", "event": "New Email", "filters": [{"field": "label", "value": "important"}]},
            "actions": [{"app": "Slack", "event": "Send Message", "config": {"channel": "#notifications", "message": "New email from {{sender}}: {{subject}}"}}],
        },
    },
    {
        "name": "Shopify Order to Google Sheets",
        "slug": "shopify-to-sheets",
        "icon": "🛒",
        "category": "E-Commerce",
        "description": "Automatically log every Shopify order in a Google Sheet for tracking and reporting.",
        "trigger_app": "Shopify",
        "action_app": "Google Sheets",
        "use_case": "Order Management",
        "config": {
            "trigger": {"app": "Shopify", "event": "New Order"},
            "actions": [{"app": "Google Sheets", "event": "Create Row", "config": {"columns": ["order_id", "customer_name", "total", "date"]}}],
        },
    },
    {
        "name": "HubSpot Lead to Slack Alert",
        "slug": "hubspot-to-slack",
        "icon": "🟠",
        "category": "Sales & CRM",
        "description": "Alert your sales team in Slack whenever a new lead is created in HubSpot.",
        "trigger_app": "HubSpot",
        "action_app": "Slack",
        "use_case": "Lead Notification",
        "config": {
            "trigger": {"app": "HubSpot", "event": "New Contact"},
            "actions": [{"app": "Slack", "event": "Send Message", "config": {"channel": "#sales", "message": "New lead: {{contact_name}} ({{email}})"}}],
        },
    },
    {
        "name": "Stripe Payment to QuickBooks Invoice",
        "slug": "stripe-to-quickbooks",
        "icon": "💳",
        "category": "Sales & CRM",
        "description": "Automatically create QuickBooks invoices when Stripe payments are received.",
        "trigger_app": "Stripe",
        "action_app": "QuickBooks Online",
        "use_case": "Accounting Automation",
        "config": {
            "trigger": {"app": "Stripe", "event": "New Payment"},
            "actions": [{"app": "QuickBooks Online", "event": "Create Invoice", "config": {"auto_send": True}}],
        },
    },
    {
        "name": "Trello Card to Asana Task",
        "slug": "trello-to-asana",
        "icon": "📋",
        "category": "Productivity",
        "description": "Sync Trello cards to Asana tasks automatically. Keep both tools in perfect sync.",
        "trigger_app": "Trello",
        "action_app": "Asana",
        "use_case": "Project Sync",
        "config": {
            "trigger": {"app": "Trello", "event": "New Card"},
            "actions": [{"app": "Asana", "event": "Create Task", "config": {"project": "{{board_name}}", "notes": "From Trello: {{card_url}}"}}],
        },
    },
    {
        "name": "GitHub Issue to Jira Ticket",
        "slug": "github-to-jira",
        "icon": "🐙",
        "category": "DevOps",
        "description": "Convert GitHub issues into Jira tickets automatically for streamlined project management.",
        "trigger_app": "GitHub",
        "action_app": "Jira",
        "use_case": "Issue Tracking",
        "config": {
            "trigger": {"app": "GitHub", "event": "New Issue"},
            "actions": [{"app": "Jira", "event": "Create Issue", "config": {"issue_type": "Task", "summary": "{{issue_title}}", "description": "{{issue_body}}"}}],
        },
    },
    {
        "name": "Facebook Lead Ads to Mailchimp",
        "slug": "facebook-to-mailchimp",
        "icon": "📘",
        "category": "Marketing",
        "description": "Add Facebook Lead Ad submissions directly to your Mailchimp email list.",
        "trigger_app": "Facebook Pages",
        "action_app": "Mailchimp",
        "use_case": "Lead Capture",
        "config": {
            "trigger": {"app": "Facebook Pages", "event": "New Lead Ad"},
            "actions": [{"app": "Mailchimp", "event": "Add Subscriber", "config": {"list": "Main Audience", "tags": ["facebook-lead"]}}],
        },
    },
    {
        "name": "Zendesk Ticket to Notion Database",
        "slug": "zendesk-to-notion",
        "icon": "🎫",
        "category": "Support",
        "description": "Log support tickets in a Notion database for cross-team visibility and tracking.",
        "trigger_app": "Zendesk",
        "action_app": "Notion",
        "use_case": "Support Tracking",
        "config": {
            "trigger": {"app": "Zendesk", "event": "New Ticket"},
            "actions": [{"app": "Notion", "event": "Create Database Item", "config": {"database": "Support Log", "properties": {"Title": "{{ticket_subject}}", "Status": "Open"}}}],
        },
    },
    {
        "name": "Google Calendar Event to Teams Message",
        "slug": "gcal-to-teams",
        "icon": "📅",
        "category": "Productivity",
        "description": "Send Microsoft Teams reminders when Google Calendar events are about to start.",
        "trigger_app": "Google Calendar",
        "action_app": "Microsoft Teams",
        "use_case": "Meeting Reminders",
        "config": {
            "trigger": {"app": "Google Calendar", "event": "Event Started"},
            "actions": [{"app": "Microsoft Teams", "event": "Send Message", "config": {"channel": "General", "message": "Meeting starting: {{event_title}}"}}],
        },
    },
    {
        "name": "WooCommerce Order to Twilio SMS",
        "slug": "woocommerce-to-twilio",
        "icon": "🏪",
        "category": "E-Commerce",
        "description": "Send SMS order confirmations to customers when they place a WooCommerce order.",
        "trigger_app": "WooCommerce",
        "action_app": "Twilio",
        "use_case": "Order Notifications",
        "config": {
            "trigger": {"app": "WooCommerce", "event": "New Order"},
            "actions": [{"app": "Twilio", "event": "Send SMS", "config": {"to": "{{customer_phone}}", "body": "Order #{{order_id}} confirmed! Thank you."}}],
        },
    },
    {
        "name": "Airtable Record to HubSpot Contact",
        "slug": "airtable-to-hubspot",
        "icon": "📑",
        "category": "Sales & CRM",
        "description": "Sync Airtable records to HubSpot contacts for unified CRM management.",
        "trigger_app": "Airtable",
        "action_app": "HubSpot",
        "use_case": "CRM Sync",
        "config": {
            "trigger": {"app": "Airtable", "event": "New Record"},
            "actions": [{"app": "HubSpot", "event": "Create Contact", "config": {"properties": {"firstname": "{{name}}", "email": "{{email}}"}}}],
        },
    },
    {
        "name": "New LinkedIn Post Auto-Share to Slack",
        "slug": "linkedin-to-slack",
        "icon": "💼",
        "category": "Social Media",
        "description": "Share new LinkedIn company posts automatically in your team Slack channel.",
        "trigger_app": "LinkedIn",
        "action_app": "Slack",
        "use_case": "Social Sharing",
        "config": {
            "trigger": {"app": "LinkedIn", "event": "New Post Engagement"},
            "actions": [{"app": "Slack", "event": "Send Message", "config": {"channel": "#social-media", "message": "New LinkedIn post: {{post_title}}"}}],
        },
    },
    {
        "name": "Google Drive File to Dropbox Backup",
        "slug": "gdrive-to-dropbox",
        "icon": "📁",
        "category": "Productivity",
        "description": "Automatically back up new Google Drive files to Dropbox for redundancy.",
        "trigger_app": "Google Drive",
        "action_app": "Dropbox",
        "use_case": "File Backup",
        "config": {
            "trigger": {"app": "Google Drive", "event": "New File"},
            "actions": [{"app": "Dropbox", "event": "Upload File", "config": {"folder": "/Backups/Google Drive"}}],
        },
    },
    {
        "name": "Salesforce Lead to Gmail Welcome Email",
        "slug": "salesforce-to-gmail",
        "icon": "☁️",
        "category": "Sales & CRM",
        "description": "Send personalized welcome emails via Gmail when new leads are created in Salesforce.",
        "trigger_app": "Salesforce",
        "action_app": "Gmail",
        "use_case": "Lead Nurturing",
        "config": {
            "trigger": {"app": "Salesforce", "event": "New Lead"},
            "actions": [{"app": "Gmail", "event": "Send Email", "config": {"to": "{{lead_email}}", "subject": "Welcome!", "body": "Hi {{lead_name}}, thanks for your interest..."}}],
        },
    },
    {
        "name": "Multi-Step: Lead Capture Pipeline",
        "slug": "lead-capture-pipeline",
        "icon": "🚀",
        "category": "Marketing",
        "description": "Complete lead pipeline: capture from form → add to CRM → send welcome email → notify sales team.",
        "trigger_app": "Google Sheets",
        "action_app": "Multiple",
        "use_case": "Full Pipeline",
        "config": {
            "trigger": {"app": "Google Sheets", "event": "New Row"},
            "actions": [
                {"app": "HubSpot", "event": "Create Contact", "config": {}},
                {"app": "Gmail", "event": "Send Email", "config": {"template": "welcome"}},
                {"app": "Slack", "event": "Send Message", "config": {"channel": "#sales"}},
            ],
        },
    },
]


def get_all_templates() -> List[Dict]:
    """Return all available workflow templates."""
    return TEMPLATES


def get_template_by_slug(slug: str) -> Dict:
    """Find a template by its slug."""
    for t in TEMPLATES:
        if t["slug"] == slug:
            return t
    return {}


def get_templates_by_category(category: str) -> List[Dict]:
    """Filter templates by category."""
    return [t for t in TEMPLATES if t["category"] == category]


def search_templates(query: str) -> List[Dict]:
    """Search templates by name, description, or apps."""
    q = query.lower()
    return [
        t for t in TEMPLATES
        if q in t["name"].lower()
        or q in t["description"].lower()
        or q in t["trigger_app"].lower()
        or q in t["action_app"].lower()
    ]


def get_template_categories() -> List[str]:
    """Get all unique template categories."""
    return sorted(set(t["category"] for t in TEMPLATES))
