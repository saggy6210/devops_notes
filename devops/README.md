# DevOps Learning Hub

A comprehensive DevOps learning repository with daily notes, concepts, and interview preparation materials.

## 🌐 Website

Visit the live site: [DevOps Learning Hub](https://saggy6210.github.io/devops_notes/devops/)

## 📚 Topics Covered

- **Docker** - Container technology
- **Kubernetes** - Container orchestration
- **Terraform** - Infrastructure as Code
- **Ansible** - Configuration management
- **Azure** - Microsoft Cloud
- **AWS** - Amazon Web Services
- **Bash** - Shell scripting
- **Python** - Automation & scripting
- **Monitoring** - Grafana, Prometheus, Datadog
- **CI/CD** - GitLab, GitHub Actions, Jenkins

## 📖 Content Structure

Each topic includes:
- Core concepts (simple terms)
- Short notes
- Interview Q&A
- Scenario-based questions
- Architecture questions
- Real-world examples

## 🔄 Daily Updates

Content is updated daily via automated GitHub Actions pipeline using AI-generated content.

## 🏗️ Local Development

```bash
# Install Jekyll
gem install bundler jekyll

# Run locally
cd devops
bundle install
bundle exec jekyll serve

# Visit http://localhost:4000
```

## 🤖 Automation

The repository uses GitHub Actions to:
- Generate daily content using Gemini AI
- Auto-commit and push updates
- Deploy to GitHub Pages

## 📁 Structure

```
devops/
├── _config.yml          # Jekyll configuration
├── index.md             # Landing page
├── topics/
│   ├── docker/          # Docker notes
│   ├── kubernetes/      # K8s notes
│   ├── terraform/       # Terraform notes
│   └── ...
├── scripts/
│   └── content_generator.py  # AI content generator
├── prompts/
│   └── devops_content.txt    # Gemini prompts
└── .github/workflows/
    └── daily-content.yml     # Automation pipeline
```

## 🎯 Goal

Build a complete DevOps learning resource over time with:
- High-quality notes
- Interview preparation material
- Real-world scenarios
- Daily updates

## 📝 License

MIT License - Feel free to use and contribute!

---

*Made with ❤️ for the DevOps community*
