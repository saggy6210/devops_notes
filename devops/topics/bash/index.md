---
layout: default
title: Bash Scripting
description: Shell scripting fundamentals - commands, scripts, and interview preparation
---

# 💻 Bash Scripting

Master shell scripting for automation and system administration.

## What You'll Learn

- Shell basics
- Variables and data types
- Control structures
- Functions
- File operations
- Text processing (sed, awk, grep)
- Process management
- Best practices

---

## Daily Notes

<ul class="notes-list">
{% assign bash_notes = site.pages | where_exp: "page", "page.path contains 'topics/bash/'" | where_exp: "page", "page.name != 'index.md'" | sort: "day" %}
{% for note in bash_notes %}
<li>
    <a href="{{ note.url | relative_url }}">
        <span class="title">Day {{ note.day }}: {{ note.title }}</span>
        <span class="meta">{{ note.date | date: "%b %d, %Y" }}</span>
    </a>
</li>
{% endfor %}
</ul>

{% if bash_notes.size == 0 %}
*Notes coming soon! Check back daily for updates.*
{% endif %}

---

## Quick Reference

| Command | Description |
|---------|-------------|
| `grep` | Search text patterns |
| `sed` | Stream editor |
| `awk` | Text processing |
| `find` | Find files |
| `xargs` | Build commands from input |

---

[← Back to Home]({{ '/' | relative_url }})
