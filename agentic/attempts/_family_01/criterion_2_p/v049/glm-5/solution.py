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
    
    # To get lexicographically smallest sequence, we want to assign shift 1 to smaller indices
    # whenever possible. We process nodes in increasing order of index.
    # If a node is unassigned, we tentatively assign it to shift 1.
    # We then perform BFS/DFS to propagate constraints.
    # If a conflict is found (neighbor has same shift), we backtrack and try shift 2.
    # If shift 2 also fails, the graph is not bipartite.
    
    color = [0] * (n + 1) # 0: uncolored, 1: shift 1, 2: shift 2
    
    for i in range(1, n + 1):
        if color[i] == 0:
            # Try assigning shift 1 to node i
            # We use a queue for BFS
            queue = deque([i])
            color[i] = 1
            path = [i] # Track nodes colored in this component for backtracking
            possible = True
            
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        queue.append(v)
                        path.append(v)
                    elif color[v] == color[u]:
                        possible = False
                        # Don't break immediately, need to clear queue to finish processing or just break
                        # since we will backtrack anyway.
                        break
                if not possible:
                    break
            
            if possible:
                continue
            
            # Backtrack: reset colors of nodes in this component
            for node in path:
                color[node] = 0
            
            # Try assigning shift 2 to node i
            queue = deque([i])
            color[i] = 2
            path = [i]
            possible = True
            
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        queue.append(v)
                        path.append(v)
                    elif color[v] == color[u]:
                        possible = False
                        break
                if not possible:
                    break
            
            if not possible:
                # Both assignments fail
                sys.stdout.write("NO\n")
                return
    
    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, color[1:])) + "\n")

if __name__ == '__main__':
    solve()