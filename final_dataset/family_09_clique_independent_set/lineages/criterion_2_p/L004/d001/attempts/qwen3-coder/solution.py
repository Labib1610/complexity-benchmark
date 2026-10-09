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

def bfs_coloring(graph, n):
    color = [-1] * (n + 1)  # -1: unvisited, 0: black, 1: white
    for i in range(1, n + 1):
        if color[i] == -1:
            queue = deque([i])
            color[i] = 0
            while queue:
                node = queue.popleft()
                current_color = color[node]
                next_color = 1 - current_color
                for neighbor in graph[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = next_color
                        queue.append(neighbor)
                    elif color[neighbor] == current_color:
                        return None  # Not bipartite
    return color

def main():
    n, m, k, edges = read_input()
    graph = build_graph(n, edges)
    
    if m == 0:
        # No conflicts, we can pick any k microservices
        print("YES")
        print(' '.join(map(str, range(1, min(k+1, n+1)))))
        return
    
    coloring = bfs_coloring(graph, n)
    if coloring is None:
        # This shouldn't happen according to problem statement, but just in case
        print("NO")
        return
    
    # Separate nodes into two camps based on coloring
    camp0 = [i for i in range(1, n+1) if coloring[i] == 0]
    camp1 = [i for i in range(1, n+1) if coloring[i] == 1]
    
    # Check if we can form a batch of size k from either camp
    if len(camp0) >= k:
        print("YES")
        print(' '.join(map(str, camp0[:k])))
    elif len(camp1) >= k:
        print("YES")
        print(' '.join(map(str, camp1[:k])))
    else:
        print("NO")

if __name__ == "__main__":
    main()