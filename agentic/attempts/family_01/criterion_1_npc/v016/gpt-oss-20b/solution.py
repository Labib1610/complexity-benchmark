import sys

def main():
    sys.setrecursionlimit(1000000)
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
        adj[u].append(v)
        adj[v].append(u)

    color = [0] * n  # 0 means uncolored

    def dfs(pos):
        if pos == n:
            return True
        for c in (1, 2, 3):
            conflict = False
            for nb in adj[pos]:
                if color[nb] == c:
                    conflict = True
                    break
            if conflict:
                continue
            color[pos] = c
            # forward checking: ensure each uncolored node has at least one available color
            fail = False
            for j in range(n):
                if color[j] == 0:
                    used = 0
                    for nb in adj[j]:
                        if color[nb] != 0:
                            used |= 1 << (color[nb] - 1)
                    if used == 0b111:
                        fail = True
                        break
            if not fail:
                if dfs(pos + 1):
                    return True
            color[pos] = 0
        return False

    if dfs(0):
        print("YES")
        print(' '.join(str(c) for c in color))
    else:
        print("NO")

if __name__ == "__main__":
    main()