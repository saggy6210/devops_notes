---
layout: default
title: Kubernetes
description: Kubernetes container orchestration - concepts, commands, and interview preparation
---

# ☸️ Kubernetes

Master Kubernetes from fundamentals to production-ready deployments.

## What You'll Learn

- Kubernetes architecture
- Pods, Deployments, Services
- ConfigMaps and Secrets
- Storage and Volumes
- Networking concepts
- Helm charts
- RBAC and Security
- Troubleshooting

---

## Daily Notes

<ul class="notes-list">
{% assign k8s_notes = site.pages | where_exp: "page", "page.path contains 'topics/kubernetes/'" | where_exp: "page", "page.name != 'index.md'" | sort: "day" %}
{% for note in k8s_notes %}
<li>
    <a href="{{ note.url | relative_url }}">
        <span class="title">Day {{ note.day }}: {{ note.title }}</span>
        <span class="meta">{{ note.date | date: "%b %d, %Y" }}</span>
    </a>
</li>
{% endfor %}
</ul>

{% if k8s_notes.size == 0 %}
*Notes coming soon! Check back daily for updates.*
{% endif %}

---

## Quick Reference

| Resource | Command |
|----------|---------|
| Pods | `kubectl get pods` |
| Deployments | `kubectl get deployments` |
| Services | `kubectl get svc` |
| Logs | `kubectl logs <pod>` |
| Exec | `kubectl exec -it <pod> -- /bin/sh` |

---

[← Back to Home]({{ '/' | relative_url }})
