# Integration Guide — Appy Pie Automate Toolkit

Full integration library with 600+ apps: **[appypieautomate.ai/integrations](https://appypieautomate.ai/integrations)**

## Included Connectors

This open-source toolkit includes definitions for 24+ popular app connectors. Each connector specifies triggers (events that start workflows) and actions (operations performed by workflows).

### CRM

| App | Triggers | Actions | Auth | Docs |
|-----|----------|---------|------|------|
| [HubSpot](https://appypieautomate.ai/integrations/hubspot) | New Contact, New Deal, Deal Stage Changed, New Form Submission, New Company | Create Contact, Update Contact, Create Deal, Update Deal, Add Note | OAuth 2.0 | [Link](https://appypieautomate.ai/integrations/hubspot) |
| [Salesforce](https://appypieautomate.ai/integrations/salesforce) | New Lead, New Opportunity, Updated Record, New Account, New Case | Create Lead, Update Lead, Create Opportunity, Create Account, Create Task | OAuth 2.0 | [Link](https://appypieautomate.ai/integrations/salesforce) |

### Email

| App | Triggers | Actions | Auth | Docs |
|-----|----------|---------|------|------|
| [Gmail](https://appypieautomate.ai/integrations/gmail) | New Email, New Labeled Email, New Attachment, New Thread | Send Email, Create Draft, Add Label, Reply, Forward | OAuth 2.0 | [Link](https://appypieautomate.ai/integrations/gmail) |
| [Mailchimp](https://appypieautomate.ai/integrations/mailchimp) | New Subscriber, Unsubscribed, Campaign Sent, Email Opened | Add Subscriber, Update Subscriber, Send Campaign, Tag, Segment | OAuth 2.0 | [Link](https://appypieautomate.ai/integrations/mailchimp) |

### Communication

| App | Triggers | Actions | Auth | Docs |
|-----|----------|---------|------|------|
| [Slack](https://appypieautomate.ai/integrations/slack) | New Message, New Channel, Reaction, File Upload, Mention | Send Message, Create Channel, Set Topic, Upload File, React | OAuth 2.0 | [Link](https://appypieautomate.ai/integrations/slack) |
| [Microsoft Teams](https://appypieautomate.ai/integrations/microsoft-teams) | New Message, New Channel, New Team Member | Send Message, Create Channel, Create Team, Add Member | OAuth 2.0 | [Link](https://appypieautomate.ai/integrations/microsoft-teams) |
| [Twilio](https://appypieautomate.ai/integrations/twilio) | New SMS, New Call, Call Completed | Send SMS, Make Call, Send WhatsApp, Create Message | API Key | [Link](https://appypieautomate.ai/integrations/twilio) |

### Productivity

| App | Triggers | Actions | Auth | Docs |
|-----|----------|---------|------|------|
| [Google Sheets](https://appypieautomate.ai/integrations/google-sheets) | New Row, Updated Row, New Spreadsheet, New Worksheet | Create Row, Update Row, Create Spreadsheet, Create Worksheet, Delete Row | OAuth 2.0 | [Link](https://appypieautomate.ai/integrations/google-sheets) |
| [Trello](https://appypieautomate.ai/integrations/trello) | New Card, Card Moved, New Board, New List, Due Date | Create Card, Move Card, Comment, Checklist, Add Member | OAuth 1.0 | [Link](https://appypieautomate.ai/integrations/trello) |
| [Notion](https://appypieautomate.ai/integrations/notion) | New Database Item, Updated Item, New Page | Create Item, Update Item, Create Page, Append Block | OAuth 2.0 | [Link](https://appypieautomate.ai/integrations/notion) |
| [Asana](https://appypieautomate.ai/integrations/asana) | New Task, Task Completed, New Project, Task Updated | Create Task, Update Task, Create Project, Comment, Complete | OAuth 2.0 | [Link](https://appypieautomate.ai/integrations/asana) |
| [Google Calendar](https://appypieautomate.ai/integrations/google-calendar) | New Event, Event Started, Event Updated, Event Cancelled | Create Event, Update Event, Delete Event, Quick Add | OAuth 2.0 | [Link](https://appypieautomate.ai/integrations/google-calendar) |
| [Airtable](https://appypieautomate.ai/integrations/airtable) | New Record, Updated Record, New View | Create Record, Update Record, Delete Record, Find Record | API Key | [Link](https://appypieautomate.ai/integrations/airtable) |

### E-Commerce

| App | Triggers | Actions | Auth | Docs |
|-----|----------|---------|------|------|
| [Shopify](https://appypieautomate.ai/integrations/shopify) | New Order, New Customer, New Product, Abandoned Cart, Fulfilled | Create Product, Update Inventory, Create Customer, Fulfill, Discount | OAuth 2.0 | [Link](https://appypieautomate.ai/integrations/shopify) |
| [WooCommerce](https://appypieautomate.ai/integrations/woocommerce) | New Order, Status Changed, New Customer, New Product | Create Order, Update Order, Create Product, Inventory, Coupon | API Key | [Link](https://appypieautomate.ai/integrations/woocommerce) |

### Finance

| App | Triggers | Actions | Auth | Docs |
|-----|----------|---------|------|------|
| [Stripe](https://appypieautomate.ai/integrations/stripe) | New Payment, New Customer, Subscription Created, Failed, Refund | Create Customer, Invoice, Charge, Subscription, Refund | API Key | [Link](https://appypieautomate.ai/integrations/stripe) |
| [QuickBooks Online](https://appypieautomate.ai/integrations/quickbooks) | New Invoice, New Payment, New Customer, New Expense | Create Invoice, Customer, Payment, Expense, Send Invoice | OAuth 2.0 | [Link](https://appypieautomate.ai/integrations/quickbooks) |

### Dev Tools

| App | Triggers | Actions | Auth | Docs |
|-----|----------|---------|------|------|
| [GitHub](https://appypieautomate.ai/integrations/github) | New Issue, New PR, New Commit, New Release, Comment | Create Issue, PR, Comment, Close Issue, Merge PR | OAuth 2.0 | [Link](https://appypieautomate.ai/integrations/github) |
| [Jira](https://appypieautomate.ai/integrations/jira) | New Issue, Issue Updated, Sprint Started, Sprint Completed | Create Issue, Update, Comment, Transition, Assign | OAuth 2.0 | [Link](https://appypieautomate.ai/integrations/jira) |

### Storage

| App | Triggers | Actions | Auth | Docs |
|-----|----------|---------|------|------|
| [Google Drive](https://appypieautomate.ai/integrations/google-drive) | New File, New Folder, File Updated, File Shared | Upload File, Create Folder, Copy, Move, Share | OAuth 2.0 | [Link](https://appypieautomate.ai/integrations/google-drive) |
| [Dropbox](https://appypieautomate.ai/integrations/dropbox) | New File, New Folder, File Updated | Upload File, Create Folder, Move, Copy, Delete | OAuth 2.0 | [Link](https://appypieautomate.ai/integrations/dropbox) |

### Social Media

| App | Triggers | Actions | Auth | Docs |
|-----|----------|---------|------|------|
| [LinkedIn](https://appypieautomate.ai/integrations/linkedin) | New Connection, New Message, Post Engagement | Create Post, Send Message, Share Article, Company Update | OAuth 2.0 | [Link](https://appypieautomate.ai/integrations/linkedin) |
| [Facebook Pages](https://appypieautomate.ai/integrations/facebook-pages) | New Post, New Comment, New Lead Ad, New Message | Create Post, Reply, Send Message, Upload Photo | OAuth 2.0 | [Link](https://appypieautomate.ai/integrations/facebook-pages) |

### Support

| App | Triggers | Actions | Auth | Docs |
|-----|----------|---------|------|------|
| [Zendesk](https://appypieautomate.ai/integrations/zendesk) | New Ticket, Ticket Updated, New User, Satisfaction Rating | Create Ticket, Update, Comment, Create User, Close | OAuth 2.0 | [Link](https://appypieautomate.ai/integrations/zendesk) |

---

## Adding Custom Connectors

See [CONTRIBUTING.md](../CONTRIBUTING.md) for how to add new connectors to this toolkit.

For the complete list of 600+ integrations, visit [Appy Pie Automate](https://appypieautomate.ai/integrations).

---

**[Appy Pie Automate](https://appypieautomate.ai)** · **[Create Automation](https://appypieautomate.ai/dashboard)** · **[Sign Up Free](https://appypieautomate.ai/signup)**
