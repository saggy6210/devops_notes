# Interview Preparation

## Git Commands

## Docker

## Kubernetes
 - https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/
 - Current version is v1.18
 - Previous versions are v1.17..14
 - Kubernetes is portable, extensible, open source plateform for managing containerised workload & services, that facilitate both declarative configuration and automation. 
 - Google Open-sourced the kubernetes project in 2014.
 - Traditional deployment era: Early on, organizations ran applications on physical servers. There was no way to define resource boundaries for applications in a physical server, and this caused resource allocation issues. 
 - Virtualized deployment era: As a solution, virtualization was introduced. It allows you to run multiple Virtual Machines (VMs) on a single physical server's CPU. Virtualization allows applications to be isolated between VMs and provides a level of security as the information of one application cannot be freely accessed by another application.
Virtualization allows better utilization of resources in a physical server and allows better scalability because an application can be added or updated easily, reduces hardware costs, and much more.
 - Containers are a good way to bundle and run your applications. In a production environment, you need to manage the containers that run the applications and ensure that there is no downtime.
 #### Kubernetes provides you 
 - Service discovery and load balancing
 -- Kubernetes can expose a container using the DNS name or using their own IP address. If traffic to a container is high, Kubernetes is able to load balance and distribute the network traffic so that the deployment is stable.
 - Storage orchestration 
 -- Kubernetes allows you to automatically mount a storage system of your choice, such as local storages, public cloud providers, and more.
 - Automated rollouts and rollbacks
 -- You can describe the desired state for your deployed containers using Kubernetes, and it can change the actual state to the desired state at a controlled rate. For example, you can automate Kubernetes to create new containers for your deployment, remove existing containers and adopt all their resources to the new container.
 - Automatic bin packing 
 -- You provide Kubernetes with a cluster of nodes that it can use to run containerized tasks. You tell Kubernetes how much CPU and memory (RAM) each container needs. Kubernetes can fit containers onto your nodes to make the best use of your resources.
 - Self-healing 
 -- Kubernetes restarts containers that fail, replaces containers, kills containers that don’t respond to your user-defined health check, and doesn’t advertise them to clients until they are ready to serve.
 - Secret and configuration management
 -- Kubernetes lets you store and manage sensitive information, such as passwords, OAuth tokens, and SSH keys. You can deploy and update secrets and application configuration without rebuilding your container images, and without exposing secrets in your stack configuration.
 
 ### Kubernetes Control plane
 - A Kubernetes cluster consists of a set of worker machines, called nodes , that run containerized applications. Every cluster has at least one worker node.
 - The worker node(s) host the Pods that are the components of the application workload. The control plane manages the worker nodes and the Pods in the cluster. 
 - Kube API Server: The API server is a component of the Kubernetes control plane that exposes the Kubernetes API. The API server is the front end for the Kubernetes control plane. The main implementation of a Kubernetes API server is kube-apiserver.kube-apiserver is designed to scale horizontally—that is, it scales by deploying more instances. You can run several instances of kube-apiserver and balance traffic between those instances.
 - etcd : Consistent and highly-available key value store used as Kubernetes' backing store for all cluster data.
 - kube-schedular : Control plane component that watches for newly created Pods with no assigned node , and selects a node for them to run on.
 - kube-controller-manager : this controller includes, 
 -- Node controller - Responsible for noticing and responding when nodes go down.
 -- Replication controller: Responsible for maintaining the correct number of pods for every replication controller object in the system.
 -- Endpoints controller: Populates the Endpoints object.
 -- Service Account & Token controllers: Create default accounts and API access tokens for new namespaces
 
 ### Node Component
 - Node components run on every node, maintaining running pods and providing the Kubernetes runtime environment.
 - Kubelet -- An agent that runs on each node in the cluster. It makes sure that containers are running in a Pod .
 - kube-proxy -- kube-proxy is a network proxy that runs on each node in your cluster, implementing part of the Kubernetes Service concept.kube-proxy maintains network rules on nodes. These network rules allow network communication to your Pods from network sessions inside or outside of your cluster. kube-proxy uses the operating system packet filtering layer if there is one and it's available. Otherwise, kube-proxy forwards the traffic itself.
 - Container Runtime -- The container runtime is the software that is responsible for running containers.Kubernetes supports several container runtimes: Docker , containerd , CRI-O , and any implementation of the Kubernetes CRI (Container Runtime Interface)
 - Addons -- Addons use Kubernetes resources (DaemonSet , Deployment , etc) to implement cluster features.
 - DNS -- Cluster DNS is a DNS server, in addition to the other DNS server(s) in your environment, which serves DNS records for Kubernetes services. Containers started by Kubernetes automatically include this DNS server in their DNS searches.
 - Web UI -- Dashboard is a general purpose, web-based UI for Kubernetes clusters. It allows users to manage and troubleshoot applications running in the cluster, as well as the cluster itself.
Cont


## Jenkins

## Linux Scripts

## Python Code

## Linux Administration 

## Networking

## Cloud - AWS/Azure/GCP
- 

## Deployment- CI/CD
