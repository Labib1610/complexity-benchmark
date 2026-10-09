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

    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        adj[u].append(v)
        adj[v].append(u)

    # We need to assign capacities 1 or 2.
    # For each edge (u, v), the number of subgrids must be 3.
    # Number of subgrids in a c_u x c_v grid is T(c_u) * T(c_v), where T(k) = k*(k+1)/2.
    # T(1) = 1, T(2) = 3.
    # Possible products: 1*1=1, 1*3=3, 3*1=3, 3*3=9.
    # We need the product to be 3.
    # This implies one endpoint must have capacity 1 and the other capacity 2.
    # Thus, the graph must be bipartite.
    # We find a bipartition. If the graph is not bipartite, answer is NO.
    # If bipartite, we have two sets S1 and S2.
    # We can assign (c=1 to S1, c=2 to S2) or (c=2 to S1, c=1 to S2).
    # To get the lexicographically smallest assignment, we should assign 1 to the
    # set containing the smallest index node (node 0).
    # If node 0 is isolated, we assign it 1 (lexicographically smallest).

    color = [-1] * n
    is_bipartite = True
    
    # We use BFS to check bipartiteness and color the graph.
    # Since the graph might be disconnected, we iterate all components.
    # We start BFS from node 0 to fix its color to 0 (which we will map to capacity 1).
    
    queue = deque()
    
    # Handle node 0 specifically to ensure it gets color 0 (capacity 1)
    # if it's part of any edge.
    if n > 0:
        color[0] = 0
        queue.append(0)
    
    # Process the connected component containing node 0
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if color[v] == -1:
                color[v] = 1 - color[u]
                queue.append(v)
            elif color[v] == color[u]:
                is_bipartite = False
                break
        if not is_bipartite:
            break

    # Process remaining components (if any and if still bipartite)
    if is_bipartite:
        for i in range(n):
            if color[i] == -1:
                # Unvisited node in a different component.
                # It can be assigned arbitrarily, but 0 is preferred for lex min.
                color[i] = 0
                queue.append(i)
                while queue:
                    u = queue.popleft()
                    for v in adj[u]:
                        if color[v] == -1:
                            color[v] = 1 - color[u]
                            queue.append(v)
                        elif color[v] == color[u]:
                            is_bipartite = False
                            break
                    if not is_bipartite:
                        break
            if not is_bipartite:
                break

    if not is_bipartite:
        sys.stdout.write("NO\n")
    else:
        sys.stdout.write("YES\n")
        # Map color 0 -> capacity 1, color 1 -> capacity 2
        capacities = [1 if c == 0 else 2 for c in color]
        sys.stdout.write(" ".join(map(str, capacities)) + "\n")

if __name__ == '__main__':
    solve()