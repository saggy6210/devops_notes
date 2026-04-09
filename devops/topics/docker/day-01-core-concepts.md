---
layout: topic
title: Core Concepts
category: docker
day: 1
date: 2026-04-09
description: Docker - Core Concepts
---

# Core Concepts

## Core Concepts

Docker is an open-source platform that automates the deployment, scaling, and management of applications using containerization. It packages an application and all its dependencies into a standardized unit called a **container**. This ensures that the application runs consistently across any environment, from development to production.

**Key Components:**

*   **Dockerfile:** A text file containing instructions to build a Docker image.
*   **Image:** A lightweight, standalone, executable package that includes everything needed to run a piece of software, including the code, a runtime, libraries, environment variables, and config files. Images are read-only templates.
*   **Container:** A runnable instance of an image. You can create, start, stop, move, or delete a container. It's an isolated environment where your application runs.
*   **Docker Engine:** The client-server application that builds and runs containers. It consists of:
    *   **Docker Daemon (dockerd):** The background service that manages Docker objects like images, containers, networks, and volumes.
    *   **Docker Client (docker):** The command-line interface (CLI) that allows users to interact with the Docker Daemon.
    *   **REST API:** Specifies how the Docker Client communicates with the Daemon.
*   **Docker Registry:** A storage and distribution system for Docker images.
    *   **Docker Hub:** Docker's public registry, where you can find official images and host your own.
    *   **Private Registries:** Used for storing proprietary images within an organization.

## Key Points

*   **Portability:** Containers encapsulate an application and its dependencies, making it easy to move across different environments (laptop, VM, cloud).
*   **Consistency:** Eliminates "it works on my machine" problems by providing a consistent runtime environment.
*   **Isolation:** Containers run in isolated environments, preventing conflicts between applications and their dependencies.
*   **Resource Efficiency:** Containers share the host OS kernel, making them much lighter and faster to start than traditional virtual machines.
*   **Version Control:** Docker images can be versioned, allowing for easy rollbacks and tracking changes.
*   **Modularity:** Encourages breaking down applications into smaller, independent services (microservices).

## Commands/Syntax

Here are some fundamental Docker commands:

*   **Pull an image from Docker Hub:**
    ```bash
    docker pull ubuntu:latest
    ```
*   **Run a container from an image:**
    ```bash
    docker run -it ubuntu:latest /bin/bash
    # -i: interactive, -t: pseudo-TTY
    # This will start an Ubuntu container and give you a bash shell inside it.
    ```
*   **List running containers:**
    ```bash
    docker ps
    ```
*   **List all containers (including stopped ones):**
    ```bash
    docker ps -a
    ```
*   **List all images:**
    ```bash
    docker images
    ```
*   **Stop a running container:**
    ```bash
    docker stop <container_id_or_name>
    ```
*   **Remove a stopped container:**
    ```bash
    docker rm <container_id_or_name>
    ```
*   **Remove an image:**
    ```bash
    docker rmi <image_id_or_name>
    ```
*   **Build an image from a Dockerfile (assuming Dockerfile is in current directory):**
    ```bash
    docker build -t myapp:1.0 .
    # -t: tag the image with a name and version
    # .: context path (current directory)
    ```

## Interview Questions

1.  **What is Docker and why is it used?**
    *   **Answer:** Docker is a platform for developing, shipping, and running applications using containerization. It's used to package applications and their dependencies into isolated units (containers) to ensure consistent execution across different environments, improving portability, scalability, and efficiency.

2.  **Explain the difference between a Docker Image and a Docker Container.**
    *   **Answer:** A **Docker Image** is a read-only template that contains the application and all its dependencies. It's like a blueprint or a class. A **Docker Container** is a runnable instance of an image. It's a live, isolated environment where the application defined by the image actually runs, like an object created from a class.

3.  **What is a Dockerfile?**
    *   **Answer:** A Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image. It's essentially a script that Docker Engine uses to build an image automatically.

4.  **What is Docker Hub?**
    *   **Answer:** Docker Hub is a cloud-based registry service provided by Docker. It's a central repository where users can find, store, and share Docker images. It hosts official images from vendors and allows users to publish their own images.

5.  **Describe the Docker Engine's main components.**
    *   **Answer:** The Docker Engine consists of three main components:
        *   **Docker Daemon (dockerd):** The server-side process that manages Docker objects.
        *   **Docker Client (docker):** The command-line tool that interacts with the Daemon.
        *   **REST API:** The interface through which the Client communicates with the Daemon.

6.  **What are the primary benefits of using Docker?**
    *   **Answer:** Key benefits include:
        *   **Portability:** Applications run consistently anywhere.
        *   **Isolation:** Applications are isolated from each other and the host system.
        *   **Resource Efficiency:** Lighter than VMs, sharing the host OS kernel.
        *   **Faster Deployment:** Quick startup times and easy scaling.
        *   **Version Control:** Images can be versioned and easily rolled back.

