import sys
from collections import defaultdict, deque

def read_input():
    n, m, k = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
    return n, m, k, edges

def build_graph(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph

def bipartite_check(n, graph):
    color = [0] * (n + 1)  # 0: unvisited, 1: red, -1: blue
    partition = {1: [], -1: []}
    
    for start in range(1, n + 1):
        if color[start] == 0:
            queue = deque([start])
            color[start] = 1
            partition[1].append(start)
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                
                for neighbor in graph[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = -current_color
                        partition[-current_color].append(neighbor)
                        queue.append(neighbor)
                    elif color[neighbor] == current_color:
                        return None, None  # Not bipartite
    
    return partition[1], partition[-1]

def solve():
    n, m, k, edges = read_input()
    graph = build_graph(n, edges)
    
    # Check if the graph is bipartite
    set1, set2 = bipartite_check(n, graph)
    
    if set1 is None:  # Graph is not bipartite
        print("NO")
        return
    
    # Try to select k nodes from the larger set
    if len(set1) >= k:
        print("YES")
        print(' '.join(map(str, set1[:k])))
    elif len(set2) >= k:
        print("YES")
        print(' '.join(map(str, set2[:k])))
    elif len(set1) + len(set2) >= k:
        # We need to take some from both sets
        # But this would create an edge between them, which is not allowed
        print("NO")
    else:
        print("NO")

if __name__ == "__main__":
    solve()