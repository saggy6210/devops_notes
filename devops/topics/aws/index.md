---
layout: default
title: AWS
description: Amazon Web Services - core services, architecture, and interview preparation
---

# 🌩️ AWS

Master Amazon Web Services for cloud infrastructure.

## What You'll Learn

- AWS fundamentals
- EC2 and compute services
- S3 and storage
- VPC networking
- IAM security
- EKS (Kubernetes)
- Lambda (Serverless)
- CloudFormation

---

## Daily Notes

<ul class="notes-list">
{% assign aws_notes = site.pages | where_exp: "page", "page.path contains 'topics/aws/'" | where_exp: "page", "page.name != 'index.md'" | sort: "day" %}
{% for note in aws_notes %}
<li>
    <a href="{{ note.url | relative_url }}">
        <span class="title">Day {{ note.day }}: {{ note.title }}</span>
        <span class="meta">{{ note.date | date: "%b %d, %Y" }}</span>
    </a>
</li>
{% endfor %}
</ul>

{% if aws_notes.size == 0 %}
*Notes coming soon! Check back daily for updates.*
{% endif %}

---

## Quick Reference

| Service | Purpose |
|---------|---------|
| EC2 | Virtual servers |
| S3 | Object storage |
| VPC | Virtual network |
| IAM | Identity management |
| EKS | Managed Kubernetes |

---

[← Back to Home]({{ '/' | relative_url }})