7.  **How does Docker achieve isolation for containers?**
    *   **Answer:** Docker leverages Linux kernel features like **namespaces** and **cgroups**.
        *   **Namespaces:** Provide isolated views of system resources (e.g., process IDs, network interfaces, mount points).
        *   **cgroups (control groups):** Limit and account for resource usage (CPU, memory, I/O) for a group of processes.

## Scenario Questions

1.  **Scenario:** A development team frequently faces "it works on my machine" issues when deploying their Python web application to staging and production environments. How can Docker help resolve this problem?
    *   **Answer:** Docker can resolve this by containerizing the Python application. The team would create a Dockerfile that specifies the exact Python version, libraries, and environment variables needed. This Dockerfile is then used to build a Docker image. This image, containing the application and all its dependencies, can then be run as a container in development, staging, and production, guaranteeing an identical runtime environment across all stages and eliminating environment-related inconsistencies.

2.  **Scenario:** You need to run an old Java application that requires a specific JDK version (e.g., Java 8) and a particular set of libraries, which conflict with other applications on your server. How would you approach this using Docker?
    *   **Answer:** I would create a Dockerfile for the Java application. This Dockerfile would start with a base image containing Java 8 (e.g., `openjdk:8-jdk-slim`). Then, I would add instructions to install the specific libraries and package the old Java application within this image. Running this as a Docker container ensures that the Java 8 environment and its specific libraries are isolated from other applications on the host, preventing conflicts and allowing the legacy application to run without affecting others.

3.  **Scenario:** Your company wants to ensure that every developer's local environment is identical to the CI/CD pipeline and production environment for a new Node.js microservice. What Docker components would you use and how?
    *   **Answer:** I would use a **Dockerfile** to define the Node.js environment, application code, and dependencies. This Dockerfile would be committed to version control. Developers would then use `docker build` to create a **Docker Image** from this Dockerfile. This same image would be used by the CI/CD pipeline to run tests and by the production environment to deploy the **Docker Container**. This ensures that the exact same environment and application package are used across all stages, guaranteeing consistency.

## Architecture Questions

1.  **Describe the high-level architecture of Docker and how its main components interact.**
    *   **Answer:** The Docker architecture is client-server based.
        *   The **Docker Client** (CLI) sends commands to the **Docker Daemon** (server).
        *   The Daemon manages Docker objects:
            *   It pulls **Images** from a **Docker Registry** (like Docker Hub).
            *   It builds Images from **Dockerfiles**.
            *   It runs, stops, and manages **Containers** based on these Images.
        *   The Daemon interacts with the underlying operating system (Linux kernel) to provide isolation and resource management for containers.

    ```
    +-------------------+       +-------------------+       +-------------------+
    |   Docker Client   | <---> |   Docker Daemon   | <---> |  Docker Registry  |
    |    (CLI: docker)  |       |    (dockerd)      |       |  (e.g., Docker Hub)|
    +-------------------+       +-------------------+       +-------------------+
                                          |
                                          | Manages
                                          V
                                +-------------------+
                                | Docker Objects:   |
                                | - Images          |
                                | - Containers      |
                                | - Networks        |
                                | - Volumes         |
                                +-------------------+
                                          |
                                          | Runs on
                                          V
                                +-------------------+
                                |   Host OS Kernel  |
                                | (Namespaces, cgroups)|
                                +-------------------+
    ```

2.  **How does Docker fit into a typical CI/CD pipeline from a high-level perspective?**
    *   **Answer:** In a CI/CD pipeline, Docker plays a crucial role in packaging and deploying applications consistently.
        1.  **Build Stage:** The CI server fetches source code, then uses a **Dockerfile** to build a **Docker Image** of the application.
        2.  **Test Stage:** The newly built Docker Image is used to spin up containers for running automated tests (unit, integration, end-to-end). This ensures tests run in an environment identical to production.
        3.  **Push Stage:** If tests pass, the Docker Image is tagged and pushed to a **Docker Registry** (e.g., Docker Hub or a private registry).
        4.  **Deploy Stage:** The CD system pulls the approved Docker Image from the registry and deploys it as a **Docker Container** to the target environment (staging, production).

    ```
    +-----------------+    +-----------------+    +-----------------+    +-----------------+
    |  Source Code    | -> |  CI Server      | -> |  Docker Registry| -> |  CD System      |
    |  (Git Repo)     |    | (Build Image,   |    | (Store Images)  |    | (Deploy Container)|
    +-----------------+    |  Run Tests)     |    +-----------------+    +-----------------+
                           +-----------------+
                                   |
                                   V
                                Dockerfile
    ```