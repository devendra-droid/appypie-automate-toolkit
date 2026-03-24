# ⚡ Appy Pie Automate Toolkit

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-red.svg)](https://streamlit.io)
[![Integrations](https://img.shields.io/badge/Integrations-600%2B-green.svg)](https://appypieautomate.ai/integrations)

**Open-source automation framework for building, testing, and deploying workflow automations across 600+ apps.**

Built and maintained by [**Appy Pie Automate**](https://appypieautomate.ai) — the no-code workflow automation platform that lets you connect apps and automate tasks in minutes.

🔗 **[Create Your First Automation →](https://appypieautomate.ai/dashboard)**

---

## 🎯 What is This?

The Appy Pie Automate Toolkit is a **Streamlit-powered dashboard** and **Python library** that provides:

- **Visual Workflow Builder** — Design automation workflows connecting any combination of 600+ apps
- **24+ Pre-built Connectors** — Gmail, Slack, Shopify, HubSpot, Salesforce, Stripe, GitHub, and more
- **15+ Ready Templates** — Production-ready automation recipes you can deploy in one click
- **Webhook Tester** — Test and debug webhook endpoints for your integrations
- **Analytics Dashboard** — Monitor workflow execution, success rates, and time saved
- **JSON Export** — Export workflows as portable JSON configs

For the full cloud-hosted experience with drag-and-drop builder, real-time execution, and 600+ integrations, visit [**Appy Pie Automate**](https://appypieautomate.ai).

---

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- pip package manager

### Installation

```bash
# Clone the repository
git clone https://github.com/nicehash/appypie-automate-toolkit.git
cd appypie-automate-toolkit

# Install dependencies
pip install -r requirements.txt

# Launch the dashboard
streamlit run app.py
```

The dashboard opens at `http://localhost:8501`.

### Using as a Python Library

```python
from src.connectors import registry
from src.workflows import engine, templates

# Browse available connectors
connectors = registry.get_all_connectors()
print(f"Available: {len(connectors)} app connectors")

# Build a workflow
workflow = engine.build_workflow(
    name="New Lead Alert",
    trigger={"app": "HubSpot", "event": "New Contact"},
    actions=[
        {"app": "Slack", "event": "Send Message"},
        {"app": "Gmail", "event": "Send Email"},
    ],
)

# Export to JSON
json_config = engine.export_workflow(workflow)
print(json_config)

# Get pre-built templates
all_templates = templates.get_all_templates()
sales_templates = templates.get_templates_by_category("Sales & CRM")
```

---

## 📦 Supported Integrations

This toolkit includes connectors for the most popular apps. The full [Appy Pie Automate platform](https://appypieautomate.ai/integrations) supports **600+ integrations**.

| Category | Apps |
|----------|------|
| **CRM** | [HubSpot](https://appypieautomate.ai/integrations/hubspot), [Salesforce](https://appypieautomate.ai/integrations/salesforce) |
| **Email** | [Gmail](https://appypieautomate.ai/integrations/gmail), [Mailchimp](https://appypieautomate.ai/integrations/mailchimp) |
| **Communication** | [Slack](https://appypieautomate.ai/integrations/slack), [Microsoft Teams](https://appypieautomate.ai/integrations/microsoft-teams), [Twilio](https://appypieautomate.ai/integrations/twilio) |
| **Productivity** | [Google Sheets](https://appypieautomate.ai/integrations/google-sheets), [Trello](https://appypieautomate.ai/integrations/trello), [Notion](https://appypieautomate.ai/integrations/notion), [Asana](https://appypieautomate.ai/integrations/asana), [Google Calendar](https://appypieautomate.ai/integrations/google-calendar) |
| **E-Commerce** | [Shopify](https://appypieautomate.ai/integrations/shopify), [WooCommerce](https://appypieautomate.ai/integrations/woocommerce) |
| **Finance** | [Stripe](https://appypieautomate.ai/integrations/stripe), [QuickBooks](https://appypieautomate.ai/integrations/quickbooks) |
| **Dev Tools** | [GitHub](https://appypieautomate.ai/integrations/github), [Jira](https://appypieautomate.ai/integrations/jira) |
| **Storage** | [Google Drive](https://appypieautomate.ai/integrations/google-drive), [Dropbox](https://appypieautomate.ai/integrations/dropbox) |
| **Social Media** | [LinkedIn](https://appypieautomate.ai/integrations/linkedin), [Facebook Pages](https://appypieautomate.ai/integrations/facebook-pages) |
| **Support** | [Zendesk](https://appypieautomate.ai/integrations/zendesk) |

👉 **[Browse all 600+ integrations →](https://appypieautomate.ai/integrations)**

---

## 📋 Workflow Templates

Ready-to-deploy automation templates included in this toolkit:

| Template | Trigger → Action | Category |
|----------|-----------------|----------|
| Gmail to Slack Notifications | Gmail → Slack | Productivity |
| Shopify Order to Google Sheets | Shopify → Sheets | E-Commerce |
| HubSpot Lead to Slack Alert | HubSpot → Slack | Sales & CRM |
| Stripe Payment to QuickBooks | Stripe → QuickBooks | Finance |
| GitHub Issue to Jira Ticket | GitHub → Jira | DevOps |
| Facebook Lead Ads to Mailchimp | Facebook → Mailchimp | Marketing |
| Google Calendar to Teams | Calendar → Teams | Productivity |
| WooCommerce Order to SMS | WooCommerce → Twilio | E-Commerce |
| Lead Capture Pipeline | Sheets → CRM + Email + Slack | Marketing |
| ...and 6 more | [See full list](docs/TEMPLATES.md) | Various |

👉 **[Deploy templates on Appy Pie Automate →](https://appypieautomate.ai/dashboard)**

---

## 🏗️ Project Structure

```
appypie-automate-toolkit/
├── app.py                      # Streamlit dashboard (main entry)
├── requirements.txt            # Python dependencies
├── setup.py                    # Package setup
├── src/
│   ├── connectors/
│   │   └── registry.py         # 24+ app connector definitions
│   ├── workflows/
│   │   ├── engine.py           # Workflow builder & validator
│   │   └── templates.py        # 15+ pre-built templates
│   └── utils/
│       ├── helpers.py           # Webhook tester, cron generator
│       └── auth_manager.py     # API key & OAuth utilities
├── examples/
│   ├── basic_workflow.py        # Simple workflow example
│   ├── multi_step_pipeline.py   # Multi-step automation
│   └── webhook_handler.py       # Webhook processing example
├── docs/
│   ├── INTEGRATIONS.md          # Full integration guide
│   ├── TEMPLATES.md             # Template documentation
│   └── API_REFERENCE.md         # Toolkit API reference
├── tests/
│   └── ...                      # Test suite
├── .github/
│   ├── ISSUE_TEMPLATE/          # GitHub issue templates
│   └── workflows/               # CI/CD workflows
├── CONTRIBUTING.md              # Contribution guidelines
├── CODE_OF_CONDUCT.md           # Community code of conduct
└── LICENSE                      # MIT License
```

---

## 🧪 Running Tests

```bash
# Install test dependencies
pip install pytest pytest-cov

# Run tests
pytest tests/ -v --cov=src

# Run specific test module
pytest tests/test_engine.py -v
```

---

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**Ways to contribute:**

- Add new connector definitions
- Create workflow templates
- Improve documentation
- Report bugs or suggest features
- Write tests

---

## 📚 Resources & Links

| Resource | Link |
|----------|------|
| **Appy Pie Automate** (Main Platform) | [appypieautomate.ai](https://appypieautomate.ai) |
| **Create Automation** | [appypieautomate.ai/dashboard](https://appypieautomate.ai/dashboard) |
| **Sign Up Free** | [appypieautomate.ai/signup](https://appypieautomate.ai/signup) |
| **Login** | [appypieautomate.ai/login](https://appypieautomate.ai/login) |
| **All Integrations** | [appypieautomate.ai/integrations](https://appypieautomate.ai/integrations) |
| **Knowledge Base** | [appypieautomate.ai/kb](https://appypieautomate.ai/kb) |
| **Appy Pie** (Parent Company) | [appypie.com](https://www.appypie.com) |
| **Appy Pie App Builder** | [appypie.com/app-builder](https://www.appypie.com/app-builder) |
| **Appy Pie Website Builder** | [appypie.com/website-builder](https://www.appypie.com/website-builder) |
| **Appy Pie Chatbot** | [appypie.com/chatbot](https://www.appypie.com/chatbot) |
| **Appy Pie Design** | [appypie.com/design](https://www.appypie.com/design) |

---

## 🏷️ Related Projects

- [Appy Pie Automate](https://appypieautomate.ai) — No-code workflow automation platform
- [Appy Pie](https://www.appypie.com) — No-code app development platform
- [Appy Pie Connect](https://www.appypie.com/connect) — App integration platform

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## ⭐ Star This Repo

If you find this toolkit useful, please give it a ⭐ on GitHub! It helps us grow the community and build more open-source tools.

---

<p align="center">
  Built with ❤️ by <a href="https://appypieautomate.ai">Appy Pie Automate</a> ·
  <a href="https://appypieautomate.ai/signup">Sign Up Free</a> ·
  <a href="https://appypieautomate.ai/dashboard">Create Automation</a> ·
  <a href="https://appypieautomate.ai/integrations">600+ Integrations</a>
</p>
