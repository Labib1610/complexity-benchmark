import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx]); v = int(input_data[idx+1])
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * (n + 1)
    possible = True
    
    for i in range(1, n + 1):
        if color[i] == 0:
            color[i] = 1
            q = deque([i])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        q.append(v)
                    elif color[v] == color[u]:
                        possible = False
                        break
                if not possible:
                    break
        if not possible:
            break
    
    if not possible:
        sys.stdout.write("NO\n")
        return
    
    # Lexicographically smallest: try to assign 1 to each vertex if possible
    # We need to check if flipping the component of a vertex (when color is 2) can make it 1
    # without causing conflicts with already fixed vertices.
    # Since the graph may be disconnected, we process components.
    # For lexicographically smallest, we want s_i = 1 if possible.
    # If color[i] is already 1, keep it.
    # If color[i] is 2, we can flip the entire component to make it 1, but only if
    # no vertex in the component is already fixed to a value that would conflict.
    # However, since we process left to right and fix assignments, we need to be careful.
    
    # Actually, for bipartite graphs, each connected component has exactly 2 valid colorings.
    # To get lexicographically smallest, we can greedily assign:
    # For each vertex from 1 to n, if not yet assigned, assign it 1, then BFS to assign
    # the rest of the component. If a conflict arises, it means the graph is not bipartite,
    # but we already checked that. However, we might have already assigned some vertices
    # in the component from previous steps? No, because we process components fully.
    # Wait, the issue is: if we assign vertex i to 1, but it's connected to an already
    # assigned vertex with color 1, then we must assign it 2. But since we process left
    # to right and assign greedily, we need to ensure we don't violate constraints.
    
    # Let's re-do the coloring with greedy lexicographically smallest approach:
    color = [0] * (n + 1)
    possible = True
    for i in range(1, n + 1):
        if color[i] == 0:
            # Try to assign 1 to i
            color[i] = 1
            q = deque([i])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        q.append(v)
                    elif color[v] == color[u]:
                        possible = False
                        break
                if not possible:
                    break
        if not possible:
            break
    
    if not possible:
        sys.stdout.write("NO\n")
        return
    
    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(str(color[i]) for i in range(1, n + 1)) + "\n")

solve()