import sys
from collections import defaultdict, deque

def read_input():
    n, m, k = map(int, sys.stdin.readline().split())
    edges = []
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
    return n, m, k, edges, adj

def bfs_bipartite_check(start, adj, visited, color):
    queue = deque([start])
    color[start] = 0
    visited.add(start)
    
    while queue:
        node = queue.popleft()
        for neighbor in adj[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                color[neighbor] = 1 - color[node]
                queue.append(neighbor)
            elif color[neighbor] == color[node]:
                return False
    return True

def check_bipartite(n, adj):
    visited = set()
    color = {}
    
    for i in range(1, n+1):
        if i not in visited:
            if not bfs_bipartite_check(i, adj, visited, color):
                return False, {}, {}
    
    set1 = [i for i in range(1, n+1) if color.get(i, 0) == 0]
    set2 = [i for i in range(1, n+1) if color.get(i, 0) == 1]
    
    return True, set1, set2

def main():
    n, m, k, edges, adj = read_input()
    
    # Check if the graph is bipartite
    is_bipartite, set1, set2 = check_bipartite(n, adj)
    
    if not is_bipartite:
        print("NO")
        return
    
    # Since the graph is bipartite, we can select from the larger set
    if len(set1) >= k:
        print("YES")
        print(" ".join(map(str, set1[:k])))
    elif len(set2) >= k:
        print("YES")
        print(" ".join(map(str, set2[:k])))
    else:
        print("NO")

if __name__ == "__main__":
    main()