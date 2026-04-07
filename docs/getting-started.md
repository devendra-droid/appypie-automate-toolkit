# Getting Started with Appy Pie Automate

This guide walks you through creating your first automated workflow on [Appy Pie Automate](https://appypieautomate.ai) in under 5 minutes.

## Step 1: Create Your Account

1. Visit [appypieautomate.ai](https://appypieautomate.ai)
2. Click **Get Started Free**
3. Sign up with Google, GitHub, or email — no credit card required
4. You'll be taken to the Automate dashboard

## Step 2: Create Your First Connect

Automations on Appy Pie Automate are called **"Connects"**. Each Connect has:

- **Trigger** — the event that starts the automation (e.g., "New email in Gmail")
- **Action** — what happens in response (e.g., "Post message to Slack")

### Example: Gmail → Slack

```
Trigger: Gmail — New Email
Action:  Slack — Send Channel Message
```

1. Click **Create a Connect** on your dashboard
2. Search for **Gmail** and select **New Email** as trigger
3. Authorize your Gmail account via OAuth
4. Click **+ Add Action** → search for **Slack**
5. Select **Send Channel Message**
6. Map fields: Message = `{{Subject}} — {{Body Snippet}}`
7. Click **Save & Enable**

✅ Done! Every new Gmail will now post a Slack message automatically.

## Step 3: Install the SDK (Optional)

If you're a developer who wants to interact with Appy Pie Automate programmatically:

### Node.js / JavaScript

```bash
npm install appypie-automate
```

```js
const AppyPie = require('appypie-automate');
const client = new AppyPie({ apiKey: process.env.APPYPIE_API_KEY });

const integrations = await client.integrations.list();
console.log(integrations);
```

### Python

```bash
pip install appypie-automate-toolkit
```

```python
from appypie_automate import AppyPieAutomate

client = AppyPieAutomate(api_key="your-api-key")
integrations = client.integrations.list()
print(integrations)
```

## Popular Workflow Templates

| Workflow | Trigger | Action |
|----------|---------|--------|
| Lead capture | Typeform submission | Add to HubSpot |
| Order alert | Shopify new order | Slack message |
| Support ticket | Zendesk new ticket | Asana task |
| Content backup | Google Sheets row | Notion page |
| Payment alert | Stripe payment | Email notification |

## Next Steps

- Explore [all 1,000+ integrations](https://www.appypieautomate.ai/integrate/app-directory)
- Read the [full SDK reference](sdk.md)
- View the [Integrations guide](integrations.md)
- Sign up at [appypieautomate.ai](https://appypieautomate.ai)
