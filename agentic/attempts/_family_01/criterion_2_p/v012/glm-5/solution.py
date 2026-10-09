import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    # color: 0=unassigned, 1=period 1, 2=period 2
    color = [0] * (n + 1)
    
    possible = True

    for i in range(1, n + 1):
        if color[i] == 0:
            # Start BFS for this component
            # We want the lexicographically smallest assignment.
            # This means we want to minimize the sequence of colors.
            # The optimal strategy for a component is to assign the starting node
            # to period 1 (color 1). This minimizes the color of the first node
            # in the component, and consequently minimizes colors of all nodes
            # reachable from it (since neighbors must be 2, their neighbors 1, etc.).
            # This yields the lexicographically smallest valid assignment for the component.
            start_node = i
            color[start_node] = 1
            q = deque([start_node])
            
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

    output = []
    if not possible:
        output.append("NO")
    else:
        output.append("YES")
        # color[i] is 1 or 2. Just join them.
        output.append(" ".join(map(str, color[1:])))

    sys.stdout.write("\n".join(output))

if __name__ == '__main__':
    solve()