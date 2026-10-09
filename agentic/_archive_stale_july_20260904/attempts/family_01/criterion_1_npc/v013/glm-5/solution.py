import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    adj = [0] * (n + 1)
    idx = 2
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx+1]); idx += 2
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    color = [0] * (n + 1)
    memo = {}

    def can_finish(start, used):
        if start > n:
            return True
        key = (start, used)
        if key in memo:
            return memo[key]
        res = False
        for c in (1, 2, 3):
            if color[start] == 0:
                color[start] = c
                ok = True
                for v in range(start + 1, n + 1):
                    if (adj[start] >> v) & 1 and color[v] == c:
                        ok = False
                        break
                if ok:
                    new_used = used | (1 << start)
                    if can_finish(start + 1, new_used):
                        res = True
                        break
                color[start] = 0
            else:
                if can_finish(start + 1, used | (1 << start)):
                    res = True
                    break
        memo[key] = res
        return res

    for i in range(1, n + 1):
        assigned = False
        for c in (1, 2, 3):
            ok = True
            for v in range(1, i):
                if (adj[i] >> v) & 1 and color[v] == c:
                    ok = False
                    break
            if not ok:
                continue
            color[i] = c
            memo.clear()
            if can_finish(i + 1, 1 << i):
                assigned = True
                break
            color[i] = 0
        if not assigned:
            print("NO")
            return

    print("YES")
    print(' '.join(str(color[i]) for i in range(1, n + 1)))

solve()