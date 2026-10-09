import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
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

    comp_id = [-1] * (n + 1)
    parity = [0] * (n + 1)
    min_vertex = []
    comp_cnt = 0

    for start in range(1, n + 1):
        if comp_id[start] != -1:
            continue
        # new component
        q = deque([start])
        comp_id[start] = comp_cnt
        parity[start] = 0
        cur_min = start
        while q:
            v = q.popleft()
            cur_min = min(cur_min, v)
            for to in adj[v]:
                if comp_id[to] == -1:
                    comp_id[to] = comp_cnt
                    parity[to] = parity[v] ^ 1
                    q.append(to)
                else:
                    if parity[to] == parity[v]:
                        sys.stdout.write("NO")
                        return
        min_vertex.append(cur_min)
        comp_cnt += 1

    # decide orientation
    flip = [0] * comp_cnt
    for c in range(comp_cnt):
        first = min_vertex[c]
        if parity[first] == 1:
            flip[c] = 1

    # build answer
    ans = [0] * n
    for v in range(1, n + 1):
        c = comp_id[v]
        col = parity[v] ^ flip[c]   # 0 or 1
        ans[v - 1] = 1 if col == 0 else 2

    out = ["YES", " ".join(map(str, ans))]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()