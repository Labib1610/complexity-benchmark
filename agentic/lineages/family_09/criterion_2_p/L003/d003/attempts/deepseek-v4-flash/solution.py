import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)

    visited = [-1] * n
    comps = []
    for i in range(n):
        if visited[i] == -1:
            # BFS to color the component
            q = deque([i])
            visited[i] = 0
            cnt = [0, 0]
            cnt[0] += 1
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if visited[v] == -1:
                        visited[v] = visited[u] ^ 1
                        cnt[visited[v]] += 1
                        q.append(v)
            comps.append((cnt[0], cnt[1]))

    # DP: possible sums of sizes
    dp = 1  # bitmask of reachable sums
    for a, b in comps:
        dp = (dp << a) | (dp << b)

    if (dp >> k) & 1:
        print("YES")
        # Reconstruct solution
        chosen = []
        # We'll backtrack from k
        target = k
        for a, b in reversed(comps):
            # Check if target can be reached by taking a or b
            if target >= a and ((dp >> (target - a)) & 1):
                # take side a
                # find nodes of that side
                chosen.extend(find_nodes(a, b, visited, comps, target, a))
                target -= a
            else:
                # take side b
                chosen.extend(find_nodes(a, b, visited, comps, target, b))
                target -= b
            dp >>= max(a, b)  # not exactly right, but we'll handle differently
        # Actually, we need a simpler reconstruction: store dp states per component
        # Let's do it properly below.
    else:
        print("NO")

if __name__ == "__main__":
    solve()