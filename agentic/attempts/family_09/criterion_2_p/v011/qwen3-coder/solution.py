import sys
from collections import defaultdict, deque

def read_input():
    n, m, k = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
    return n, m, k, edges

def bipartite_check(n, edges):
    # Create adjacency list
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Color array: -1 unvisited, 0 and 1 are colors
    color = [-1] * (n + 1)
    
    # Check each component
    for start in range(1, n + 1):
        if color[start] == -1:
            queue = deque([start])
            color[start] = 0
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                
                for neighbor in adj[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - current_color
                        queue.append(neighbor)
                    elif color[neighbor] == current_color:
                        return None, None  # Not bipartite
    
    # Separate into two groups
    group0 = []
    group1 = []
    for i in range(1, n + 1):
        if color[i] == 0:
            group0.append(i)
        else:
            group1.append(i)
    
    return group0, group1

def solve():
    n, m, k, edges = read_input()
    
    if m == 0:
        # No reactions, we can take any k substances
        print("YES")
        print(" ".join(map(str, range(1, k + 1))))
        return
    
    # Check if graph is bipartite and get the two groups
    group0, group1 = bipartite_check(n, edges)
    
    if group0 is None:
        # This shouldn't happen according to problem statement
        print("NO")
        return
    
    # Since no reactions occur within a group, we can take any subset from a group
    if len(group0) >= k:
        print("YES")
        print(" ".join(map(str, group0[:k])))
    elif len(group1) >= k:
        print("YES")
        print(" ".join(map(str, group1[:k])))
    else:
        print("NO")

if __name__ == "__main__":
    solve()