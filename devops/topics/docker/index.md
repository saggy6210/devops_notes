---
layout: default
title: Docker
description: Docker container technology - concepts, commands, and interview preparation
---

# 🐳 Docker

Learn Docker from basics to advanced concepts with daily notes and interview preparation.

## What You'll Learn

- Container fundamentals
- Docker commands and CLI
- Networking concepts
- Volume and storage management
- Dockerfile best practices
- Docker Compose
- Multi-stage builds
- Security best practices

---

## Daily Notes

<ul class="notes-list">
{% assign docker_notes = site.pages | where_exp: "page", "page.path contains 'topics/docker/'" | where_exp: "page", "page.name != 'index.md'" | sort: "day" %}
{% for note in docker_notes %}
<li>
    <a href="{{ note.url | relative_url }}">
        <span class="title">Day {{ note.day }}: {{ note.title }}</span>
        <span class="meta">{{ note.date | date: "%b %d, %Y" }}</span>
    </a>
</li>
{% endfor %}
</ul>

{% if docker_notes.size == 0 %}
*Notes coming soon! Check back daily for updates.*
{% endif %}

---

## Quick Reference

| Command | Description |
|---------|-------------|
| `docker run` | Run a container |
| `docker ps` | List running containers |
| `docker images` | List images |
| `docker build` | Build an image |
| `docker-compose up` | Start services |

---

[← Back to Home]({{ '/' | relative_url }})
