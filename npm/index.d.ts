/** Appy Pie Automate SDK — TypeScript Definitions
 * https://appypieautomate.ai
 */

export interface ConnectorInfo {
  name: string;
  url: string;
}

export interface ConnectorMap {
  [key: string]: ConnectorInfo;
  gmail: ConnectorInfo;
  slack: ConnectorInfo;
  shopify: ConnectorInfo;
  hubspot: ConnectorInfo;
  salesforce: ConnectorInfo;
  stripe: ConnectorInfo;
  github: ConnectorInfo;
  jira: ConnectorInfo;
}

export interface WorkflowTrigger {
  app: string;
  event: string;
}

export interface WorkflowAction {
  app: string;
  action: string;
  [key: string]: any;
}

export interface WorkflowDefinition {
  name: string;
  trigger: WorkflowTrigger;
  actions: WorkflowAction[];
  platform: string;
  dashboard: string;
  created?: string;
}

export interface PlatformInfo {
  platform: string;
  sdkVersion: string;
  website: string;
  appDirectory: string;
  signUp: string;
  docs: string;
  github: string;
  totalApps: number;
  connectors: number;
}

export interface WebhookResponse {
  status: number;
  body: any;
}

export interface AppyPieAutomateOptions {
  apiKey?: string;
  baseUrl?: string;
}

export declare class AppyPieAutomate {
  constructor(options?: AppyPieAutomateOptions);
  listConnectors(): ConnectorMap;
  getIntegrationUrl(appName: string): string | null;
  triggerWebhook(webhookUrl: string, payload?: object): Promise<WebhookResponse>;
  buildWorkflow(config: { name: string; trigger: WorkflowTrigger; actions?: WorkflowAction[] }): WorkflowDefinition;
  info(): PlatformInfo;
}

export declare const CONNECTORS: ConnectorMap;
export default AppyPieAutomate;
