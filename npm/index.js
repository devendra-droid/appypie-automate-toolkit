/**
 * Appy Pie Automate — JavaScript SDK
 * Connect 600+ apps with no-code workflow automation
 *
 * Website:     https://appypieautomate.ai
 * App Dir:     https://www.appypieautomate.ai/integrate/app-directory
 * Sign Up:     https://accounts.appypie.com/register
 * Docs:        https://helpdesk.appypieautomate.ai/portal/en/kb/automate
 * GitHub:      https://github.com/devendra-droid/appypie-automate-toolkit
 */

'use strict';

const https = require('https');

const CONNECTORS = {
  gmail:        { name: 'Gmail',         url: 'https://www.appypieautomate.ai/integrate/gmail' },
  slack:        { name: 'Slack',         url: 'https://www.appypieautomate.ai/integrate/slack' },
  shopify:      { name: 'Shopify',       url: 'https://www.appypieautomate.ai/integrate/shopify' },
  hubspot:      { name: 'HubSpot',       url: 'https://www.appypieautomate.ai/integrate/hubspot' },
  salesforce:   { name: 'Salesforce',    url: 'https://www.appypieautomate.ai/integrate/salesforce' },
  stripe:       { name: 'Stripe',        url: 'https://www.appypieautomate.ai/integrate/stripe' },
  github:       { name: 'GitHub',        url: 'https://www.appypieautomate.ai/integrate/github' },
  jira:         { name: 'Jira',          url: 'https://www.appypieautomate.ai/integrate/jira' },
  trello:       { name: 'Trello',        url: 'https://www.appypieautomate.ai/integrate/trello' },
  notion:       { name: 'Notion',        url: 'https://www.appypieautomate.ai/integrate/notion' },
  airtable:     { name: 'Airtable',      url: 'https://www.appypieautomate.ai/integrate/airtable' },
  googleSheets: { name: 'Google Sheets', url: 'https://www.appypieautomate.ai/integrate/google-sheets' },
  mailchimp:    { name: 'Mailchimp',     url: 'https://www.appypieautomate.ai/integrate/mailchimp' },
  discord:      { name: 'Discord',       url: 'https://www.appypieautomate.ai/integrate/discord' },
  zoom:         { name: 'Zoom',          url: 'https://www.appypieautomate.ai/integrate/zoom' },
  dropbox:      { name: 'Dropbox',       url: 'https://www.appypieautomate.ai/integrate/dropbox' },
  twilio:       { name: 'Twilio',        url: 'https://www.appypieautomate.ai/integrate/twilio' },
  asana:        { name: 'Asana',         url: 'https://www.appypieautomate.ai/integrate/asana' },
  googleDrive:  { name: 'Google Drive',  url: 'https://www.appypieautomate.ai/integrate/google-drive' },
  zendesk:      { name: 'Zendesk',       url: 'https://www.appypieautomate.ai/integrate/zendesk' },
  wordpress:    { name: 'WordPress',     url: 'https://www.appypieautomate.ai/integrate/wordpress' },
  googleCalendar: { name: 'Google Calendar', url: 'https://www.appypieautomate.ai/integrate/google-calendar' },
  typeform:     { name: 'Typeform',      url: 'https://www.appypieautomate.ai/integrate/typeform' },
  woocommerce:  { name: 'WooCommerce',   url: 'https://www.appypieautomate.ai/integrate/woocommerce' },
};

class AppyPieAutomate {
  constructor(options = {}) {
    this.apiKey  = options.apiKey || null;
    this.baseUrl = options.baseUrl || 'https://appypieautomate.ai';
    this.version = '2.1.0';
  }

  listConnectors() { return CONNECTORS; }

  getIntegrationUrl(appName) {
    const key = appName.toLowerCase().replace(/[^a-z]/g, '');
    return CONNECTORS[key] ? CONNECTORS[key].url : null;
  }

  triggerWebhook(webhookUrl, payload = {}) {
    return new Promise((resolve, reject) => {
      if (!webhookUrl) { reject(new Error('webhookUrl required')); return; }
      const body = JSON.stringify(payload);
      const url  = new URL(webhookUrl);
      const opts = {
        hostname: url.hostname, path: url.pathname + url.search, method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Content-Length': Buffer.byteLength(body) },
      };
      const req = https.request(opts, (res) => {
        let data = '';
        res.on('data', (c) => { data += c; });
        res.on('end', () => { try { resolve({ status: res.statusCode, body: JSON.parse(data) }); } catch (_) { resolve({ status: res.statusCode, body: data }); } });
      });
      req.on('error', reject); req.write(body); req.end();
    });
  }

  buildWorkflow({ name, trigger, actions = [] }) {
    return { name, trigger, actions, platform: 'Appy Pie Automate', dashboard: 'https://appypieautomate.ai/dashboard' };
  }

  info() {
    return { platform: 'Appy Pie Automate', sdkVersion: this.version, website: 'https://appypieautomate.ai',
      appDirectory: 'https://www.appypieautomate.ai/integrate/app-directory', totalApps: 600 };
  }
}

module.exports = AppyPieAutomate;
module.exports.AppyPieAutomate = AppyPieAutomate;
module.exports.CONNECTORS = CONNECTORS;
