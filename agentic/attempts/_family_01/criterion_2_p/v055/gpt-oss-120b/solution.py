import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    color = [ -1 ] * (n + 1)          # 0/1 parity inside component
    phase = [ 0 ] * (n + 1)            # final answer 1 or 2
    from collections import deque

    for i in range(1, n + 1):
        if color[i] != -1:
            continue
        # start new component
        q = deque([i])
        color[i] = 0
        comp = [i]
        ok = True
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    q.append(v)
                    comp.append(v)
                elif color[v] == color[u]:
                    ok = False
                    break
            if not ok:
                break
        if not ok:
            print("NO")
            return
        # orient component so that node i gets phase 1
        start_par = color[i]
        for v in comp:
            phase[v] = 1 if color[v] == start_par else 2

    print("YES")
    print(' '.join(str(phase[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    solve()