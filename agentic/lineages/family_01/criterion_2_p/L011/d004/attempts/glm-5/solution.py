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
    
    # -1: unvisited, 0: color 0 (x=1), 1: color 1 (x=2)
    color = [-1] * (n + 1)
    
    # We want lexicographically smallest sequence of states.
    # x_i = 1 corresponds to color 0.
    # x_i = 2 corresponds to color 1.
    # Lexicographically smallest means we prefer color 0 over color 1.
    # We iterate nodes from 1 to n. If a node is unvisited, we start a BFS.
    # We try to assign color 0 to the starting node. If this leads to a conflict,
    # we try color 1. If both fail, the graph is not bipartite.
    
    for i in range(1, n + 1):
        if color[i] == -1:
            # Attempt to color component starting with node i having color 0
            # We use a local queue for the BFS attempt
            queue = deque([i])
            color[i] = 0
            success = True
            path = [i]
            
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        queue.append(v)
                        path.append(v)
                    elif color[v] == color[u]:
                        success = False
                        break
                if not success:
                    break
            
            if success:
                continue
            
            # If coloring with 0 failed, reset colors in this component and try 1
            for node_idx in path:
                color[node_idx] = -1
            
            queue = deque([i])
            color[i] = 1
            success = True
            
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        success = False
                        break
                if not success:
                    break
            
            if not success:
                print("NO")
                return

    print("YES")
    # Convert colors to states: color 0 -> 1, color 1 -> 2
    result = []
    for i in range(1, n + 1):
        result.append(str(color[i] + 1))
    print(" ".join(result))

if __name__ == '__main__':
    solve()