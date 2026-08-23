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

    colors = [0] * n
    possible = [0b111] * n  # bits 0,1,2 for colors 1,2,3

    def dfs(idx):
        if idx == n:
            return True
        v = idx
        allowed = possible[v]
        # try colors 1..3
        for c in (1, 2, 3):
            bit = 1 << (c - 1)
            if allowed & bit:
                colors[v] = c
                changes = []
                ok = True
                for u in adj[v]:
                    if u > v and colors[u] == 0 and (possible[u] & bit):
                        possible[u] ^= bit
                        changes.append((u, bit))
                        if possible[u] == 0:
                            ok = False
                            break
                if ok:
                    if dfs(idx + 1):
                        return True
                # revert changes
                for u, b in changes:
                    possible[u] |= b
                colors[v] = 0
        return False

    if dfs(0):
        out = ['YES', ' '.join(map(str, colors))]
    else:
        out = ['NO']
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    main()