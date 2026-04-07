# SDK Reference — Appy Pie Automate

The Appy Pie Automate Toolkit provides official SDKs for JavaScript/Node.js and Python.

## JavaScript / Node.js SDK

### Installation

```bash
npm install appypie-automate
```

**npm:** [npmjs.com/package/appypie-automate](https://www.npmjs.com/package/appypie-automate)

### Initialization

```javascript
const AppyPieAutomate = require('appypie-automate');

const client = new AppyPieAutomate({
  apiKey: process.env.APPYPIE_API_KEY,
  baseUrl: 'https://api.appypieautomate.ai'
});
```

### Methods

#### List Integrations

```javascript
// Get all available integrations
const integrations = await client.integrations.list();
console.log(integrations.data); // Array of integration objects
```

#### Get Integration Details

```javascript
const gmail = await client.integrations.get('gmail');
console.log(gmail.triggers); // Available triggers
console.log(gmail.actions);  // Available actions
```

#### Trigger a Workflow

```javascript
const result = await client.workflows.trigger('your-workflow-id', {
  data: {
    email: 'user@example.com',
    name: 'John Doe',
    message: 'Hello!'
  }
});
console.log(result.status); // 'success'
```

#### List Workflows

```javascript
const workflows = await client.workflows.list();
workflows.forEach(w => console.log(w.name, w.status));
```

#### Create Webhook

```javascript
const webhook = await client.webhooks.create({
  url: 'https://your-app.com/webhook',
  events: ['workflow.triggered', 'workflow.completed']
});
console.log(webhook.id, webhook.secret);
```

---

## Python SDK

### Installation

```bash
pip install appypie-automate-toolkit
```

**PyPI:** [pypi.org/project/appypie-automate-toolkit](https://pypi.org/project/appypie-automate-toolkit/)

### Initialization

```python
from appypie_automate import AppyPieAutomate
import os

client = AppyPieAutomate(
    api_key=os.environ['APPYPIE_API_KEY']
)
```

### Methods

#### List Integrations

```python
integrations = client.integrations.list()
for integration in integrations:
    print(integration['name'], integration['category'])
```

#### Trigger a Workflow

```python
result = client.workflows.trigger(
    workflow_id='your-workflow-id',
    data={
        'email': 'user@example.com',
        'name': 'Jane Doe'
    }
)
print(result['status'])  # 'success'
```

#### List Active Workflows

```python
workflows = client.workflows.list(status='active')
for workflow in workflows:
    print(f"{workflow['name']}: {workflow['trigger']} → {workflow['action']}")
```

#### Handle Webhooks

```python
from appypie_automate import WebhookHandler

handler = WebhookHandler(secret='your-webhook-secret')

@handler.on('workflow.completed')
def on_complete(event):
    print(f"Workflow {event['workflow_id']} completed!")
    print(f"Result: {event['result']}")
```

---

## Environment Variables

| Variable | Description |
|----------|-------------|
| `APPYPIE_API_KEY` | Your Appy Pie Automate API key |
| `APPYPIE_BASE_URL` | API base URL (default: production) |
| `APPYPIE_WEBHOOK_SECRET` | Secret for webhook verification |

## Getting Your API Key

1. Log in at [appypieautomate.ai](https://appypieautomate.ai)
2. Go to **Settings → API Keys**
3. Click **Generate New Key**
4. Copy and store securely

## Links

- 🌐 [Appy Pie Automate](https://appypieautomate.ai)
- 📦 [npm Package](https://www.npmjs.com/package/appypie-automate)
- 🐍 [PyPI Package](https://pypi.org/project/appypie-automate-toolkit/)
- 📚 [Full Documentation](https://helpdesk.appypieautomate.ai/portal/en/kb/automate)
- 💻 [GitHub Source](https://github.com/devendra-droid/appypie-automate-toolkit)
