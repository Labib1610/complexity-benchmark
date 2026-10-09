import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    B = int(data[idx])
    idx += 1
    
    edges = []
    adj = defaultdict(list)
    degree = [0] * (n + 1)
    
    for _ in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
        degree[u] += 1
        degree[v] += 1
    
    # Check if the graph is a tree
    if m != n - 1:
        print("NO")
        return
    
    # Find leaves (degree 1 nodes)
    leaves = deque()
    for i in range(1, n + 1):
        if degree[i] == 1:
            leaves.append(i)
    
    # BFS to get a linear arrangement
    visited = [False] * (n + 1)
    order = []
    
    while leaves:
        node = leaves.popleft()
        if visited[node]:
            continue
        visited[node] = True
        order.append(node)
        for neighbor in adj[node]:
            if not visited[neighbor]:
                degree[neighbor] -= 1
                if degree[neighbor] == 1:
                    leaves.append(neighbor)
    
    # Reverse to get the correct order (leaf to leaf path)
    order.reverse()
    
    # Assign positions optimally along the line
    position = [0] * (n + 1)
    for i in range(n):
        position[order[i]] = i + 1
    
    # Calculate total wire length
    total_length = 0
    for u, v in edges:
        total_length += abs(position[u] - position[v])
    
    if total_length <= B:
        print("YES")
        print(' '.join(map(str, position[1:])))
    else:
        print("NO")

if __name__ == "__main__":
    main()