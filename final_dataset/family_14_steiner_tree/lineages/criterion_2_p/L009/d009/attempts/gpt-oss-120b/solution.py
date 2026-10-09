import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it)); E = int(next(it)); F = int(next(it))
    crit = set(int(next(it)) - 1 for _ in range(F))
    adj = [[] for _ in range(N)]
    edges = []
    for eid in range(E):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        adj[u].append((v, w, eid))
        adj[v].append((u, w, eid))
        edges.append((u, v, w))

    if F <= 1:
        print(0)
        return

    parent = [-1] * N
    pw = [0] * N          # weight to parent
    order = []
    stack = [0]
    parent[0] = 0
    while stack:
        node = stack.pop()
        order.append(node)
        for nb, w, _ in adj[node]:
            if parent[nb] == -1:
                parent[nb] = node
                pw[nb] = w
                stack.append(nb)

    term_cnt = [0] * N
    for v in crit:
        term_cnt[v] = 1

    total_terms = F
    ans = 0
    for node in reversed(order):
        if node == 0:
            continue
        cnt = term_cnt[node]
        if cnt > 0 and total_terms - cnt > 0:
            ans += pw[node]
        term_cnt[parent[node]] += cnt

    print(ans)

if __name__ == "__main__":
    solve()