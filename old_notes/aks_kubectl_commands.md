Kubernetes Documentation:  https://kubernetes.io/docs/concepts/

1. AZ Login

az login
az account set --subscription "SUB_NAME"
                                                            
2. ACR Login            
az acr login --name <acrName>

az acr list --resource-group <myResourceGroup> --query "[].{acrLoginServer:loginServer}" --output table acrName - dfeacr.azurecr.io

3. Docker Build & Push

docker build -t <loginServerName>/<appName>:<tag> .
docker push <LoginServerName>/<appName>:<tag>

5. Install kubectl

az aks install-cli
az aks get-credentials --resource-group <myResourceGroup> --name <myAKSCluster>
To verify the connection to your cluster, run the kubectl get nodes command.                             
kubectl get nodes
                                                            
6 Launch Kubernetes Dashboard
az aks browse --resource-group RG  --name AKS-NAME

7. You can list the current namespaces in a cluster using:
kubectl get namespaces

Kubernetes starts with three initial namespaces:
default - The default namespace for objects with no other namespace
kube-system - The namespace for objects created by the Kubernetes system
kube-public - This namespace is created automatically and is readable by all users (including those not authenticated). This namespace is mostly reserved for cluster usage, in case that some resources should be visible and readable publicly throughout the whole cluster.

8. You can list the current pods in a cluster using:
kubectl --namespace=<insert-namespace-name-here> get pods

9. Namespace and DNS:
When you create a Service, it creates a corresponding DNS entry. This entry is of the form <service-name>.<namespace-name>.svc.cluster.local, which means that if a container just uses <service-name>, it will resolve to the service which is local to a namespace.

10. Kubernets Object 
Kubernetes Objects are persistent entities in the Kubernetes system. Kubernetes uses these entities to represent the state of your cluster. Specifically, they can describe:

What containerized applications are running (and on which nodes)
The resources available to those applications
The policies around how those applications behave, such as restart policies, upgrades, and fault-tolerance

When you create an object in Kubernetes, you must provide the object spec that describes its desired state, as well as some basic information about the object (such as a name).

In the .yaml file for the Kubernetes object you want to create, you’ll need to set values for the following fields:

apiVersion - Which version of the Kubernetes API you’re using to create this object
kind - What kind of object you want to create
metadata - Data that helps uniquely identify the object, including a name string, UID, and optional namespace
