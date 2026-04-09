---
layout: topic
title: Docker Core Concepts
category: docker
day: 1
date: 2026-04-09
description: Introduction to Docker - containers, images, and basic concepts
---

# Docker Core Concepts

## What is Docker?

Docker is a platform that packages applications and their dependencies into **containers** - lightweight, portable units that run consistently across any environment.

> **Think of it like this:** A container is like a shipping container for software. Everything the app needs is inside, and it works the same everywhere.

---

## Key Concepts

### Container vs Virtual Machine

| Feature | Container | Virtual Machine |
|---------|-----------|-----------------|
| Boot time | Seconds | Minutes |
| Size | MBs | GBs |
| OS | Shares host kernel | Full OS |
| Isolation | Process level | Hardware level |
| Performance | Near native | Overhead |

### Docker Image

- A **read-only template** with instructions to create a container
- Built from a `Dockerfile`
- Stored in registries (Docker Hub, ECR, ACR)

### Docker Container

- A **running instance** of an image
- Isolated environment with its own filesystem, network, and processes
- Ephemeral by default (data lost when stopped)

### Docker Registry

- Storage for Docker images
- **Docker Hub** - public registry
- **Private registries** - ECR (AWS), ACR (Azure), GCR (Google)

---

## Basic Commands

```bash
# Pull an image
docker pull nginx

# Run a container
docker run -d -p 80:80 nginx

# List running containers
docker ps

# List all containers
docker ps -a

# Stop a container
docker stop <container_id>

# Remove a container
docker rm <container_id>

# List images
docker images

# Remove an image
docker rmi <image_id>
```

---

## Interview Questions

<div class="qa-section">

<div class="question">
Q1: What is the difference between Docker image and container?
</div>
<div class="answer">
An **image** is a read-only template (like a class), while a **container** is a running instance of that image (like an object). You can create multiple containers from one image.
</div>

<div class="question">
Q2: Why use containers over VMs?
</div>
<div class="answer">

- **Faster startup** - seconds vs minutes
- **Lightweight** - share host OS kernel
- **Portable** - runs the same everywhere
- **Resource efficient** - less overhead
- **Better for microservices** - one process per container
</div>

<div class="question">
Q3: What is Docker daemon?
</div>
<div class="answer">
The Docker daemon (`dockerd`) is the background service that manages Docker objects (images, containers, networks, volumes). The Docker CLI communicates with the daemon via REST API.
</div>

<div class="question">
Q4: Explain Docker architecture.
</div>
<div class="answer">
Docker uses a **client-server architecture**:

1. **Docker Client** - CLI tool (`docker` command)
2. **Docker Daemon** - background service managing containers
3. **Docker Registry** - stores images (Docker Hub)

The client sends commands to the daemon, which builds, runs, and manages containers.
</div>

<div class="question">
Q5: What happens when you run `docker run nginx`?
</div>
<div class="answer">

1. Docker checks for `nginx` image locally
2. If not found, pulls from Docker Hub
3. Creates a new container from the image
4. Allocates filesystem and network
5. Starts the container
6. Runs the default command (nginx server)
</div>

</div>

---

## Scenario-Based Questions

<div class="qa-section">

<div class="question">
Scenario: Your container exits immediately after starting. How do you debug?
</div>
<div class="answer">

1. Check logs: `docker logs <container_id>`
2. Run interactively: `docker run -it <image> /bin/sh`
3. Check exit code: `docker inspect <container_id> | grep ExitCode`
4. Common causes:
   - Main process exits
   - Missing environment variables
   - Incorrect entrypoint
</div>

<div class="question">
Scenario: How would you reduce Docker image size?
</div>
<div class="answer">

1. Use **multi-stage builds** - separate build and runtime
2. Use **alpine** base images (~5MB vs ~100MB)
3. **Combine RUN commands** - fewer layers
4. Use `.dockerignore` - exclude unnecessary files
5. **Clean up** in same layer - `apt-get clean`
</div>

</div>

---

## Architecture Questions

<div class="qa-section">

<div class="question">
Q: Design a containerized microservices deployment.
</div>
<div class="answer">

```
                    ┌─────────────────┐
                    │   Load Balancer │
                    └────────┬────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
   ┌────▼────┐         ┌─────▼────┐         ┌────▼────┐
   │ API GW  │         │ Service A │         │ Service B│
   │Container│         │ Container │         │Container│
   └────┬────┘         └─────┬─────┘         └────┬────┘
        │                    │                    │
        └────────────────────┼────────────────────┘
                             │
                    ┌────────▼────────┐
                    │    Database     │
                    │   (Container)   │
                    └─────────────────┘
```

**Key considerations:**
- One service per container
- Use orchestrator (K8s) for production
- Shared network for inter-service communication
- Persistent volumes for databases
</div>

</div>

---

## Quick Tips

- Always use specific image tags (not `latest`)
- One process per container
- Containers should be ephemeral
- Use `.dockerignore` to reduce build context
- Run as non-root user for security

---

*Next: [Day 2 - Docker Networking](day-02-networking.md)*
