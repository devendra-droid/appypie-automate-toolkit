# Integration Guide — Appy Pie Automate Toolkit

Full integration library with 600+ apps: **[appypieautomate.ai](https://www.appypieautomate.ai/integrate/app-directory)**

## Included Connectors

This open-source toolkit includes definitions for 24+ popular app connectors. Each connector specifies triggers (events that start workflows) and actions (operations performed by workflows).

### CRM

| App | Triggers | Actions | Auth | Docs |
|-----|----------|---------|------|------|
| [HubSpot](https://www.appypieautomate.ai/integrate/apps/hubspot/integrations) | New Contact, New Deal, Deal Stage Changed, New Form Submission, New Company | Create Contact, Update Contact, Create Deal, Update Deal, Add Note | OAuth 2.0 | [Link](https://www.appypieautomate.ai/integrate/apps/hubspot/integrations) |
| [Salesforce](https://www.appypieautomate.ai/integrate/apps/salesforce/integrations) | New Lead, New Opportunity, Updated Record, New Account, New Case | Create Lead, Update Lead, Create Opportunity, Create Account, Create Task | OAuth 2.0 | [Link](https://www.appypieautomate.ai/integrate/apps/salesforce/integrations) |

### Email

| App | Triggers | Actions | Auth | Docs |
|-----|----------|---------|------|------|
| [Gmail](https://www.appypieautomate.ai/integrate/apps/gmail/integrations) | New Email, New Labeled Email, New Attachment, New Thread | Send Email, Create Draft, Add Label, Reply, Forward | OAuth 2.0 | [Link](https://www.appypieautomate.ai/integrate/apps/gmail/integrations) |
| [Mailchimp](https://www.appypieautomate.ai/integrate/apps/mailchimp/integrations) | New Subscriber, Unsubscribed, Campaign Sent, Email Opened | Add Subscriber, Update Subscriber, Send Campaign, Tag, Segment | OAuth 2.0 | [Link](https://www.appypieautomate.ai/integrate/apps/mailchimp/integrations) |

### Communication

| App | Triggers | Actions | Auth | Docs |
|-----|----------|---------|------|------|
| [Slack](https://www.appypieautomate.ai/integrate/apps/slack/integrations) | New Message, New Channel, Reaction, File Upload, Mention | Send Message, Create Channel, Set Topic, Upload File, React | OAuth 2.0 | [Link](https://www.appypieautomate.ai/integrate/apps/slack/integrations) |
| [Microsoft Teams](https://www.appypieautomate.ai/integrate/apps/microsoft-teams/integrations) | New Message, New Channel, New Team Member | Send Message, Create Channel, Create Team, Add Member | OAuth 2.0 | [Link](https://www.appypieautomate.ai/integrate/apps/microsoft-teams/integrations) |
| [Twilio](https://www.appypieautomate.ai/integrate/apps/twilio/integrations) | New SMS, New Call, Call Completed | Send SMS, Make Call, Send WhatsApp, Create Message | API Key | [Link](https://www.appypieautomate.ai/integrate/apps/twilio/integrations) |

### Productivity

| App | Triggers | Actions | Auth | Docs |
|-----|----------|---------|------|------|
| [Google Sheets](https://www.appypieautomate.ai/integrate/apps/google-sheets/integrations) | New Row, Updated Row, New Spreadsheet, New Worksheet | Create Row, Update Row, Create Spreadsheet, Create Worksheet, Delete Row | OAuth 2.0 | [Link](https://www.appypieautomate.ai/integrate/apps/google-sheets/integrations) |
| [Trello](https://www.appypieautomate.ai/integrate/apps/trello/integrations) | New Card, Card Moved, New Board, New List, Due Date | Create Card, Move Card, Comment, Checklist, Add Member | OAuth 1.0 | [Link](https://www.appypieautomate.ai/integrate/apps/trello/integrations) |
| [Notion](https://www.appypieautomate.ai/integrate/apps/notion/integrations) | New Database Item, Updated Item, New Page | Create Item, Update Item, Create Page, Append Block | OAuth 2.0 | [Link](https://www.appypieautomate.ai/integrate/apps/notion/integrations) |
| [Asana](https://www.appypieautomate.ai/integrate/apps/asana/integrations) | New Task, Task Completed, New Project, Task Updated | Create Task, Update Task, Create Project, Comment, Complete | OAuth 2.0 | [Link](https://www.appypieautomate.ai/integrate/apps/asana/integrations) |
| [Google Calendar](https://www.appypieautomate.ai/integrate/apps/google-calendar/integrations) | New Event, Event Started, Event Updated, Event Cancelled | Create Event, Update Event, Delete Event, Quick Add | OAuth 2.0 | [Link](https://www.appypieautomate.ai/integrate/apps/google-calendar/integrations) |
| [Airtable](https://www.appypieautomate.ai/integrate/apps/airtable/integrations) | New Record, Updated Record, New View | Create Record, Update Record, Delete Record, Find Record | API Key | [Link](https://www.appypieautomate.ai/integrate/apps/airtable/integrations) |

### E-Commerce

| App | Triggers | Actions | Auth | Docs |
|-----|----------|---------|------|------|
| [Shopify](https://www.appypieautomate.ai/integrate/apps/shopify/integrations) | New Order, New Customer, New Product, Abandoned Cart, Fulfilled | Create Product, Update Inventory, Create Customer, Fulfill, Discount | OAuth 2.0 | [Link](https://www.appypieautomate.ai/integrate/apps/shopify/integrations) |
| [WooCommerce](https://www.appypieautomate.ai/integrate/apps/woocommerce/integrations) | New Order, Status Changed, New Customer, New Product | Create Order, Update Order, Create Product, Inventory, Coupon | API Key | [Link](https://www.appypieautomate.ai/integrate/apps/woocommerce/integrations) |

### Finance

| App | Triggers | Actions | Auth | Docs |
|-----|----------|---------|------|------|
| [Stripe](https://www.appypieautomate.ai/integrate/apps/stripe/integrations) | New Payment, New Customer, Subscription Created, Failed, Refund | Create Customer, Invoice, Charge, Subscription, Refund | API Key | [Link](https://www.appypieautomate.ai/integrate/apps/stripe/integrations) |
| [QuickBooks Online](https://www.appypieautomate.ai/integrate/apps/quickbooks/integrations) | New Invoice, New Payment, New Customer, New Expense | Create Invoice, Customer, Payment, Expense, Send Invoice | OAuth 2.0 | [Link](https://www.appypieautomate.ai/integrate/apps/quickbooks/integrations) |

### Dev Tools

| App | Triggers | Actions | Auth | Docs |
|-----|----------|---------|------|------|
| [GitHub](https://www.appypieautomate.ai/integrate/apps/github/integrations) | New Issue, New PR, New Commit, New Release, Comment | Create Issue, PR, Comment, Close Issue, Merge PR | OAuth 2.0 | [Link](https://www.appypieautomate.ai/integrate/apps/github/integrations) |
| [Jira](https://www.appypieautomate.ai/integrate/apps/jirasoftwarecloud/integrations) | New Issue, Issue Updated, Sprint Started, Sprint Completed | Create Issue, Update, Comment, Transition, Assign | OAuth 2.0 | [Link](https://www.appypieautomate.ai/integrate/apps/jirasoftwarecloud/integrations) |

### Storage

| App | Triggers | Actions | Auth | Docs |
|-----|----------|---------|------|------|
| [Google Drive](https://www.appypieautomate.ai/integrate/apps/google-drive/integrations) | New File, New Folder, File Updated, File Shared | Upload File, Create Folder, Copy, Move, Share | OAuth 2.0 | [Link](https://www.appypieautomate.ai/integrate/apps/google-drive/integrations) |
| [Dropbox](https://www.appypieautomate.ai/integrate/apps/dropbox/integrations) | New File, New Folder, File Updated | Upload File, Create Folder, Move, Copy, Delete | OAuth 2.0 | [Link](https://www.appypieautomate.ai/integrate/apps/dropbox/integrations) |

### Social Media

| App | Triggers | Actions | Auth | Docs |
|-----|----------|---------|------|------|
| [LinkedIn](https://www.appypieautomate.ai/integrate/apps/linkedin/integrations) | New Connection, New Message, Post Engagement | Create Post, Send Message, Share Article, Company Update | OAuth 2.0 | [Link](https://www.appypieautomate.ai/integrate/apps/linkedin/integrations) |
| [Facebook Pages](https://www.appypieautomate.ai/integrate/apps/facebook-page/integrations) | New Post, New Comment, New Lead Ad, New Message | Create Post, Reply, Send Message, Upload Photo | OAuth 2.0 | [Link](https://www.appypieautomate.ai/integrate/apps/facebook-page/integrations) |
| [Instagram](https://www.appypieautomate.ai/integrate/apps/instagram/integrations) | New Post, New Story, New Follower, Tagged Post | Create Post, Reply Comment, Like, Share Story | OAuth 2.0 | [Link](https://www.appypieautomate.ai/integrate/apps/instagram/integrations) |
| [Twitter](https://www.appypieautomate.ai/integrate/apps/twitter/integrations) | New Tweet, New Mention, New Follower, Liked Tweet | Post Tweet, Like, Retweet, Send DM, Follow | OAuth 1.0a | [Link](https://www.appypieautomate.ai/integrate/apps/twitter/integrations) |

### Support

| App | Triggers | Actions | Auth | Docs |
|-----|----------|---------|------|------|
| [Zendesk](https://www.appypieautomate.ai/integrate/apps/zendesk/integrations) | New Ticket, Ticket Updated, New User, Satisfaction Rating | Create Ticket, Update, Comment, Create User, Close | OAuth 2.0 | [Link](https://www.appypieautomate.ai/integrate/apps/zendesk/integrations) |

---

## Adding Custom Connectors

See [CONTRIBUTING.md](../CONTRIBUTING.md) for how to add new connectors to this toolkit.

For the complete list of 600+ integrations, visit [Appy Pie Automate](https://www.appypieautomate.ai/integrate/app-directory).

---

**[Appy Pie Automate](https://appypieautomate.ai)** · **[Create Automation](https://appypieautomate.ai/dashboard)** · **[Sign Up Free](https://appypieautomate.ai/signup)**
