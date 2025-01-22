# Kubectl Commands Cheat Sheet

## General Commands

```bash
# View kubectl version
kubectl version --client

# View cluster information
kubectl cluster-info

# Get help for any kubectl command
kubectl <command> --help

# List all available API resources
kubectl api-resources

# Get details about API versions and resources
kubectl api-versions
```

---

## Context and Configuration

```bash
# List contexts
kubectl config get-contexts

# Switch context
kubectl config use-context <context-name>

# View current context
kubectl config current-context

# Set a cluster, user, and namespace for a context
kubectl config set-context <context-name> \
  --cluster=<cluster-name> --user=<user-name> --namespace=<namespace>

# View kubeconfig file
kubectl config view
```

---

## Working with Namespaces

```bash
# List all namespaces
kubectl get namespaces

# Create a new namespace
kubectl create namespace <namespace-name>

# Switch to a specific namespace (default for commands)
kubectl config set-context --current --namespace=<namespace-name>

# Delete a namespace
kubectl delete namespace <namespace-name>
```

---

## Managing Pods

```bash
# List all pods in the current namespace
kubectl get pods

# List pods across all namespaces
kubectl get pods --all-namespaces

# Get detailed information about a pod
kubectl describe pod <pod-name>

# Stream logs from a pod
kubectl logs <pod-name>

# Stream logs from a specific container in a pod
kubectl logs <pod-name> -c <container-name>

# Execute a command inside a pod
kubectl exec -it <pod-name> -- <command>

# Delete a pod
kubectl delete pod <pod-name>

# Create a pod from a YAML file
kubectl apply -f <file.yaml>
```

---

## Managing Deployments

```bash
# List all deployments
kubectl get deployments

# Get detailed information about a deployment
kubectl describe deployment <deployment-name>

# Scale a deployment
kubectl scale deployment <deployment-name> --replicas=<number>

# Apply changes to a deployment using a YAML file
kubectl apply -f <file.yaml>

# Rollout an update for a deployment
kubectl rollout restart deployment <deployment-name>

# Check rollout status
kubectl rollout status deployment <deployment-name>

# Rollback a deployment to the previous version
kubectl rollout undo deployment <deployment-name>

# Delete a deployment
kubectl delete deployment <deployment-name>
```

---

## Services and Endpoints

```bash
# List all services in the current namespace
kubectl get services

# Get detailed information about a service
kubectl describe service <service-name>

# Expose a deployment as a service
kubectl expose deployment <deployment-name> --type=<type> --port=<port>

# Delete a service
kubectl delete service <service-name>
```

---

## ConfigMaps and Secrets

```bash
# List all ConfigMaps
kubectl get configmaps

# Create a ConfigMap from a file
kubectl create configmap <name> --from-file=<file-path>

# Create a ConfigMap from key-value pairs
kubectl create configmap <name> --from-literal=<key>=<value>

# Get detailed information about a ConfigMap
kubectl describe configmap <name>

# Delete a ConfigMap
kubectl delete configmap <name>

# List all Secrets
kubectl get secrets

# Create a Secret from key-value pairs
kubectl create secret generic <name> --from-literal=<key>=<value>

# Get detailed information about a Secret
kubectl describe secret <name>

# Delete a Secret
kubectl delete secret <name>
```

---

## Working with Nodes

```bash
# List all nodes
kubectl get nodes

# Get detailed information about a node
kubectl describe node <node-name>

# Cordon a node (mark as unschedulable)
kubectl cordon <node-name>

# Uncordon a node (mark as schedulable)
kubectl uncordon <node-name>

# Drain a node (safely evict pods from a node)
kubectl drain <node-name> --ignore-daemonsets

# Delete a node
kubectl delete node <node-name>
```

---

## Persistent Volumes and Claims

```bash
# List all PersistentVolumes (PVs)
kubectl get pv

# Get detailed information about a PV
kubectl describe pv <pv-name>

# List all PersistentVolumeClaims (PVCs)
kubectl get pvc

# Get detailed information about a PVC
kubectl describe pvc <pvc-name>

# Delete a PVC
kubectl delete pvc <pvc-name>
```

---

## Events and Debugging

```bash
# List all events in the current namespace
kubectl get events

# Describe a specific resource
kubectl describe <resource-type> <resource-name>

# Debug a running pod
kubectl debug pod/<pod-name> --image=<debug-image>
```

---

## Customizing Output

```bash
# Show output in a wide format
kubectl get pods -o wide

# Show output as YAML
kubectl get pods <pod-name> -o yaml

# Show output as JSON
kubectl get pods <pod-name> -o json

# Watch resources and automatically update output
kubectl get pods --watch

# Save output to a file
kubectl get pods -o yaml > pods.yaml
```

---

## Resource Management

```bash
# Apply a configuration file
kubectl apply -f <file.yaml>

# Delete resources using a configuration file
kubectl delete -f <file.yaml>

# Dry-run a command without applying changes
kubectl apply -f <file.yaml> --dry-run=client

# Force delete a resource
kubectl delete pod <pod-name> --grace-period=0 --force

# Edit a resource interactively
kubectl edit <resource-type> <resource-name>
```

---

## Other Useful Commands

```bash
# Run a pod with an image
kubectl run <pod-name> --image=<image-name>

# Port-forward a pod to localhost
kubectl port-forward pod/<pod-name> <local-port>:<pod-port>

# Copy files to/from a pod
kubectl cp <local-path> <pod-name>:<container-path>
kubectl cp <pod-name>:<container-path> <local-path>
```

