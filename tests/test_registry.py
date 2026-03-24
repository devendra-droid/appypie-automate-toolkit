"""Tests for the connector registry module."""

import pytest
from src.connectors import registry


def test_get_all_connectors():
    connectors = registry.get_all_connectors()
    assert len(connectors) > 0
    assert all("name" in c for c in connectors)
    assert all("triggers" in c for c in connectors)
    assert all("actions" in c for c in connectors)


def test_get_popular_connectors():
    popular = registry.get_popular_connectors()
    assert len(popular) == 8
    names = [c["name"] for c in popular]
    assert "Gmail" in names
    assert "Slack" in names


def test_get_connector_by_name():
    gmail = registry.get_connector_by_name("Gmail")
    assert gmail is not None
    assert gmail["slug"] == "gmail"
    assert "Send Email" in gmail["actions"]

    missing = registry.get_connector_by_name("NonExistentApp")
    assert missing is None


def test_get_connector_by_slug():
    slack = registry.get_connector_by_slug("slack")
    assert slack is not None
    assert slack["name"] == "Slack"


def test_get_connectors_by_category():
    crm = registry.get_connectors_by_category("CRM")
    assert len(crm) >= 2
    assert all(c["category"] == "CRM" for c in crm)


def test_search_connectors():
    results = registry.search_connectors("email")
    assert len(results) > 0

    results = registry.search_connectors("shopify")
    assert any(c["name"] == "Shopify" for c in results)


def test_get_categories():
    categories = registry.get_categories()
    assert "CRM" in categories
    assert "Email" in categories
    assert "Productivity" in categories
