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

    parity = [-1] * (n + 1)   # 0 or 1
    comp_id = [-1] * (n + 1)
    comp_min = []            # min node per component

    comp_cnt = 0
    for start in range(1, n + 1):
        if parity[start] != -1:
            continue
        # new component
        q = deque([start])
        parity[start] = 0
        comp_id[start] = comp_cnt
        min_node = start
        while q:
            u = q.popleft()
            if u < min_node:
                min_node = u
            for v in adj[u]:
                if parity[v] == -1:
                    parity[v] = parity[u] ^ 1
                    comp_id[v] = comp_cnt
                    q.append(v)
                elif parity[v] == parity[u]:
                    sys.stdout.write("NO")
                    return
        comp_min.append(min_node)
        comp_cnt += 1

    # Build answer
    ans = [0] * n
    for i in range(1, n + 1):
        cid = comp_id[i]
        min_node = comp_min[cid]
        min_parity = parity[min_node]
        if parity[i] == min_parity:
            ans[i - 1] = 1
        else:
            ans[i - 1] = 2

    out_lines = ["YES", " ".join(map(str, ans))]
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()