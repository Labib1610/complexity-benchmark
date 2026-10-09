import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); t = int(next(it))
    required = [0] * (n + 1)
    for _ in range(t):
        required[int(next(it))] = 1
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it)); w = int(next(it))
        adj[u].append((v, w))
        adj[v].append((u, w))

    total = 0
    visited = [False] * (n + 1)
    stack = [(1, 0, 0)]  # node, parent, state 0=pre,1=post
    sub_cnt = [0] * (n + 1)
    while stack:
        u, p, state = stack.pop()
        if state == 0:
            visited[u] = True
            stack.append((u, p, 1))
            for v, w in adj[u]:
                if v == p:
                    continue
                stack.append((v, u, 0))
        else:
            cnt = required[u]
            for v, w in adj[u]:
                if v == p:
                    continue
                cnt += sub_cnt[v]
                if 0 < sub_cnt[v] < t:
                    total += w
            sub_cnt[u] = cnt

    print(total)

if __name__ == "__main__":
    solve()