import sys
sys.setrecursionlimit(1 << 20)
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

for i in range(n):
    if color[i] == -1:
        color[i] = 0
        stack = [i]
        while stack:
            u = stack.pop()
            for v in g[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    stack.append(v)
                elif color[v] == color[u]:
                    ok = False
                    break
            if not ok:
                break
    if not ok:
        break

if not ok:
    print("NO")
else:
    # color 0 -> multiplier 1, color 1 -> multiplier 2
    # But we want lexicographically smallest: prefer 1 at earlier indices.
    # We can flip colors in each connected component if it makes earlier index 1.
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            comp = []
            stack = [i]
            visited[i] = True
            while stack:
                u = stack.pop()
                comp.append(u)
                for v in g[u]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
            # If the first node in this component (by index) has color 1,
            # flip the whole component to make it 0 (multiplier 1).
            first = min(comp)
            if color[first] == 1:
                for u in comp:
                    color[u] ^= 1

    ans = [1 if c == 0 else 2 for c in color]
    print("YES")
    print(" ".join(map(str, ans)))