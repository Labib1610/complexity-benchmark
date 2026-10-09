import sys
import heapq

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    try:
        n = int(next(it))
        m = int(next(it))
        s = int(next(it))
        t = int(next(it))
        B = int(next(it))
    except StopIteration:
        return

    adj = [[] for _ in range(n + 1)]
    edges = []
    for i in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        adj[u].append((v, w, i))
        adj[v].append((u, w, i))
        edges.append((u, v, w))

    # Dijkstra from s
    dist_s = [float('inf')] * (n + 1)
    dist_s[s] = 0
    pq = [(0, s)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist_s[u]:
            continue
        for v, w, _ in adj[u]:
            if dist_s[v] > d + w:
                dist_s[v] = d + w
                heapq.heappush(pq, (dist_s[v], v))

    # Dijkstra from t
    dist_t = [float('inf')] * (n + 1)
    dist_t[t] = 0
    pq = [(0, t)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist_t[u]:
            continue
        for v, w, _ in adj[u]:
            if dist_t[v] > d + w:
                dist_t[v] = d + w
                heapq.heappush(pq, (dist_t[v], v))

    min_path_cost = dist_s[t]
    if min_path_cost > B:
        print("NO")
        return

    # Build level graph
    level = [0] * (n + 1)
    for u in range(1, n + 1):
        if dist_s[u] + dist_t[u] == min_path_cost:
            level[u] = dist_s[u]

    # Find edges on shortest paths
    blocked_edges = []
    for idx, (u, v, w) in enumerate(edges):
        on_path = False
        if dist_s[u] + w + dist_t[v] == min_path_cost:
            on_path = True
        elif dist_s[v] + w + dist_t[u] == min_path_cost:
            on_path = True
        
        if on_path:
            blocked_edges.append((u, v))

    print("YES")
    print(len(blocked_edges))
    for u, v in blocked_edges:
        print(u, v)

if __name__ == "__main__":
    solve()