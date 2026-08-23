import sys
sys.setrecursionlimit(10000)

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if v not in adj[u]:
            adj[u].append(v)
        if u not in adj[v]:
            adj[v].append(u)

    color = [0] * n  # 0 uncolored, 1/2/3 colored

    def dfs(pos):
        if pos == n:
            return True
        v = pos
        for c in (1, 2, 3):
            # check conflict with colored neighbors
            conflict = False
            for u in adj[v]:
                if color[u] == c:
                    conflict = True
                    break
            if conflict:
                continue
            color[v] = c
            # forward checking: ensure all uncolored vertices have at least one available color
            fail = False
            for u in range(n):
                if color[u] == 0:
                    used_mask = 0
                    for w in adj[u]:
                        cw = color[w]
                        if cw:
                            used_mask |= 1 << (cw - 1)
                    if used_mask == 7:   # all 3 colors used
                        fail = True
                        break
            if not fail:
                if dfs(pos + 1):
                    return True
            color[v] = 0
        return False

    if dfs(0):
        print("YES")
        print(' '.join(map(str, color)))
    else:
        print("NO")

if __name__ == "__main__":
    main()