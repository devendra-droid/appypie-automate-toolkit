# Workflow Templates — Appy Pie Automate Toolkit

Pre-built automation templates ready to deploy. Use the [Appy Pie Automate Dashboard](https://appypieautomate.ai/dashboard) for one-click deployment.

## All Templates

### Productivity

| Template | Flow | Description |
|----------|------|-------------|
| Gmail to Slack Notifications | Gmail → Slack | Instant Slack alerts for important emails |
| Google Calendar to Teams | Calendar → Teams | Meeting reminders in Microsoft Teams |
| Google Drive to Dropbox Backup | Drive → Dropbox | Auto-backup new files across cloud storage |
| Trello Card to Asana Task | Trello → Asana | Two-way project management sync |

### Sales & CRM

| Template | Flow | Description |
|----------|------|-------------|
| HubSpot Lead to Slack Alert | HubSpot → Slack | Instant sales team notifications |
| Stripe Payment to QuickBooks | Stripe → QuickBooks | Automated invoice creation |
| Airtable Record to HubSpot | Airtable → HubSpot | CRM sync from spreadsheet data |
| Salesforce Lead to Gmail | Salesforce → Gmail | Automated welcome emails |

### E-Commerce

| Template | Flow | Description |
|----------|------|-------------|
| Shopify Order to Google Sheets | Shopify → Sheets | Order logging and reporting |
| WooCommerce Order to SMS | WooCommerce → Twilio | SMS order confirmations |

### Marketing

| Template | Flow | Description |
|----------|------|-------------|
| Facebook Lead Ads to Mailchimp | Facebook → Mailchimp | Automatic list building |
| Lead Capture Pipeline | Sheets → CRM + Email + Slack | Complete lead nurturing flow |

### DevOps

| Template | Flow | Description |
|----------|------|-------------|
| GitHub Issue to Jira Ticket | GitHub → Jira | Cross-platform issue tracking |

### Support

| Template | Flow | Description |
|----------|------|-------------|
| Zendesk Ticket to Notion | Zendesk → Notion | Support ticket visibility |

### Social Media

| Template | Flow | Description |
|----------|------|-------------|
| LinkedIn Post to Slack | LinkedIn → Slack | Social content team sharing |

## Using Templates

### In the Streamlit Dashboard

1. Navigate to "Templates Gallery"
2. Filter by category
3. View the workflow JSON
4. Click "Use Template" to deploy on [Appy Pie Automate](https://appypieautomate.ai/dashboard)

### Programmatically

```python
from src.workflows import templates

# Get all templates
all_tmpl = templates.get_all_templates()

# Filter by category
sales = templates.get_templates_by_category("Sales & CRM")

# Search
results = templates.search_templates("shopify")

# Get specific template
tmpl = templates.get_template_by_slug("gmail-to-slack")
print(tmpl["config"])
```

## Creating Custom Templates

See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines on submitting new templates.

---

**[Deploy Templates →](https://appypieautomate.ai/dashboard)** · **[Browse Integrations →](https://appypieautomate.ai/integrations)** · **[Sign Up Free](https://appypieautomate.ai/signup)**
