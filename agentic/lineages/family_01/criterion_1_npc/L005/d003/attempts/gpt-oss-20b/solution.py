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
        adj[u].append(v)
        adj[v].append(u)

    avail = [0b111] * n  # bits 0,1,2 correspond to colors 1,2,3
    color = [0] * n
    found = False

    def dfs(idx):
        nonlocal found
        if idx == n:
            found = True
            return True
        i = idx
        for c in (1, 2, 3):
            bit = 1 << (c - 1)
            if not (avail[i] & bit):
                continue
            color[i] = c
            updated = []
            fail = False
            for j in adj[i]:
                if color[j] == 0:
                    old = avail[j]
                    avail[j] &= ~bit
                    if avail[j] == 0:
                        fail = True
                        break
                    updated.append((j, old))
            if not fail:
                if dfs(idx + 1):
                    return True
            # revert changes
            for j, old in updated:
                avail[j] = old
            color[i] = 0
        return False

    if dfs(0):
        print("YES")
        print(' '.join(str(c) for c in color))
    else:
        print("NO")

if __name__ == "__main__":
    main()