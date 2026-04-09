---
layout: default
title: Python for DevOps
description: Python scripting for automation - tools, libraries, and interview preparation
---

# 🐍 Python for DevOps

Learn Python for DevOps automation and tooling.

## What You'll Learn

- Python basics for DevOps
- File and system operations
- API interactions (requests)
- AWS SDK (boto3)
- Azure SDK
- Automation scripts
- Testing with pytest
- Popular DevOps tools

---

## Daily Notes

<ul class="notes-list">
{% assign python_notes = site.pages | where_exp: "page", "page.path contains 'topics/python/'" | where_exp: "page", "page.name != 'index.md'" | sort: "day" %}
{% for note in python_notes %}
<li>
    <a href="{{ note.url | relative_url }}">
        <span class="title">Day {{ note.day }}: {{ note.title }}</span>
        <span class="meta">{{ note.date | date: "%b %d, %Y" }}</span>
    </a>
</li>
{% endfor %}
</ul>

{% if python_notes.size == 0 %}
*Notes coming soon! Check back daily for updates.*
{% endif %}

---

## Quick Reference

| Library | Purpose |
|---------|---------|
| `boto3` | AWS SDK |
| `azure-sdk` | Azure SDK |
| `requests` | HTTP client |
| `paramiko` | SSH client |
| `pyyaml` | YAML parser |

---

[← Back to Home]({{ '/' | relative_url }})
