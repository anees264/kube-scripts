import subprocess
import re
import argparse
from collections import defaultdict

def get_kubectl_output(namespace=None, all_namespaces=False):
    try:
        command = ["kubectl", "top", "pods"]
        if all_namespaces:
            command.append("--all-namespaces")
        elif namespace:
            command.extend(["--namespace", namespace])
        
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running kubectl command: {e.stderr}")
        return None

def calculate_resources(kubectl_output, all_namespaces=False):
    lines = kubectl_output.strip().split("\n")[1:]
    namespace_usage = defaultdict(lambda: {"cpu": 0, "memory": 0})
    total_cpu = 0
    total_memory = 0

    for line in lines:
        parts = re.split(r"\s{2,}", line.strip())
        if len(parts) < (4 if all_namespaces else 3):
            continue

        if all_namespaces:
            namespace = parts[0]
            cpu = parts[2]
            memory = parts[3]
        else:
            namespace = "default"
            cpu = parts[1]
            memory = parts[2]

        if cpu.endswith("m"):
            cpu_millicores = int(cpu[:-1])
        else:
            cpu_millicores = int(cpu) * 1000

        if memory.endswith("Mi"):
            memory_mib = int(memory[:-2])
        elif memory.endswith("Gi"):
            memory_mib = int(memory[:-2]) * 1024
        else:
            memory_mib = 0

        namespace_usage[namespace]["cpu"] += cpu_millicores
        namespace_usage[namespace]["memory"] += memory_mib
        total_cpu += cpu_millicores
        total_memory += memory_mib

    return namespace_usage, total_cpu, total_memory

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--namespace", help="Specify the namespace to fetch pod metrics.")
    group.add_argument("--all-namespaces", action="store_true", help="Fetch metrics from all namespaces.")
    args = parser.parse_args()

    kubectl_output = get_kubectl_output(namespace=args.namespace, all_namespaces=args.all_namespaces)

    if kubectl_output:
        namespace_usage, total_cpu, total_memory = calculate_resources(kubectl_output, all_namespaces=args.all_namespaces)
        print("\nNamespace-wise Resource Usage:")
        for namespace, usage in namespace_usage.items():
            print(f"- {namespace}: CPU={usage['cpu']}m ({usage['cpu'] / 1000:.2f} cores), Memory={usage['memory']}Mi")
        print("\nTotal Resource Usage:")
        print(f"Total CPU: {total_cpu}m ({total_cpu / 1000:.2f} cores)")
        print(f"Total Memory in MiB: {total_memory}Mi")
        print(f"Total Memory in GiB: {total_memory / 1024:.2f}Gi")
    else:
        print("Failed to fetch data from Kubernetes.")
