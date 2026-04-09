Practice Session: Highly available Kubernetes Server:

kubectl get pods -o custom-columns=POD:metadata.name,NODE:spec.nodeName --sort-by spec.nodeName -n kube-system
POD                                        NODE
kube-apiserver-saggy-k8s-master            saggy-k8s-master
calico-node-qp544                          saggy-k8s-master
kube-proxy-jr4hf                           saggy-k8s-master
coredns-6955765f44-btddp                   saggy-k8s-master
kube-scheduler-saggy-k8s-master            saggy-k8s-master
etcd-saggy-k8s-master                      saggy-k8s-master
kube-controller-manager-saggy-k8s-master   saggy-k8s-master
calico-kube-controllers-6b94766748-8wlt9   saggy-k8s-node1
calico-node-x5bxd                          saggy-k8s-node1
kube-proxy-rz2vr                           saggy-k8s-node1
coredns-6955765f44-ns7dr                   saggy-k8s-node1

Run a simple nginx deployment:

kubectl create deployment nginx --image=nginx

View the deployments in your cluster:

kubectl get deployments

View the pods in the cluster:

kubectl get pods

Use port forwarding to access a pod directly:
kubectl port-forward $pod_name 8081:80
