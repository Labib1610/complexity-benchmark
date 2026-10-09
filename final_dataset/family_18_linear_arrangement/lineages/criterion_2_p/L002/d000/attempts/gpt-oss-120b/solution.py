import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    adj = [[] for _ in range(n)]
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))

    # 1. compute subtree sizes from an arbitrary root to get MIN
    parent = [-1] * n
    order = [0]
    parent[0] = -2
    for v in order:
        for to in adj[v]:
            if parent[to] == -1:
                parent[to] = v
                order.append(to)
    sub = [1] * n
    for v in reversed(order):
        for to in adj[v]:
            if to != parent[v]:
                sub[v] += sub[to]

    MIN = 0
    for u, v in edges:
        s = sub[u] if parent[v] == u else sub[v]
        MIN += min(s, n - s)

    if B < MIN:
        print("NO")
        return

    # 2. centroid decomposition and ordering
    removed = [False] * n
    answer = []

    from collections import deque

    def collect_component(start):
        comp = []
        dq = deque([start])
        removed[start] = True  # temporary mark to avoid revisiting
        while dq:
            v = dq.popleft()
            comp.append(v)
            for to in adj[v]:
                if not removed[to]:
                    removed[to] = True
                    dq.append(to)
        # unmark for later use
        for v in comp:
            removed[v] = False
        return comp

    def find_centroid(comp):
        sz = len(comp)
        # map vertex -> index in comp for fast lookup
        in_comp = set(comp)
        # compute sizes inside this component
        stack = [(comp[0], -1, 0)]  # (node, parent, state) state 0=first,1=post
        order = []
        while stack:
            v, p, state = stack.pop()
            if state == 0:
                stack.append((v, p, 1))
                for to in adj[v]:
                    if to != p and not removed[to] and to in in_comp:
                        stack.append((to, v, 0))
            else:
                order.append((v, p))
        subc = {}
        for v, p in order:
            cur = 1
            for to in adj[v]:
                if to != p and not removed[to] and to in in_comp:
                    cur += subc[to]
            subc[v] = cur

        centroid = None
        for v, p in order:
            max_part = sz - subc[v]  # part outside
            for to in adj[v]:
                if to != p and not removed[to] and to in in_comp:
                    max_part = max(max_part, subc[to])
            if max_part * 2 <= sz:
                centroid = v
                break
        return centroid

    sys.setrecursionlimit(1 << 25)

    def decompose(start):
        comp = collect_component(start)
        c = find_centroid(comp)
        removed[c] = True
        answer.append(c + 1)          # store 1‑based bay number
        for nb in adj[c]:
            if not removed[nb]:
                decompose(nb)

    decompose(0)

    print("YES")
    print(' '.join(map(str, answer)))

if __name__ == "__main__":
    solve()