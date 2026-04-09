---
layout: default
title: Monitoring
description: Monitoring and observability - Grafana, Prometheus, Datadog
---

# 📊 Monitoring

Learn monitoring and observability tools for DevOps.

## What You'll Learn

- Monitoring fundamentals
- Prometheus metrics
- Grafana dashboards
- Alerting strategies
- Log aggregation (ELK)
- Datadog integration
- APM concepts
- SRE practices

---

## Daily Notes

<ul class="notes-list">
{% assign monitoring_notes = site.pages | where_exp: "page", "page.path contains 'topics/monitoring/'" | where_exp: "page", "page.name != 'index.md'" | sort: "day" %}
{% for note in monitoring_notes %}
<li>
    <a href="{{ note.url | relative_url }}">
        <span class="title">Day {{ note.day }}: {{ note.title }}</span>
        <span class="meta">{{ note.date | date: "%b %d, %Y" }}</span>
    </a>
</li>
{% endfor %}
</ul>

{% if monitoring_notes.size == 0 %}
*Notes coming soon! Check back daily for updates.*
{% endif %}

---

## Quick Reference

| Tool | Purpose |
|------|---------|
| Prometheus | Metrics collection |
| Grafana | Visualization |
| Alertmanager | Alert routing |
| Datadog | Full observability |
| ELK Stack | Log management |

---

[← Back to Home]({{ '/' | relative_url }})
