import sys
from collections import deque

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        adj[u].append(v)
        adj[v].append(u)

    parity = [-1] * n  # 0 or 1
    result = [0] * n
    INF = n + 1

    for start in range(n):
        if parity[start] != -1:
            continue
        q = deque([start])
        parity[start] = 0
        comp = [start]
        min0 = start + 1
        min1 = INF
        ok = True
        while q:
            u = q.popleft()
            for w in adj[u]:
                if parity[w] == -1:
                    parity[w] = parity[u] ^ 1
                    if parity[w] == 0:
                        if w + 1 < min0:
                            min0 = w + 1
                    else:
                        if w + 1 < min1:
                            min1 = w + 1
                    comp.append(w)
                    q.append(w)
                elif parity[w] == parity[u]:
                    ok = False
                    break
            if not ok:
                break
        if not ok:
            print("NO")
            return
        # decide mapping
        if min0 < min1:
            map0 = 1
            map1 = 2
        else:
            map0 = 2
            map1 = 1
        for v in comp:
            if parity[v] == 0:
                result[v] = map0
            else:
                result[v] = map1

    print("YES")
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    solve()