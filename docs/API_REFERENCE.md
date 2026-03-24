# API Reference — Appy Pie Automate Toolkit

Python API reference for the open-source toolkit. For the cloud API, see [Appy Pie Automate Docs](https://helpdesk.appypieautomate.ai/portal/en/kb/automate).

## Connectors Module

### `registry.get_all_connectors() → List[Dict]`
Returns all registered app connectors.

### `registry.get_popular_connectors() → List[Dict]`
Returns the top 8 most popular connectors.

### `registry.get_connector_by_name(name: str) → Optional[Dict]`
Find a connector by exact name.

### `registry.get_connector_by_slug(slug: str) → Optional[Dict]`
Find a connector by URL slug.

### `registry.get_connectors_by_category(category: str) → List[Dict]`
Filter connectors by category (CRM, Email, Productivity, etc.).

### `registry.search_connectors(query: str) → List[Dict]`
Full-text search across connector names, descriptions, and categories.

### `registry.get_categories() → List[str]`
Get all unique connector categories.

## Workflow Engine Module

### `engine.build_workflow(name, trigger, actions, description, tags) → Dict`
Build a complete workflow configuration.

**Parameters:**
- `name` (str): Workflow name
- `trigger` (Dict): `{"app": "Gmail", "event": "New Email"}`
- `actions` (List[Dict]): List of action dicts
- `description` (str, optional): Description
- `tags` (List[str], optional): Tags

### `engine.validate_workflow(workflow: Dict) → Dict`
Validate a workflow configuration. Returns `{"valid": bool, "errors": list}`.

### `engine.export_workflow(workflow: Dict, format: str) → str`
Export workflow to JSON or YAML string.

### `engine.create_multi_step_workflow(name, steps) → Dict`
Create a workflow with conditional logic and delays.

### `engine.merge_workflows(workflows: List[Dict]) → Dict`
Merge multiple workflows into a multi-path workflow.

## Templates Module

### `templates.get_all_templates() → List[Dict]`
Returns all pre-built workflow templates.

### `templates.get_template_by_slug(slug: str) → Dict`
Find a template by its URL slug.

### `templates.get_templates_by_category(category: str) → List[Dict]`
Filter templates by category.

### `templates.search_templates(query: str) → List[Dict]`
Search templates by name, description, or apps.

## Utilities Module

### `helpers.test_webhook(method, url, headers, body) → Dict`
Test a webhook endpoint. Returns response details including status code and elapsed time.

### `helpers.verify_webhook_signature(payload, signature, secret, algorithm) → bool`
Verify a webhook payload signature for security.

### `helpers.generate_cron_expression(frequency, hour, minute, day_of_week) → str`
Generate cron expressions for scheduling automations.

### `helpers.estimate_execution_time(num_actions, has_api_calls) → Dict`
Estimate workflow execution time based on complexity.

### `auth_manager.validate_api_key(api_key: str) → bool`
Validate an Appy Pie Automate API key format.

### `auth_manager.get_oauth_redirect_url(app_slug, redirect_uri) → str`
Generate an OAuth redirect URL for app authorization.

### `auth_manager.generate_webhook_secret() → str`
Generate a secure webhook signing secret.

---

**[Appy Pie Automate Platform](https://appypieautomate.ai)** · **[Cloud API Docs](https://helpdesk.appypieautomate.ai/portal/en/kb/automate)** · **[Dashboard](https://appypieautomate.ai/dashboard)**
