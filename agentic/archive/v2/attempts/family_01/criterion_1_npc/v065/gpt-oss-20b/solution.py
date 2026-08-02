import sys

def main():
    sys.setrecursionlimit(10000)
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [set() for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u == v:
            continue
        adj[u].add(v)
        adj[v].add(u)
    # Convert sets to lists for iteration
    adj = [list(s) for s in adj]

    allowed = [7] * (n + 1)  # 3 bits: 0b111
    ans = [0] * (n + 1)      # store colors 1..3, 0 means unassigned

    def dfs(i: int) -> bool:
        if i > n:
            return True
        u = i
        for col in range(3):  # 0,1,2 corresponding to colors 1,2,3
            mask = 1 << col
            if not (allowed[u] & mask):
                continue
            # conflict with already assigned neighbors
            conflict = False
            for v in adj[u]:
                if v < i and ans[v] == col + 1:
                    conflict = True
                    break
            if conflict:
                continue
            # assign color
            ans[u] = col + 1
            changes = []
            ok = True
            for v in adj[u]:
                if v > i:
                    prev = allowed[v]
                    if prev & mask:
                        allowed[v] = prev & ~mask
                        changes.append((v, prev))
                        if allowed[v] == 0:
                            ok = False
                            break
            if ok:
                if dfs(i + 1):
                    return True
            # revert changes
            for v, prev in changes:
                allowed[v] = prev
            ans[u] = 0
        return False

    if dfs(1):
        print(' '.join(str(ans[i]) for i in range(1, n + 1)))
    else:
        print(-1)

if __name__ == "__main__":
    main()