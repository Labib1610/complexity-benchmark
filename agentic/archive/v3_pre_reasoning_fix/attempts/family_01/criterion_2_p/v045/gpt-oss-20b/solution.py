import sys
from collections import deque

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = next(it)
        v = next(it)
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * (n + 1)      # 0 or 1
    comp_id = [-1] * (n + 1)    # component index
    comp_counter = 0

    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        comp_counter += 1
        dq = deque([start])
        color[start] = 0
        comp_id[start] = comp_counter
        while dq:
            u = dq.popleft()
            cu = color[u]
            for w in adj[u]:
                if color[w] == -1:
                    color[w] = cu ^ 1
                    comp_id[w] = comp_counter
                    dq.append(w)
                elif color[w] == cu:
                    print("NO")
                    return

    comp_flip = [-1] * (comp_counter + 1)  # 0: keep, 1: flip
    ans = [0] * (n + 1)

    for i in range(1, n + 1):
        cid = comp_id[i]
        ci = color[i]
        if comp_flip[cid] == -1:
            comp_flip[cid] = 0 if ci == 0 else 1
        ans[i] = 1 + (ci ^ comp_flip[cid])

    print("YES")
    print(' '.join(map(str, ans[1:])))

if __name__ == "__main__":
    solve()