# appypie-automate

> JavaScript SDK for [Appy Pie Automate](https://appypieautomate.ai) — connect 600+ apps with no-code workflow automation

[![npm version](https://img.shields.io/npm/v/appypie-automate.svg)](https://www.npmjs.com/package/appypie-automate)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## What is Appy Pie Automate?

[Appy Pie Automate](https://appypieautomate.ai) is a no-code automation platform (like Zapier or Make) that connects 600+ apps — Gmail, Slack, Shopify, HubSpot, Salesforce, Stripe, GitHub, Jira, and more.

- **[Browse 600+ integrations](https://www.appypieautomate.ai/integrate/app-directory)**
- **[Sign up free](https://accounts.appypie.com/register)**
- **[Full documentation](https://helpdesk.appypieautomate.ai/portal/en/kb/automate)**

## Installation

```bash
npm install appypie-automate
```

## Quick Start

```javascript
const AppyPieAutomate = require('appypie-automate');

const client = new AppyPieAutomate({ apiKey: 'your-api-key' });

// List all supported connectors
const connectors = client.listConnectors();
console.log(connectors.gmail.url);
// https://www.appypieautomate.ai/integrate/gmail

// Get integration URL for any app
const url = client.getIntegrationUrl('shopify');
// https://www.appypieautomate.ai/integrate/shopify

// Build a workflow definition
const workflow = client.buildWorkflow({
  name: 'New Lead to Slack',
  trigger: { app: 'hubspot', event: 'new_contact' },
  actions: [{ app: 'slack', action: 'send_message', channel: '#sales' }]
});

// Trigger a webhook
await client.triggerWebhook('https://your-webhook-url.com/hook', {
  event: 'new_order',
  data: { orderId: '12345' }
});
```

## Supported Apps (24+ connectors)

| Category | Apps |
|----------|------|
| CRM | [HubSpot](https://www.appypieautomate.ai/integrate/hubspot), [Salesforce](https://www.appypieautomate.ai/integrate/salesforce), [Zendesk](https://www.appypieautomate.ai/integrate/zendesk) |
| Email | [Gmail](https://www.appypieautomate.ai/integrate/gmail), [Mailchimp](https://www.appypieautomate.ai/integrate/mailchimp) |
| Messaging | [Slack](https://www.appypieautomate.ai/integrate/slack), [Discord](https://www.appypieautomate.ai/integrate/discord) |
| E-commerce | [Shopify](https://www.appypieautomate.ai/integrate/shopify), [Stripe](https://www.appypieautomate.ai/integrate/stripe), [WooCommerce](https://www.appypieautomate.ai/integrate/woocommerce) |
| Productivity | [Notion](https://www.appypieautomate.ai/integrate/notion), [Airtable](https://www.appypieautomate.ai/integrate/airtable), [Trello](https://www.appypieautomate.ai/integrate/trello), [Asana](https://www.appypieautomate.ai/integrate/asana) |
| Dev Tools | [GitHub](https://www.appypieautomate.ai/integrate/github), [Jira](https://www.appypieautomate.ai/integrate/jira) |

[See all 600+ integrations →](https://www.appypieautomate.ai/integrate/app-directory)

## License

MIT © [Appy Pie Automate](https://appypieautomate.ai)
