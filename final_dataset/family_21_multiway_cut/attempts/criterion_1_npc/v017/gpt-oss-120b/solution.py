import sys
from itertools import combinations

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it)); B = int(next(it))
    hubs = set(int(next(it)) for _ in range(k))
    edges = []
    for _ in range(m):
        u = int(next(it)); v = int(next(it)); w = int(next(it))
        edges.append((u, v, w))
    # adjacency for quick BFS
    adj_full = [[] for _ in range(n+1)]
    for idx, (u, v, w) in enumerate(edges):
        adj_full[u].append((v, idx))
        adj_full[v].append((u, idx))

    # try all subsets up to budget
    # enumerate by increasing number of edges to possibly find small solution early
    for r in range(m+1):
        for combo in combinations(range(m), r):
            total = sum(edges[i][2] for i in combo)
            if total > B:
                continue
            removed = set(combo)
            # BFS from each hub, label component
            comp = {}
            label = 0
            visited = [False]*(n+1)
            for node in range(1, n+1):
                if not visited[node]:
                    label += 1
                    stack = [node]
                    visited[node] = True
                    while stack:
                        cur = stack.pop()
                        comp[cur] = label
                        for nb, eid in adj_full[cur]:
                            if eid in removed:
                                continue
                            if not visited[nb]:
                                visited[nb] = True
                                stack.append(nb)
            # check hubs all in distinct components
            hub_labels = {comp[h] for h in hubs}
            if len(hub_labels) == k:
                # success
                out = ["YES", str(r)]
                for i in combo:
                    u, v, _ = edges[i]
                    out.append(f"{u} {v}")
                sys.stdout.write("\n".join(out))
                return
    sys.stdout.write("NO")

if __name__ == "__main__":
    solve()