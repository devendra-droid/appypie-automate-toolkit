"""Tests for the workflow templates module."""

import pytest
from src.workflows import templates


def test_get_all_templates():
    all_tmpl = templates.get_all_templates()
    assert len(all_tmpl) > 0
    assert all("name" in t for t in all_tmpl)
    assert all("config" in t for t in all_tmpl)


def test_get_template_by_slug():
    tmpl = templates.get_template_by_slug("gmail-to-slack")
    assert tmpl["name"] == "Gmail to Slack Notifications"
    assert tmpl["trigger_app"] == "Gmail"

    missing = templates.get_template_by_slug("nonexistent")
    assert missing == {}


def test_get_templates_by_category():
    ecom = templates.get_templates_by_category("E-Commerce")
    assert len(ecom) >= 2
    assert all(t["category"] == "E-Commerce" for t in ecom)


def test_search_templates():
    results = templates.search_templates("slack")
    assert len(results) > 0

    results = templates.search_templates("shopify")
    assert any(t["trigger_app"] == "Shopify" for t in results)


def test_get_template_categories():
    categories = templates.get_template_categories()
    assert "E-Commerce" in categories
    assert "Productivity" in categories
