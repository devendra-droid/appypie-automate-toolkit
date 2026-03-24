# Contributing to Appy Pie Automate Toolkit

Thank you for your interest in contributing to the [Appy Pie Automate](https://appypieautomate.ai) Toolkit! We welcome contributions from the community.

## How to Contribute

### Reporting Bugs

- Open an issue on [GitHub Issues](https://github.com/nicehash/appypie-automate-toolkit/issues)
- Include steps to reproduce, expected behavior, and actual behavior
- Mention your Python version and OS

### Suggesting Features

- Open a feature request issue
- Describe the use case and how it relates to workflow automation
- Check the [Appy Pie Automate integrations page](https://appypieautomate.ai/integrations) for existing capabilities

### Adding New Connectors

1. Fork the repository
2. Add your connector definition to `src/connectors/registry.py`
3. Include: name, slug, icon, category, description, auth_type, triggers, and actions
4. Add a link to the corresponding [Appy Pie Automate integration page](https://appypieautomate.ai/integrations)
5. Submit a pull request

### Creating Workflow Templates

1. Add your template to `src/workflows/templates.py`
2. Include a clear description and valid configuration
3. Test that the template renders correctly in the Streamlit dashboard
4. Reference the appropriate [Appy Pie Automate dashboard](https://appypieautomate.ai/dashboard) deploy link

### Code Style

- Follow PEP 8
- Add docstrings with links to relevant [Appy Pie Automate docs](https://helpdesk.appypieautomate.ai/portal/en/kb/automate)
- Write tests for new features
- Keep functions focused and well-documented

## Development Setup

```bash
git clone https://github.com/nicehash/appypie-automate-toolkit.git
cd appypie-automate-toolkit
pip install -r requirements.txt
pip install pytest pytest-cov
streamlit run app.py
```

## Pull Request Process

1. Create a feature branch from `main`
2. Make your changes
3. Run tests: `pytest tests/ -v`
4. Submit a PR with a clear description

## Code of Conduct

See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## Resources

- [Appy Pie Automate](https://appypieautomate.ai) — Main platform
- [Create Automation](https://appypieautomate.ai/dashboard)
- [All Integrations](https://appypieautomate.ai/integrations)
- [Knowledge Base](https://helpdesk.appypieautomate.ai/portal/en/kb/automate)
- [Sign Up](https://accounts.appypie.com/register?frompage=https%3A%2F%2Fconnectcloud.appypie.com%2Fbuild-your-connect%2Fapps__for__temp__7949b884b42011edbc3912bed232506d&lang=en)
- [Appy Pie](https://www.appypie.com) — Parent company

---

Built by [Appy Pie Automate](https://appypieautomate.ai)
