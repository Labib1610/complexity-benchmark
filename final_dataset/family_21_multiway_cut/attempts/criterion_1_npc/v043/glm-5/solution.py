import sys
from collections import deque

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    B = int(next(it))
    
    sources = []
    for _ in range(k):
        sources.append(int(next(it)))
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edges.append((u, v, w))
        adj[u].append((v, w, len(edges) - 1))
        adj[v].append((u, w, len(edges) - 1))
    
    # BFS to find minimum cost edges to cut
    color = [0] * (n + 1)  # 0 = uncolored, 1..k = source color
    cut_edges = []
    
    for i, src in enumerate(sources, 1):
        if color[src] != 0:
            continue
        color[src] = i
        q = deque([src])
        while q:
            u = q.popleft()
            for v, w, idx in adj[u]:
                if color[v] == 0:
                    color[v] = i
                    q.append(v)
                elif color[v] == color[u]:
                    continue
                else:
                    # Conflict edge - need to cut
                    cut_edges.append((w, idx, u, v))
    
    # Remove duplicates and sort by weight
    seen = set()
    unique_cuts = []
    for w, idx, u, v in cut_edges:
        if idx not in seen:
            seen.add(idx)
            unique_cuts.append((w, idx, u, v))
    
    unique_cuts.sort()
    
    total_cost = 0
    result_edges = []
    for w, idx, u, v in unique_cuts:
        if total_cost + w <= B:
            total_cost += w
            result_edges.append((u, v))
        else:
            break
    
    # Verify solution
    # Re-check if all conflicts are resolved
    temp_color = [0] * (n + 1)
    edge_set = set()
    for u, v in result_edges:
        edge_set.add((min(u, v), max(u, v)))
    
    valid = True
    for i, src in enumerate(sources, 1):
        if temp_color[src] != 0:
            if temp_color[src] != i:
                valid = False
            continue
        temp_color[src] = i
        q = deque([src])
        while q:
            u = q.popleft()
            for v, w, idx in adj[u]:
                edge_key = (min(u, v), max(u, v))
                if edge_key in edge_set:
                    continue
                if temp_color[v] == 0:
                    temp_color[v] = i
                    q.append(v)
                elif temp_color[v] != temp_color[u]:
                    valid = False
                    break
            if not valid:
                break
        if not valid:
            break
    
    if valid and total_cost <= B:
        print("YES")
        print(len(result_edges))
        for u, v in result_edges:
            print(u, v)
    else:
        print("NO")

if __name__ == "__main__":
    solve()