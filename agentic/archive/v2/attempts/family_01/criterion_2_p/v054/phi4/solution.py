import sys
from collections import defaultdict

def find_partition(n, conflicts):
    # Create adjacency list for conflicts
    graph = defaultdict(list)
    degree = [0] * (n + 1)

    for u, v in conflicts:
        graph[u].append(v)
        graph[v].append(u)
        degree[u] += 1
        degree[v] += 1

    # Initialize slot assignment with default to 1 (Slot 1)
    slots = [1] * (n + 1)

    def dfs(node, current_slot):
        if slots[node] != 0:
            return slots[node] == current_slot
        
        slots[node] = current_slot
        for neighbor in graph[node]:
            if not dfs(neighbor, 3 - current_slot):
                return False
        return True

    # Try to assign each person starting with the smallest index
    for i in range(1, n + 1):
        if slots[i] == 0:  # If slot is unassigned
            if not dfs(i, 1):  # Start assigning from Slot 1
                return "NO"

    # Convert slot assignments to a string result
    result = "YES\n" + ' '.join(map(str, slots[1:n+1]))
    return result

# Read input
input_data = sys.stdin.read().split()
n = int(input_data[0])
m = int(input_data[1])

conflicts = []
index = 2
for _ in range(m):
    u = int(input_data[index])
    v = int(input_data[index + 1])
    conflicts.append((u, v))
    index += 2

# Find the partition and print result
print(find_partition(n, conflicts))