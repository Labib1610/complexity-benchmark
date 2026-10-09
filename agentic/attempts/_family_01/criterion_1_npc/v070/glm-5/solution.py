import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    adj = [0] * n
    idx = 2
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx+1]) - 1
        idx += 2
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    # Find connected components
    seen = [False] * n
    components = []
    for i in range(n):
        if not seen[i]:
            comp = []
            stack = [i]
            seen[i] = True
            while stack:
                u = stack.pop()
                comp.append(u)
                for v in range(n):
                    if (adj[u] >> v) & 1 and not seen[v]:
                        seen[v] = True
                        stack.append(v)
            components.append(comp)

    color = [0] * n

    for comp in components:
        size = len(comp)
        if size > 3:
            print("NO")
            return
        # Try all 3^size colorings
        found = False
        for mask in range(3 ** size):
            ok = True
            for j in range(size):
                cj = mask // (3 ** j) % 3
                for k in range(j + 1, size):
                    ck = mask / (3 ** k) % 3
                    if cj == ck and (adj[comp[j]] >> comp[k]) & 1:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                for j in range(size):
                    color[comp[j]] = mask // (3 ** j) % 3 + 1
                found = True
                break
        if not found:
            print("NO")
            return

    print("YES")
    print(" ".join(map(str, color)))

solve()