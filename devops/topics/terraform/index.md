---
layout: default
title: Terraform
description: Terraform Infrastructure as Code - concepts, modules, and interview preparation
---

# 🏗️ Terraform

Learn Infrastructure as Code with Terraform.

## What You'll Learn

- HCL syntax and basics
- Providers and resources
- State management
- Modules and reusability
- Workspaces
- Backend configuration
- Best practices
- CI/CD integration

---

## Daily Notes

<ul class="notes-list">
{% assign tf_notes = site.pages | where_exp: "page", "page.path contains 'topics/terraform/'" | where_exp: "page", "page.name != 'index.md'" | sort: "day" %}
{% for note in tf_notes %}
<li>
    <a href="{{ note.url | relative_url }}">
        <span class="title">Day {{ note.day }}: {{ note.title }}</span>
        <span class="meta">{{ note.date | date: "%b %d, %Y" }}</span>
    </a>
</li>
{% endfor %}
</ul>

{% if tf_notes.size == 0 %}
*Notes coming soon! Check back daily for updates.*
{% endif %}

---

## Quick Reference

| Command | Description |
|---------|-------------|
| `terraform init` | Initialize working directory |
| `terraform plan` | Preview changes |
| `terraform apply` | Apply changes |
| `terraform destroy` | Destroy infrastructure |
| `terraform state list` | List resources in state |

---

[← Back to Home]({{ '/' | relative_url }})
