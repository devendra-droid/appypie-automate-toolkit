"""
Connector Registry — App Integration Definitions
=================================================
Central registry of all supported app connectors with triggers, actions,
and authentication methods.

Full integration library: https://appypieautomate.ai/integrations
Create automations: https://appypieautomate.ai/dashboard
"""

from typing import List, Dict, Optional

# ─── Master Connector Registry ───────────────────────────────────────────────
CONNECTORS: List[Dict] = [
    {
        "name": "Gmail",
        "slug": "gmail",
        "icon": "📧",
        "category": "Email",
        "description": "Send, receive, and manage emails. Trigger automations on new emails, labels, and attachments.",
        "auth_type": "OAuth 2.0",
        "triggers": ["New Email", "New Labeled Email", "New Attachment", "New Thread"],
        "actions": ["Send Email", "Create Draft", "Add Label", "Reply to Email", "Forward Email"],
        "website": "https://mail.google.com",
        "docs_url": "https://appypieautomate.ai/integrations/gmail",
    },
    {
        "name": "Slack",
        "slug": "slack",
        "icon": "💬",
        "category": "Communication",
        "description": "Automate Slack messaging, channel management, and notifications across your workspace.",
        "auth_type": "OAuth 2.0",
        "triggers": ["New Message", "New Channel", "New Reaction", "New File Upload", "Mention"],
        "actions": ["Send Message", "Create Channel", "Set Topic", "Upload File", "Add Reaction"],
        "website": "https://slack.com",
        "docs_url": "https://appypieautomate.ai/integrations/slack",
    },
    {
        "name": "Google Sheets",
        "slug": "google-sheets",
        "icon": "📊",
        "category": "Productivity",
        "description": "Read, write, and update spreadsheet data. Perfect for data syncing and reporting automations.",
        "auth_type": "OAuth 2.0",
        "triggers": ["New Row", "Updated Row", "New Spreadsheet", "New Worksheet"],
        "actions": ["Create Row", "Update Row", "Create Spreadsheet", "Create Worksheet", "Delete Row"],
        "website": "https://sheets.google.com",
        "docs_url": "https://appypieautomate.ai/integrations/google-sheets",
    },
    {
        "name": "HubSpot",
        "slug": "hubspot",
        "icon": "🟠",
        "category": "CRM",
        "description": "Sync contacts, deals, and marketing data. Automate your entire sales pipeline.",
        "auth_type": "OAuth 2.0",
        "triggers": ["New Contact", "New Deal", "Deal Stage Changed", "New Form Submission", "New Company"],
        "actions": ["Create Contact", "Update Contact", "Create Deal", "Update Deal", "Add Note"],
        "website": "https://hubspot.com",
        "docs_url": "https://appypieautomate.ai/integrations/hubspot",
    },
    {
        "name": "Salesforce",
        "slug": "salesforce",
        "icon": "☁️",
        "category": "CRM",
        "description": "Connect Salesforce CRM with any app. Automate lead management, opportunity tracking, and more.",
        "auth_type": "OAuth 2.0",
        "triggers": ["New Lead", "New Opportunity", "Updated Record", "New Account", "New Case"],
        "actions": ["Create Lead", "Update Lead", "Create Opportunity", "Create Account", "Create Task"],
        "website": "https://salesforce.com",
        "docs_url": "https://appypieautomate.ai/integrations/salesforce",
    },
    {
        "name": "Shopify",
        "slug": "shopify",
        "icon": "🛒",
        "category": "E-Commerce",
        "description": "Automate order processing, inventory updates, and customer management for your Shopify store.",
        "auth_type": "OAuth 2.0",
        "triggers": ["New Order", "New Customer", "New Product", "Abandoned Cart", "Order Fulfilled"],
        "actions": ["Create Product", "Update Inventory", "Create Customer", "Fulfill Order", "Create Discount"],
        "website": "https://shopify.com",
        "docs_url": "https://appypieautomate.ai/integrations/shopify",
    },
    {
        "name": "Trello",
        "slug": "trello",
        "icon": "📋",
        "category": "Productivity",
        "description": "Automate card creation, board management, and task assignments in Trello.",
        "auth_type": "OAuth 1.0",
        "triggers": ["New Card", "Card Moved", "New Board", "New List", "Card Due Date"],
        "actions": ["Create Card", "Move Card", "Add Comment", "Create Checklist", "Add Member"],
        "website": "https://trello.com",
        "docs_url": "https://appypieautomate.ai/integrations/trello",
    },
    {
        "name": "Notion",
        "slug": "notion",
        "icon": "📝",
        "category": "Productivity",
        "description": "Sync databases, create pages, and automate your Notion workspace.",
        "auth_type": "OAuth 2.0",
        "triggers": ["New Database Item", "Updated Database Item", "New Page"],
        "actions": ["Create Database Item", "Update Database Item", "Create Page", "Append Block"],
        "website": "https://notion.so",
        "docs_url": "https://appypieautomate.ai/integrations/notion",
    },
    {
        "name": "Mailchimp",
        "slug": "mailchimp",
        "icon": "🐵",
        "category": "Marketing",
        "description": "Automate email campaigns, subscriber management, and audience segmentation.",
        "auth_type": "OAuth 2.0",
        "triggers": ["New Subscriber", "Subscriber Unsubscribed", "Campaign Sent", "Email Opened"],
        "actions": ["Add Subscriber", "Update Subscriber", "Send Campaign", "Tag Subscriber", "Create Segment"],
        "website": "https://mailchimp.com",
        "docs_url": "https://appypieautomate.ai/integrations/mailchimp",
    },
    {
        "name": "Stripe",
        "slug": "stripe",
        "icon": "💳",
        "category": "Finance",
        "description": "Automate payment processing, subscription management, and financial reporting.",
        "auth_type": "API Key",
        "triggers": ["New Payment", "New Customer", "Subscription Created", "Payment Failed", "Refund Issued"],
        "actions": ["Create Customer", "Create Invoice", "Create Charge", "Create Subscription", "Issue Refund"],
        "website": "https://stripe.com",
        "docs_url": "https://appypieautomate.ai/integrations/stripe",
    },
    {
        "name": "Airtable",
        "slug": "airtable",
        "icon": "📑",
        "category": "Productivity",
        "description": "Connect Airtable bases with any app. Sync records, trigger workflows on changes.",
        "auth_type": "API Key",
        "triggers": ["New Record", "Updated Record", "New View"],
        "actions": ["Create Record", "Update Record", "Delete Record", "Find Record"],
        "website": "https://airtable.com",
        "docs_url": "https://appypieautomate.ai/integrations/airtable",
    },
    {
        "name": "GitHub",
        "slug": "github",
        "icon": "🐙",
        "category": "Dev Tools",
        "description": "Automate repo management, issue tracking, and CI/CD workflows.",
        "auth_type": "OAuth 2.0",
        "triggers": ["New Issue", "New Pull Request", "New Commit", "New Release", "Issue Comment"],
        "actions": ["Create Issue", "Create PR", "Create Comment", "Close Issue", "Merge PR"],
        "website": "https://github.com",
        "docs_url": "https://appypieautomate.ai/integrations/github",
    },
    {
        "name": "Jira",
        "slug": "jira",
        "icon": "🔵",
        "category": "Dev Tools",
        "description": "Automate issue creation, sprint management, and project tracking in Jira.",
        "auth_type": "OAuth 2.0",
        "triggers": ["New Issue", "Issue Updated", "Sprint Started", "Sprint Completed"],
        "actions": ["Create Issue", "Update Issue", "Add Comment", "Transition Issue", "Assign Issue"],
        "website": "https://jira.atlassian.com",
        "docs_url": "https://appypieautomate.ai/integrations/jira",
    },
    {
        "name": "Zendesk",
        "slug": "zendesk",
        "icon": "🎫",
        "category": "Support",
        "description": "Automate ticket management, customer support workflows, and satisfaction tracking.",
        "auth_type": "OAuth 2.0",
        "triggers": ["New Ticket", "Ticket Updated", "New User", "Satisfaction Rating"],
        "actions": ["Create Ticket", "Update Ticket", "Add Comment", "Create User", "Close Ticket"],
        "website": "https://zendesk.com",
        "docs_url": "https://appypieautomate.ai/integrations/zendesk",
    },
    {
        "name": "Google Drive",
        "slug": "google-drive",
        "icon": "📁",
        "category": "Storage",
        "description": "Automate file management, sharing, and backup workflows in Google Drive.",
        "auth_type": "OAuth 2.0",
        "triggers": ["New File", "New Folder", "File Updated", "File Shared"],
        "actions": ["Upload File", "Create Folder", "Copy File", "Move File", "Share File"],
        "website": "https://drive.google.com",
        "docs_url": "https://appypieautomate.ai/integrations/google-drive",
    },
    {
        "name": "Dropbox",
        "slug": "dropbox",
        "icon": "📦",
        "category": "Storage",
        "description": "Sync files, automate backups, and manage cloud storage workflows.",
        "auth_type": "OAuth 2.0",
        "triggers": ["New File", "New Folder", "File Updated"],
        "actions": ["Upload File", "Create Folder", "Move File", "Copy File", "Delete File"],
        "website": "https://dropbox.com",
        "docs_url": "https://appypieautomate.ai/integrations/dropbox",
    },
    {
        "name": "Microsoft Teams",
        "slug": "microsoft-teams",
        "icon": "👥",
        "category": "Communication",
        "description": "Automate messaging, channel management, and notifications in Microsoft Teams.",
        "auth_type": "OAuth 2.0",
        "triggers": ["New Message", "New Channel", "New Team Member"],
        "actions": ["Send Message", "Create Channel", "Create Team", "Add Member"],
        "website": "https://teams.microsoft.com",
        "docs_url": "https://appypieautomate.ai/integrations/microsoft-teams",
    },
    {
        "name": "Asana",
        "slug": "asana",
        "icon": "✅",
        "category": "Productivity",
        "description": "Automate task creation, project updates, and team assignments in Asana.",
        "auth_type": "OAuth 2.0",
        "triggers": ["New Task", "Task Completed", "New Project", "Task Updated"],
        "actions": ["Create Task", "Update Task", "Create Project", "Add Comment", "Complete Task"],
        "website": "https://asana.com",
        "docs_url": "https://appypieautomate.ai/integrations/asana",
    },
    {
        "name": "Twilio",
        "slug": "twilio",
        "icon": "📱",
        "category": "Communication",
        "description": "Send SMS, make calls, and automate communication workflows with Twilio.",
        "auth_type": "API Key",
        "triggers": ["New SMS Received", "New Call", "Call Completed"],
        "actions": ["Send SMS", "Make Call", "Send WhatsApp", "Create Message"],
        "website": "https://twilio.com",
        "docs_url": "https://appypieautomate.ai/integrations/twilio",
    },
    {
        "name": "WooCommerce",
        "slug": "woocommerce",
        "icon": "🏪",
        "category": "E-Commerce",
        "description": "Automate WooCommerce orders, inventory, and customer management.",
        "auth_type": "API Key",
        "triggers": ["New Order", "Order Status Changed", "New Customer", "New Product"],
        "actions": ["Create Order", "Update Order", "Create Product", "Update Inventory", "Create Coupon"],
        "website": "https://woocommerce.com",
        "docs_url": "https://appypieautomate.ai/integrations/woocommerce",
    },
    {
        "name": "Google Calendar",
        "slug": "google-calendar",
        "icon": "📅",
        "category": "Productivity",
        "description": "Automate event creation, reminders, and calendar syncing across apps.",
        "auth_type": "OAuth 2.0",
        "triggers": ["New Event", "Event Started", "Event Updated", "Event Cancelled"],
        "actions": ["Create Event", "Update Event", "Delete Event", "Quick Add Event"],
        "website": "https://calendar.google.com",
        "docs_url": "https://appypieautomate.ai/integrations/google-calendar",
    },
    {
        "name": "LinkedIn",
        "slug": "linkedin",
        "icon": "💼",
        "category": "Social Media",
        "description": "Automate LinkedIn posting, lead generation, and networking workflows.",
        "auth_type": "OAuth 2.0",
        "triggers": ["New Connection", "New Message", "New Post Engagement"],
        "actions": ["Create Post", "Send Message", "Share Article", "Create Company Update"],
        "website": "https://linkedin.com",
        "docs_url": "https://appypieautomate.ai/integrations/linkedin",
    },
    {
        "name": "Facebook Pages",
        "slug": "facebook-pages",
        "icon": "📘",
        "category": "Social Media",
        "description": "Automate Facebook page posts, responses, and lead ad processing.",
        "auth_type": "OAuth 2.0",
        "triggers": ["New Post", "New Comment", "New Lead Ad", "New Message"],
        "actions": ["Create Post", "Reply to Comment", "Send Message", "Upload Photo"],
        "website": "https://facebook.com",
        "docs_url": "https://appypieautomate.ai/integrations/facebook-pages",
    },
    {
        "name": "QuickBooks Online",
        "slug": "quickbooks",
        "icon": "💰",
        "category": "Finance",
        "description": "Automate invoicing, expense tracking, and accounting workflows.",
        "auth_type": "OAuth 2.0",
        "triggers": ["New Invoice", "New Payment", "New Customer", "New Expense"],
        "actions": ["Create Invoice", "Create Customer", "Create Payment", "Create Expense", "Send Invoice"],
        "website": "https://quickbooks.intuit.com",
        "docs_url": "https://appypieautomate.ai/integrations/quickbooks",
    },
]


