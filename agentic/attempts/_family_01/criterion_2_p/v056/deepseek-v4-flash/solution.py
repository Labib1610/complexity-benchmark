import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    color = [-1] * n
    
    for start in range(n):
        if color[start] != -1:
            continue
        # try to color start with 0 (vault 1) for lexicographically smallest
        color[start] = 0
        q = deque([start])
        ok = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    q.append(v)
                elif color[v] == color[u]:
                    ok = False
                    break
            if not ok:
                break
        if not ok:
            # We can also try opposite coloring for this component
            # reset colors in this component and try inverted
            comp_nodes = []
            # find all nodes in this component
            # Actually simpler: reset colors for this component by BFS again
            # We'll re-color by BFS from start with color 1 instead
            # First, clear previously colored nodes in this component
            # We don't have full list yet, so we'll collect during the failed BFS
            # But easier: we can do a second pass starting with color 1.
            # For that we need to know all nodes in this component before.
            # Let's gather them with a quick BFS/DFS (no coloring yet)
            stack = [start]
            comp = []
            visited = [False]*n
            visited[start] = True
            while stack:
                u = stack.pop()
                comp.append(u)
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
            # Now color with 1-start
            for node in comp:
                color[node] = -1
            color[start] = 1
            q = deque([start])
            ok2 = True
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        q.append(v)
                    elif color[v] == color[u]:
                        ok2 = False
                        break
                if not ok2:
                    break
            if not ok2:
                print("NO")
                return
            # else keep this coloring
    
    # Build result
    res = [1 if c == 0 else 2 for c in color]
    print("YES")
    print(" ".join(map(str, res)))

if __name__ == "__main__":
    solve()