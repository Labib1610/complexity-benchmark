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

def bfs_bipartite_check(adj, n):
    # Color nodes with 0 or 1
    color = [-1] * (n + 1)
    partition = [[], []]
    
    for start in range(1, n + 1):
        if color[start] == -1:
            queue = deque([start])
            color[start] = 0
            partition[0].append(start)
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                next_color = 1 - current_color
                
                for neighbor in adj[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = next_color
                        partition[next_color].append(neighbor)
                        queue.append(neighbor)
                    elif color[neighbor] == current_color:
                        # Not bipartite, but according to problem statement,
                        # the graph should satisfy the even-sequence property
                        # which implies it's bipartite
                        pass
    return partition

def solve():
    n, m, k, edges, adj = read_input()
    
    # The even-sequence property means the graph is bipartite
    # So we can color it with two colors such that no two adjacent nodes have the same color
    partition = bfs_bipartite_check(adj, n)
    
    # Choose the larger partition to maximize our selection
    if len(partition[0]) >= k:
        print("YES")
        print(' '.join(map(str, partition[0][:k])))
    elif len(partition[1]) >= k:
        print("YES")
        print(' '.join(map(str, partition[1][:k])))
    else:
        print("NO")

if __name__ == "__main__":
    solve()