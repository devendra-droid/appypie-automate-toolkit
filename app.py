"""
🚀 Appy Pie Automate - Open Source Automation Toolkit
=====================================================
A Streamlit-powered dashboard for building, testing, and managing
workflow automations across 600+ apps.

Built by the team at Appy Pie Automate (https://appypieautomate.ai)
Docs: https://appypieautomate.ai/kb
Dashboard: https://appypieautomate.ai/dashboard

License: MIT
"""

import streamlit as st
import json
import time
from datetime import datetime
from src.connectors import registry
from src.workflows import engine, templates
from src.utils import helpers, auth_manager

# ─── Page Config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Appy Pie Automate Toolkit - Workflow Automation Dashboard",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://appypieautomate.ai/kb",
        "Report a bug": "https://github.com/nicehash/appypie-automate-toolkit/issues",
        "About": (
            "### Appy Pie Automate Toolkit\n"
            "Open-source automation framework by [Appy Pie Automate](https://appypieautomate.ai).\n\n"
            "Build workflows connecting 600+ apps — no code required.\n\n"
            "**[Create your first automation →](https://appypieautomate.ai/dashboard)**"
        ),
    },
)

# ─── Custom CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem; border-radius: 12px; color: white; margin-bottom: 2rem;
    }
    .metric-card {
        background: #f8f9fa; border-radius: 10px; padding: 1.2rem;
        border-left: 4px solid #667eea; margin-bottom: 1rem;
    }
    .connector-badge {
        display: inline-block; padding: 4px 12px; border-radius: 20px;
        background: #e8eaf6; color: #3f51b5; font-size: 0.85rem;
        margin: 2px; font-weight: 500;
    }
    .workflow-card {
        background: white; border: 1px solid #e0e0e0; border-radius: 10px;
        padding: 1.5rem; margin-bottom: 1rem; transition: box-shadow 0.2s;
    }
    .workflow-card:hover { box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
    .cta-banner {
        background: linear-gradient(90deg, #4CAF50, #45a049);
        color: white; padding: 1rem 2rem; border-radius: 8px;
        text-align: center; margin-top: 2rem;
    }
    .cta-banner a { color: white; text-decoration: underline; font-weight: bold; }
</style>
""", unsafe_allow_html=True)


# ─── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.image("https://appypieautomate.ai/favicon.ico", width=40)
    st.title("⚡ Automate Toolkit")
    st.markdown(
        "Open-source tools by [Appy Pie Automate](https://appypieautomate.ai) "
        "for building workflow automations."
    )
    st.divider()

    page = st.radio(
        "Navigate",
        [
            "🏠 Dashboard",
            "🔗 App Connectors",
            "🔄 Workflow Builder",
            "📋 Templates Gallery",
            "🧪 Webhook Tester",
            "📊 Automation Analytics",
            "⚙️ Settings",
        ],
        label_visibility="collapsed",
    )

    st.divider()
    st.markdown(
        "**Quick Links**\n"
        "- [Create Automation](https://appypieautomate.ai/dashboard)\n"
        "- [Integration Library](https://appypieautomate.ai/integrations)\n"
        "- [API Docs](https://appypieautomate.ai/kb)\n"
        "- [Signup Free](https://appypieautomate.ai/signup)\n"
        "- [Login](https://appypieautomate.ai/login)\n"
    )
    st.caption("v2.1.0 • MIT License • [GitHub](https://github.com/nicehash/appypie-automate-toolkit)")


# ─── Dashboard Page ──────────────────────────────────────────────────────────
if page == "🏠 Dashboard":
    st.markdown(
        '<div class="main-header">'
        "<h1>⚡ Appy Pie Automate Toolkit</h1>"
        "<p>Open-source framework for building, testing, and deploying workflow automations across 600+ apps. "
        'Powered by <a href="https://appypieautomate.ai" style="color:#ffd740">Appy Pie Automate</a>.</p>'
        "</div>",
        unsafe_allow_html=True,
    )

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Supported Apps", "600+", "+45 this month")
    with col2:
        st.metric("Workflow Templates", "150+", "+12 new")
    with col3:
        st.metric("Active Connectors", len(registry.get_all_connectors()), "Ready")
    with col4:
        st.metric("Avg. Setup Time", "< 3 min", "No code needed")

    st.markdown("---")

    # Quick Start
    st.subheader("🚀 Quick Start — Build Your First Automation")
    qs_col1, qs_col2, qs_col3 = st.columns(3)

    with qs_col1:
        st.markdown(
            '<div class="metric-card">'
            "<h4>Step 1: Choose a Trigger</h4>"
            "<p>Select which app event starts your workflow — a new email, form submission, "
            "Slack message, or any of 600+ triggers.</p>"
            "</div>",
            unsafe_allow_html=True,
        )

    with qs_col2:
        st.markdown(
            '<div class="metric-card">'
            "<h4>Step 2: Add Actions</h4>"
            "<p>Define what happens next — create a record, send a notification, update a sheet, "
            "post to a channel, and more.</p>"
            "</div>",
            unsafe_allow_html=True,
        )

    with qs_col3:
        st.markdown(
            '<div class="metric-card">'
            "<h4>Step 3: Activate & Monitor</h4>"
            "<p>Turn on your automation and watch it run. Track executions, errors, "
            "and performance from your dashboard.</p>"
            "</div>",
            unsafe_allow_html=True,
        )

    st.markdown(
        '<div class="cta-banner">'
        '👉 <a href="https://appypieautomate.ai/signup">Sign up free</a> and '
        '<a href="https://appypieautomate.ai/dashboard">create your first automation</a> in under 3 minutes.'
        "</div>",
        unsafe_allow_html=True,
    )

    # Popular Integrations
    st.markdown("---")
    st.subheader("🔥 Most Popular Integrations")
    popular = registry.get_popular_connectors()
    cols = st.columns(4)
    for i, connector in enumerate(popular[:8]):
        with cols[i % 4]:
            st.markdown(
                f'<div class="workflow-card">'
                f'<h4>{connector["icon"]} {connector["name"]}</h4>'
                f'<p>{connector["description"]}</p>'
                f'<span class="connector-badge">{connector["category"]}</span>'
                f"</div>",
                unsafe_allow_html=True,
            )

    st.info(
        "💡 **Tip:** Use Appy Pie Automate to connect these apps without writing code. "
        "[Explore all integrations →](https://appypieautomate.ai/integrations)"
    )


# ─── App Connectors Page ─────────────────────────────────────────────────────
elif page == "🔗 App Connectors":
    st.header("🔗 App Connectors Library")
    st.markdown(
        "Browse and test connectors for 600+ apps. Each connector provides "
        "triggers, actions, and search capabilities. "
        "[Full integration list →](https://appypieautomate.ai/integrations)"
    )

    search_term = st.text_input("🔍 Search connectors...", placeholder="e.g. Gmail, Slack, Sheets")
    category_filter = st.multiselect(
        "Filter by category",
        ["CRM", "Email", "Productivity", "Social Media", "E-Commerce", "Dev Tools",
         "Marketing", "Finance", "HR", "Support", "Storage", "Communication"],
    )

    connectors = registry.get_all_connectors()
    if search_term:
        connectors = [c for c in connectors if search_term.lower() in c["name"].lower()]
    if category_filter:
        connectors = [c for c in connectors if c["category"] in category_filter]

    st.markdown(f"**Showing {len(connectors)} connectors**")

    for connector in connectors:
        with st.expander(f'{connector["icon"]} {connector["name"]} — {connector["category"]}'):
            st.markdown(f'**Description:** {connector["description"]}')
            st.markdown(f'**Auth Type:** `{connector["auth_type"]}`')

            tcol, acol = st.columns(2)
            with tcol:
                st.markdown("**Triggers:**")
                for t in connector["triggers"]:
                    st.markdown(f"- `{t}`")
            with acol:
                st.markdown("**Actions:**")
                for a in connector["actions"]:
                    st.markdown(f"- `{a}`")

            st.markdown(
                f'[Use this integration on Appy Pie Automate →]'
                f'(https://appypieautomate.ai/integrations/{connector["slug"]})'
            )

    st.markdown(
        '<div class="cta-banner">'
        "Need a connector that's not listed? "
        '<a href="https://appypieautomate.ai/integrations">Browse all 600+ integrations</a> '
        "on Appy Pie Automate."
        "</div>",
        unsafe_allow_html=True,
    )


# ─── Workflow Builder Page ────────────────────────────────────────────────────
elif page == "🔄 Workflow Builder":
    st.header("🔄 Visual Workflow Builder")
    st.markdown(
        "Design automation workflows step by step. For a full visual builder with drag-and-drop, "
        "use the [Appy Pie Automate Dashboard](https://appypieautomate.ai/dashboard)."
    )

    workflow_name = st.text_input("Workflow Name", value="My Automation")

    st.subheader("1️⃣ Trigger Configuration")
    trigger_app = st.selectbox(
        "Trigger App",
        [c["name"] for c in registry.get_all_connectors()],
    )
    trigger_connector = registry.get_connector_by_name(trigger_app)
    if trigger_connector:
        trigger_event = st.selectbox("Trigger Event", trigger_connector["triggers"])

    st.subheader("2️⃣ Action Configuration")
    num_actions = st.number_input("Number of actions", min_value=1, max_value=10, value=1)

    actions = []
    for i in range(int(num_actions)):
        st.markdown(f"**Action {i + 1}**")
        acol1, acol2 = st.columns(2)
        with acol1:
            action_app = st.selectbox(
                f"Action App #{i+1}",
                [c["name"] for c in registry.get_all_connectors()],
                key=f"action_app_{i}",
            )
        with acol2:
            action_connector = registry.get_connector_by_name(action_app)
            if action_connector:
                action_event = st.selectbox(
                    f"Action Event #{i+1}",
                    action_connector["actions"],
                    key=f"action_event_{i}",
                )
                actions.append({"app": action_app, "event": action_event})

    st.subheader("3️⃣ Workflow Preview")
    workflow_config = engine.build_workflow(
        name=workflow_name,
        trigger={"app": trigger_app, "event": trigger_event if trigger_connector else ""},
        actions=actions,
    )
    st.json(workflow_config)

    col_save, col_deploy = st.columns(2)
    with col_save:
        if st.button("💾 Save Workflow JSON", use_container_width=True):
            st.download_button(
                "Download workflow.json",
                json.dumps(workflow_config, indent=2),
                "workflow.json",
                "application/json",
            )
    with col_deploy:
        st.link_button(
            "🚀 Deploy on Appy Pie Automate",
            "https://appypieautomate.ai/dashboard",
            use_container_width=True,
        )


# ─── Templates Gallery Page ──────────────────────────────────────────────────
elif page == "📋 Templates Gallery":
    st.header("📋 Automation Templates Gallery")
    st.markdown(
        "Pre-built workflow templates to get started instantly. "
        "Click any template to deploy it on [Appy Pie Automate](https://appypieautomate.ai/dashboard)."
    )

    template_category = st.selectbox(
        "Filter by category",
        ["All", "Sales & CRM", "Marketing", "Productivity", "E-Commerce",
         "Support", "HR & Recruiting", "DevOps", "Social Media"],
    )

    all_templates = templates.get_all_templates()
    if template_category != "All":
        all_templates = [t for t in all_templates if t["category"] == template_category]

    for tmpl in all_templates:
        with st.container():
            st.markdown(
                f'<div class="workflow-card">'
                f'<h4>{tmpl["icon"]} {tmpl["name"]}</h4>'
                f'<p>{tmpl["description"]}</p>'
                f'<span class="connector-badge">{tmpl["trigger_app"]} → {tmpl["action_app"]}</span> '
                f'<span class="connector-badge">{tmpl["category"]}</span>'
                f"</div>",
                unsafe_allow_html=True,
            )

            tcol1, tcol2 = st.columns([3, 1])
            with tcol1:
                with st.expander("View workflow JSON"):
                    st.json(tmpl["config"])
            with tcol2:
                st.link_button(
                    "Use Template →",
                    f'https://appypieautomate.ai/dashboard?template={tmpl["slug"]}',
                    use_container_width=True,
                )

    st.markdown(
        '<div class="cta-banner">'
        "Want more templates? Explore hundreds of ready-made automations at "
        '<a href="https://appypieautomate.ai/integrations">Appy Pie Automate Integrations</a>.'
        "</div>",
        unsafe_allow_html=True,
    )


# ─── Webhook Tester Page ─────────────────────────────────────────────────────
elif page == "🧪 Webhook Tester":
    st.header("🧪 Webhook & API Tester")
    st.markdown(
        "Test webhooks and API endpoints for your automations. "
        "For production webhook management, use [Appy Pie Automate](https://appypieautomate.ai/dashboard)."
    )

    method = st.selectbox("HTTP Method", ["GET", "POST", "PUT", "PATCH", "DELETE"])
    url = st.text_input("Endpoint URL", placeholder="https://api.example.com/webhook")
    headers_input = st.text_area(
        "Headers (JSON)",
        value='{\n  "Content-Type": "application/json"\n}',
        height=100,
    )

    if method in ("POST", "PUT", "PATCH"):
        body_input = st.text_area(
            "Request Body (JSON)",
            value='{\n  "key": "value"\n}',
            height=150,
        )

    if st.button("🚀 Send Request", use_container_width=True):
        if url:
            with st.spinner("Sending request..."):
                result = helpers.test_webhook(
                    method=method,
                    url=url,
                    headers=json.loads(headers_input) if headers_input else {},
                    body=json.loads(body_input) if method in ("POST", "PUT", "PATCH") and body_input else None,
                )
                st.success(f"Response received in {result['elapsed_ms']}ms")
                st.json(result)
        else:
            st.warning("Please enter a URL.")

    st.info(
        "💡 **Pro Tip:** Set up webhooks as triggers in your "
        "[Appy Pie Automate workflows](https://appypieautomate.ai/dashboard) "
        "to receive real-time data from any app."
    )


# ─── Analytics Page ───────────────────────────────────────────────────────────
elif page == "📊 Automation Analytics":
    st.header("📊 Automation Analytics Dashboard")
    st.markdown(
        "Monitor your workflow performance. For full analytics with real data, "
        "[login to Appy Pie Automate](https://appypieautomate.ai/login)."
    )

    # Demo metrics
    mcol1, mcol2, mcol3, mcol4 = st.columns(4)
    with mcol1:
        st.metric("Total Executions", "12,847", "+1,230 this week")
    with mcol2:
        st.metric("Success Rate", "99.2%", "+0.3%")
    with mcol3:
        st.metric("Active Workflows", "24", "+3 new")
    with mcol4:
        st.metric("Time Saved", "186 hrs", "+22 hrs/week")

    # Demo chart
    import pandas as pd
    import numpy as np

    dates = pd.date_range(start="2026-01-01", periods=90, freq="D")
    demo_data = pd.DataFrame({
        "Date": dates,
        "Executions": np.random.poisson(150, 90).cumsum(),
        "Errors": np.random.poisson(2, 90),
    })

    st.subheader("Execution Trends")
    st.line_chart(demo_data.set_index("Date")["Executions"])

    st.subheader("Error Rate")
    st.bar_chart(demo_data.set_index("Date")["Errors"])

    st.markdown(
        '<div class="cta-banner">'
        "📈 Get real-time analytics for your automations — "
        '<a href="https://appypieautomate.ai/login">Login to your dashboard</a>.'
        "</div>",
        unsafe_allow_html=True,
    )


# ─── Settings Page ───────────────────────────────────────────────────────────
elif page == "⚙️ Settings":
    st.header("⚙️ Configuration & API Keys")
    st.markdown(
        "Configure your local toolkit settings. "
        "For cloud automation management, visit your "
        "[Appy Pie Automate Dashboard](https://appypieautomate.ai/dashboard)."
    )

    with st.expander("🔑 API Configuration"):
        api_key = st.text_input("Appy Pie Automate API Key", type="password",
                                help="Get your API key from https://appypieautomate.ai/dashboard")
        if st.button("Validate Key"):
            if api_key:
                is_valid = auth_manager.validate_api_key(api_key)
                if is_valid:
                    st.success("API key is valid!")
                else:
                    st.error("Invalid API key. Get one at https://appypieautomate.ai/dashboard")
            else:
                st.warning("Please enter an API key.")

    with st.expander("🌐 Webhook Settings"):
        webhook_url = st.text_input("Default Webhook URL")
        webhook_secret = st.text_input("Webhook Secret", type="password")

    with st.expander("📧 Notification Settings"):
        email = st.text_input("Notification Email")
        notify_on_error = st.checkbox("Notify on workflow errors", value=True)
        notify_on_success = st.checkbox("Notify on workflow completion", value=False)

    st.divider()
    st.markdown(
        "**Resources:**\n"
        "- [Appy Pie Automate — Main Site](https://appypieautomate.ai)\n"
        "- [Create an Automation](https://appypieautomate.ai/dashboard)\n"
        "- [Sign Up Free](https://appypieautomate.ai/signup)\n"
        "- [Login](https://appypieautomate.ai/login)\n"
        "- [Knowledge Base](https://appypieautomate.ai/kb)\n"
        "- [All Integrations](https://appypieautomate.ai/integrations)\n"
        "- [Appy Pie (Parent)](https://www.appypie.com)\n"
    )


# ─── Footer ──────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown(
    "Built with ❤️ by [Appy Pie Automate](https://appypieautomate.ai) • "
    "[GitHub](https://github.com/nicehash/appypie-automate-toolkit) • "
    "[Docs](https://appypieautomate.ai/kb) • "
    "[Create Free Account](https://appypieautomate.ai/signup) • "
    "[Login](https://appypieautomate.ai/login)"
)
