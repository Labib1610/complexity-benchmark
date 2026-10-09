import sys
from collections import defaultdict, deque

def read_input():
    n, m, k = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
    return n, m, k, edges

def solve(n, m, k, edges):
    # Build adjacency list
    adj = defaultdict(set)
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    
    # Try to partition into two sets (bipartite check)
    color = {}
    visited = set()
    
    def bfs(start):
        queue = deque([start])
        color[start] = 0
        set0 = [start]
        set1 = []
        
        while queue:
            node = queue.popleft()
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor not in color:
                    color[neighbor] = 1 - color[node]
                    if color[neighbor] == 0:
                        set0.append(neighbor)
                    else:
                        set1.append(neighbor)
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False, [], []  # Not bipartite
        return True, set0, set1
    
    set0_all = []
    set1_all = []
    
    for i in range(1, n+1):
        if i not in visited:
            is_bipartite, set0, set1 = bfs(i)
            if not is_bipartite:
                return "NO"
            set0_all.extend(set0)
            set1_all.extend(set1)
    
    # Check if we can form a group of size k
    if len(set0_all) >= k:
        return "YES\n" + " ".join(map(str, set0_all[:k]))
    elif len(set1_all) >= k:
        return "YES\n" + " ".join(map(str, set1_all[:k]))
    else:
        return "NO"

def main():
    n, m, k, edges = read_input()
    result = solve(n, m, k, edges)
    print(result)

if __name__ == "__main__":
    main()