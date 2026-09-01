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

    # We need to assign values 1 or 2 to each node.
    # Constraint: for every edge (u, v), val[u] != val[v].
    # This is a bipartite graph check.
    # To find the lexicographically smallest assignment, we process nodes
    # in increasing order of index. If a node is unassigned, we assign it 1
    # and propagate the constraints (neighbors must be 2).
    
    color = [0] * (n + 1)
    possible = True
    
    for i in range(1, n + 1):
        if color[i] == 0:
            # Start BFS for this component
            queue = deque([i])
            color[i] = 1
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if color[v] == 0:
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
        sys.stdout.write("NO\n")
    else:
        sys.stdout.write("YES\n")
        sys.stdout.write(" ".join(map(str, color[1:])) + "\n")

if __name__ == '__main__':
    solve()