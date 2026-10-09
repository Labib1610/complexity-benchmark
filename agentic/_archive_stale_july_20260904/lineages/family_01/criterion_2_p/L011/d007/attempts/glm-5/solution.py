import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)

    # We need to find assignment x_i in {1, 2} such that
    # Product over edges (x_u + x_v) = 3^m
    # Since x_u + x_v is in {2, 3, 4}, and 3^m has only prime factor 3,
    # every term (x_u + x_v) must be 3.
    # This implies for every edge (u, v), x_u != x_v.
    # Thus, the graph must be bipartite.
    # We want the lexicographically smallest valid assignment.
    # Since we prefer 1 over 2, we should assign 1 to nodes whenever possible.
    # In a connected component, once one node is assigned, all others are determined.
    # To minimize lexicographically, we should assign 1 to the smallest-indexed node in each component.
    
    color = [-1] * (n + 1)
    possible = True
    
    for i in range(1, n + 1):
        if color[i] == -1:
            # Start BFS from node i, assigning it color 1 (tier 1)
            # This ensures the smallest index in the component gets tier 1.
            queue = deque([i])
            color[i] = 1
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 3 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        possible = False
                        break
                if not possible:
                    break
        if not possible:
            break
            
    if not possible:
        print("NO")
    else:
        print("YES")
        print(*(color[1:]))

if __name__ == '__main__':
    solve()