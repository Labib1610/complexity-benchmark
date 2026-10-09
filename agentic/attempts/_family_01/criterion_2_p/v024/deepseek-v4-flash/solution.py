import sys
sys.setrecursionlimit(1 << 25)

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

    # BFS to check bipartiteness and assign colors
    from collections import deque
    for i in range(n):
        if color[i] != -1:
            continue
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

    # Now we have a valid 2-coloring, but we need lexicographically smallest.
    # We can try to flip colors in each connected component to make the
    # smallest index in that component be 1 (color 0 -> window 1).
    # Since each component is independent, we can choose orientation.

    # Build component info
    comp = [-1] * n
    comp_id = 0
    for i in range(n):
        if comp[i] != -1:
            continue
        # BFS to mark component
        comp[i] = comp_id
        q = deque([i])
        while q:
            u = q.popleft()
            for v in g[u]:
                if comp[v] == -1:
                    comp[v] = comp_id
                    q.append(v)
        comp_id += 1

    # For each component, decide orientation: if color[first] == 1, flip all
    # in that component so that first becomes 0 (window 1).
    for c in range(comp_id):
        # find first node in this component
        first = None
        for i in range(n):
            if comp[i] == c:
                first = i
                break
        if color[first] == 1:
            # flip all in this component
            for i in range(n):
                if comp[i] == c:
                    color[i] ^= 1

    # Now color 0 -> window 1, color 1 -> window 2
    ans = [1 if color[i] == 0 else 2 for i in range(n)]
    print("YES")
    print(" ".join(map(str, ans)))

if __name__ == "__main__":
    solve()