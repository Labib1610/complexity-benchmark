import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)

    color = [-1] * n
    ok = True

    # BFS to check bipartiteness and assign initial colors
    from collections import deque
    for i in range(n):
        if color[i] == -1:
            color[i] = 0
            q = deque([i])
            while q:
                u = q.popleft()
                for v in g[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        q.append(v)
                    elif color[v] == color[u]:
                        ok = False
                        break
                if not ok:
                    break
        if not ok:
            break

    if not ok:
        print("NO")
        return

    # Now we have a valid 2-coloring (0/1). We want lexicographically smallest
    # with values 1 and 2. We can flip entire components if it helps lexicographic order.
    # Strategy: For each component, if the first node in that component has color 1 (meaning 2 in output),
    # we flip the whole component so that the smallest index gets 1.

    comp_id = [-1] * n
    comps = []
    comp_nodes = []
    cid = 0
    for i in range(n):
        if comp_id[i] == -1:
            stack = [i]
            comp_id[i] = cid
            nodes = []
            while stack:
                u = stack.pop()
                nodes.append(u)
                for v in g[u]:
                    if comp_id[v] == -1:
                        comp_id[v] = cid
                        stack.append(v)
            comps.append(nodes)
            cid += 1

    # For each component, decide orientation
    for nodes in comps:
        # Find smallest index in component
        min_idx = min(nodes)
        # If color[min_idx] == 1, flip all colors in this component
        if color[min_idx] == 1:
            for u in nodes:
                color[u] ^= 1

    # Output
    print("YES")
    print(' '.join(str(color[i] + 1) for i in range(n)))

if __name__ == "__main__":
    solve()