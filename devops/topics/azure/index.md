---
layout: default
title: Azure
description: Microsoft Azure cloud platform - services, architecture, and interview preparation
---

# ☁️ Azure

Learn Microsoft Azure cloud services and architecture.

## What You'll Learn

- Azure fundamentals
- Compute services (VMs, AKS, App Services)
- Storage services
- Networking (VNet, Load Balancer)
- Azure DevOps
- ARM templates & Bicep
- Azure CLI & PowerShell
- Security and Identity (Entra ID)

---

## Daily Notes

<ul class="notes-list">
{% assign azure_notes = site.pages | where_exp: "page", "page.path contains 'topics/azure/'" | where_exp: "page", "page.name != 'index.md'" | sort: "day" %}
{% for note in azure_notes %}
<li>
    <a href="{{ note.url | relative_url }}">
        <span class="title">Day {{ note.day }}: {{ note.title }}</span>
        <span class="meta">{{ note.date | date: "%b %d, %Y" }}</span>
    </a>
</li>
{% endfor %}
</ul>

{% if azure_notes.size == 0 %}
*Notes coming soon! Check back daily for updates.*
{% endif %}

---

## Quick Reference

| Service | Purpose |
|---------|---------|
| Azure VMs | Virtual machines |
| AKS | Managed Kubernetes |
| App Service | Web app hosting |
| Blob Storage | Object storage |
| Azure DevOps | CI/CD platform |

---

[← Back to Home]({{ '/' | relative_url }})
