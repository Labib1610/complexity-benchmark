import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * n
    # Try to assign color 1 if possible, else 0 (meaning band 2)
    # We store colors as 0 or 1 but output as 1 or 2.
    for start in range(n):
        if color[start] != -1:
            continue
        # BFS/DFS with preference for color 0 (band 1)
        stack = [start]
        color[start] = 0
        while stack:
            u = stack.pop()
            for v in adj[u]:
                if color[v] == -1:
                    # prefer to give v color 0 if possible (no conflict)
                    # But constrained: must differ from u.
                    # If u=0, v=1; if u=1, v=0. No choice for uncolored.
                    color[v] = 1 - color[u]
                    stack.append(v)
                elif color[v] == color[u]:
                    print("NO")
                    return
    # Already colored bipartitely. Now try to flip some nodes to get lexicographically smallest.
    # But flipping a node affects its neighbors, so we need to ensure consistency.
    # Standard approach: For each connected component, we decide its 0/1 assignment
    # by trying to make node with smallest index in component be 0 if possible.
    # Since we already have a 2-coloring, we can consider both parities for each component.
    # Actually the above BFS already found a valid coloring. To get lexicographically smallest,
    # we should attempt at each node (in order) to set it to 0 if possible, ignoring already fixed.
    # However, the initial coloring from BFS may not be minimal. We can recompute differently.

    # Better: Do BFS but at each step try 0 first and propagate.
    color = [-1] * n
    for start in range(n):
        if color[start] != -1:
            continue
        # Try start=0, but if that leads to contradiction, then start must be 1.
        stack = [(start, 0)]
        color[start] = 0
        ok = True
        temp_stack = [(start, 0)]
        while temp_stack:
            u, c = temp_stack.pop()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - c
                    temp_stack.append((v, 1-c))
                elif color[v] != 1 - c:
                    ok = False
                    break
            if not ok:
                break
        if not ok:
            # Reset component
            comp = []
            stack2 = [(start, 0)]
            comp.append(start)
            color[start] = -1
            while stack2:
                u, _ = stack2.pop()
                for v in adj[u]:
                    if color[v] != -1:
                        color[v] = -1
                        comp.append(v)
                        stack2.append((v, 0))
            # Now assign start=1
            stack3 = [(start, 1)]
            color[start] = 1
            while stack3:
                u, c = stack3.pop()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - c
                        stack3.append((v, 1-c))
                    elif color[v] != 1 - c:
                        print("NO")
                        return

    print("YES")
    print(' '.join(str(c+1) for c in color))

if __name__ == "__main__":
    solve()