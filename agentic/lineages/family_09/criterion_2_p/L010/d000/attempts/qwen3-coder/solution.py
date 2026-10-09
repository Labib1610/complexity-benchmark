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

def bipartite_partition(n, graph):
    color = {}
    for start in range(1, n + 1):
        if start not in color:
            queue = deque([start])
            color[start] = 0
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in color:
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        # This should not happen according to the problem statement
                        return None, None
    # Separate nodes by their color
    set0 = [node for node in color if color[node] == 0]
    set1 = [node for node in color if color[node] == 1]
    return set0, set1

def main():
    n, m, k, edges = read_input()
    graph = build_graph(n, edges)
    
    # If there are no edges, any k nodes will do
    if m == 0:
        print("YES")
        print(' '.join(map(str, range(1, min(k + 1, n + 1)))))
        return
    
    # Partition the graph into two sets based on the bipartite structure
    set0, set1 = bipartite_partition(n, graph)
    
    # Check which set can provide enough nodes for the all-strangers group
    if len(set0) >= k:
        print("YES")
        print(' '.join(map(str, set0[:k])))
    elif len(set1) >= k:
        print("YES")
        print(' '.join(map(str, set1[:k])))
    else:
        print("NO")

if __name__ == "__main__":
    main()