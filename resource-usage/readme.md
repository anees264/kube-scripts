## CPU and Memory Usage

Run the script `cpu-mem-usage.py` to get the total CPU and memory usage of the pods in the cluster.

#### Get the total CPU and memory usage of the pods in the cluster.

```bash
python3 cpu-mem-usage.py --all-namespaces
```

#### Get the total CPU and memory usage of the pods in the namespace.

```bash
python3 cpu-mem-usage.py --namespace <namespace>
```
