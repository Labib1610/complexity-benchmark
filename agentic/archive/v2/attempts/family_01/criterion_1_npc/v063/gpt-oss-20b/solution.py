import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n + 1)]
    bitmask = [0] * (n + 1)
    edges = set()
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        if u == v:
            continue
        if u > v:
            u, v = v, u
        edges.add((u, v))
        adj[u].append(v)
        adj[v].append(u)
        bitmask[u] |= 1 << (v - 1)
        bitmask[v] |= 1 << (u - 1)

    # Check for K4 clique
    found_k4 = False
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if (i, j) not in edges:
                continue
            for k in range(j + 1, n + 1):
                if (i, k) not in edges or (j, k) not in edges:
                    continue
                for l in range(k + 1, n + 1):
                    if ((i, l) in edges and (j, l) in edges and (k, l) in edges):
                        found_k4 = True
                        break
                if found_k4:
                    break
            if found_k4:
                break
        if found_k4:
            break
    if found_k4:
        print("NO")
        return

    colors = [0] * (n + 1)
    sys.setrecursionlimit(10000)
    def dfs(idx):
        if idx > n:
            return True
        for c in (1, 2, 3):
            ok = True
            for nb in adj[idx]:
                if colors[nb] == c:
                    ok = False
                    break
            if ok:
                colors[idx] = c
                if dfs(idx + 1):
                    return True
                colors[idx] = 0
        return False

    if dfs(1):
        print("YES")
        print(' '.join(str(colors[i]) for i in range(1, n + 1)))
    else:
        print("NO")

if __name__ == "__main__":
    main()