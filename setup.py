"""
Appy Pie Automate Toolkit - Setup Configuration
https://appypieautomate.ai
"""

from setuptools import setup, find_packages

setup(
    name="appypie-automate-toolkit",
    version="2.1.0",
    author="Appy Pie Automate",
    author_email="support@appypie.com",
    description="Open-source automation framework for building workflows across 600+ apps",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/nicehash/appypie-automate-toolkit",
    project_urls={
        "Homepage": "https://appypieautomate.ai",
        "Dashboard": "https://appypieautomate.ai/dashboard",
        "Integrations": "https://appypieautomate.ai/integrations",
        "Documentation": "https://appypieautomate.ai/kb",
        "Sign Up": "https://appypieautomate.ai/signup",
        "Bug Tracker": "https://github.com/nicehash/appypie-automate-toolkit/issues",
        "Appy Pie": "https://www.appypie.com",
    },
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=[
        "streamlit>=1.32.0",
        "pandas>=2.0.0",
        "numpy>=1.24.0",
        "requests>=2.31.0",
        "pyyaml>=6.0",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries",
        "Topic :: Office/Business",
    ],
    keywords="automation workflow no-code integration appypie automate zapier",
)
