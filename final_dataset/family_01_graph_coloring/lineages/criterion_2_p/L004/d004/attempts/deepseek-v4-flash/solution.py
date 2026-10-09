import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))

    color = [-1] * n
    comps = []

    for i in range(n):
        if color[i] == -1:
            stack = [i]
            color[i] = 0
            comp = []
            ok = True
            while stack:
                u = stack.pop()
                comp.append(u)
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        stack.append(v)
                    elif color[v] == color[u]:
                        ok = False
            if not ok:
                print("NO")
                return
            comps.append(comp)

    s = [0] * n
    for comp in comps:
        # split into two sides
        side0 = [u for u in comp if color[u] == 0]
        side1 = [u for u in comp if color[u] == 1]
        # choose side with smaller minimum index to be emitters (s=1)
        if min(side0) < min(side1):
            for u in side0:
                s[u] = 1
            for u in side1:
                s[u] = 2
        else:
            for u in side1:
                s[u] = 1
            for u in side0:
                s[u] = 2

    print("YES")
    print(" ".join(map(str, s)))

if __name__ == "__main__":
    solve()