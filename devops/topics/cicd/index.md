---
layout: default
title: CI/CD
description: Continuous Integration and Deployment - GitLab, GitHub Actions, Jenkins
---

# 🔄 CI/CD

Master continuous integration and deployment pipelines.

## What You'll Learn

- CI/CD fundamentals
- GitHub Actions
- GitLab CI/CD
- Jenkins pipelines
- Artifact management
- Deployment strategies
- GitOps with ArgoCD
- Security scanning

---

## Daily Notes

<ul class="notes-list">
{% assign cicd_notes = site.pages | where_exp: "page", "page.path contains 'topics/cicd/'" | where_exp: "page", "page.name != 'index.md'" | sort: "day" %}
{% for note in cicd_notes %}
<li>
    <a href="{{ note.url | relative_url }}">
        <span class="title">Day {{ note.day }}: {{ note.title }}</span>
        <span class="meta">{{ note.date | date: "%b %d, %Y" }}</span>
    </a>
</li>
{% endfor %}
</ul>

{% if cicd_notes.size == 0 %}
*Notes coming soon! Check back daily for updates.*
{% endif %}

---

## Quick Reference

| Tool | Key Feature |
|------|-------------|
| GitHub Actions | YAML workflows |
| GitLab CI | `.gitlab-ci.yml` |
| Jenkins | Jenkinsfile |
| ArgoCD | GitOps |
| Tekton | Kubernetes-native |

---

[← Back to Home]({{ '/' | relative_url }})
