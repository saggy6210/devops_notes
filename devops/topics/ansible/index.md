---
layout: default
title: Ansible
description: Ansible configuration management - playbooks, roles, and interview preparation
---

# ⚙️ Ansible

Master configuration management and automation with Ansible.

## What You'll Learn

- Ansible architecture
- Inventory management
- Ad-hoc commands
- Playbooks
- Roles and collections
- Variables and facts
- Templates (Jinja2)
- Ansible Vault

---

## Daily Notes

<ul class="notes-list">
{% assign ansible_notes = site.pages | where_exp: "page", "page.path contains 'topics/ansible/'" | where_exp: "page", "page.name != 'index.md'" | sort: "day" %}
{% for note in ansible_notes %}
<li>
    <a href="{{ note.url | relative_url }}">
        <span class="title">Day {{ note.day }}: {{ note.title }}</span>
        <span class="meta">{{ note.date | date: "%b %d, %Y" }}</span>
    </a>
</li>
{% endfor %}
</ul>

{% if ansible_notes.size == 0 %}
*Notes coming soon! Check back daily for updates.*
{% endif %}

---

## Quick Reference

| Command | Description |
|---------|-------------|
| `ansible all -m ping` | Test connectivity |
| `ansible-playbook` | Run playbook |
| `ansible-galaxy` | Manage roles |
| `ansible-vault` | Encrypt secrets |

---

[← Back to Home]({{ '/' | relative_url }})
