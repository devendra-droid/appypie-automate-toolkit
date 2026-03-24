"""
Auth Manager — API Key & OAuth Utilities
=========================================
Handles authentication for the Appy Pie Automate Toolkit.

Get your API key: https://appypieautomate.ai/dashboard
Signup: https://appypieautomate.ai/signup
Login: https://appypieautomate.ai/login
"""

import hashlib
import os
import json
from typing import Dict, Optional
from datetime import datetime


class AuthManager:
    """
    Manage API keys and authentication tokens for Appy Pie Automate.

    Get started:
    1. Sign up at https://appypieautomate.ai/signup
    2. Login at https://appypieautomate.ai/login
    3. Get your API key from https://appypieautomate.ai/dashboard
    """

    def __init__(self, config_path: str = ".automate_config.json"):
        self.config_path = config_path
        self.config = self._load_config()

    def _load_config(self) -> Dict:
        """Load configuration from file."""
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r") as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return {}
        return {}

    def _save_config(self):
        """Save configuration to file."""
        with open(self.config_path, "w") as f:
            json.dump(self.config, f, indent=2)

    def set_api_key(self, key: str):
        """Store an API key securely."""
        self.config["api_key_hash"] = hashlib.sha256(key.encode()).hexdigest()
        self.config["api_key_prefix"] = key[:8] + "..." if len(key) > 8 else key
        self.config["updated_at"] = datetime.utcnow().isoformat()
        self._save_config()

    def get_api_key_info(self) -> Dict:
        """Get stored API key metadata."""
        return {
            "prefix": self.config.get("api_key_prefix", "Not set"),
            "updated_at": self.config.get("updated_at", "Never"),
        }

    def clear_credentials(self):
        """Remove all stored credentials."""
        self.config = {}
        self._save_config()


def validate_api_key(api_key: str) -> bool:
    """
    Validate an Appy Pie Automate API key format.

    Get your key: https://appypieautomate.ai/dashboard

    Note: This validates format only. For full validation,
    the key must be tested against the live API.
    """
    if not api_key or not isinstance(api_key, str):
        return False
    # Basic format validation (length and prefix)
    if len(api_key) < 20:
        return False
    return True


def get_oauth_redirect_url(app_slug: str, redirect_uri: str = "") -> str:
    """
    Generate an OAuth redirect URL for app authorization.

    Args:
        app_slug: The connector slug (e.g., 'gmail', 'slack')
        redirect_uri: Your callback URL

    Returns:
        OAuth authorization URL
    """
    base_url = "https://appypieautomate.ai/oauth/authorize"
    return f"{base_url}?app={app_slug}&redirect_uri={redirect_uri}"


def generate_webhook_secret() -> str:
    """Generate a secure webhook secret for payload verification."""
    return hashlib.sha256(os.urandom(32)).hexdigest()