def get_all_connectors() -> List[Dict]:
    """Return all registered connectors."""
    return CONNECTORS


def get_popular_connectors() -> List[Dict]:
    """Return the top 8 most popular connectors."""
    popular_names = ["Gmail", "Slack", "Google Sheets", "HubSpot", "Shopify", "Notion", "Stripe", "GitHub"]
    return [c for c in CONNECTORS if c["name"] in popular_names]


def get_connector_by_name(name: str) -> Optional[Dict]:
    """Find a connector by its name."""
    for c in CONNECTORS:
        if c["name"] == name:
            return c
    return None


def get_connector_by_slug(slug: str) -> Optional[Dict]:
    """Find a connector by its slug."""
    for c in CONNECTORS:
        if c["slug"] == slug:
            return c
    return None


def get_connectors_by_category(category: str) -> List[Dict]:
    """Filter connectors by category."""
    return [c for c in CONNECTORS if c["category"] == category]


def search_connectors(query: str) -> List[Dict]:
    """Search connectors by name, description, or category."""
    query_lower = query.lower()
    return [
        c for c in CONNECTORS
        if query_lower in c["name"].lower()
        or query_lower in c["description"].lower()
        or query_lower in c["category"].lower()
    ]


def get_categories() -> List[str]:
    """Get all unique connector categories."""
    return sorted(set(c["category"] for c in CONNECTORS))
