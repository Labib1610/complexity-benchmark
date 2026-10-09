import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    N, E, F = map(int, sys.stdin.readline().split())
    critical = set(map(int, sys.stdin.readline().split()))
    
    edges = []
    for _ in range(E):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((w, u, v))
    
    # Sort edges by weight
    edges.sort()
    
    # Union-Find data structure
    parent = list(range(N + 1))
    rank = [0] * (N + 1)
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return False
        if rank[px] < rank[py]:
            px, py = py, px
        parent[py] = px
        if rank[px] == rank[py]:
            rank[px] += 1
        return True
    
    # Kruskal's algorithm to find MST
    mst_edges = []
    for w, u, v in edges:
        if union(u, v):
            mst_edges.append((w, u, v))
        if len(mst_edges) == N - 1:
            break
    
    # Now we need to find the minimum cost to connect all critical nodes
    # This is equivalent to finding the MST of the subgraph induced by critical nodes
    # We can do this by running Kruskal again on the MST edges but only considering critical nodes
    
    parent_critical = list(range(N + 1))
    rank_critical = [0] * (N + 1)
    
    def find_critical(x):
        if parent_critical[x] != x:
            parent_critical[x] = find_critical(parent_critical[x])
        return parent_critical[x]
    
    def union_critical(x, y):
        px, py = find_critical(x), find_critical(y)
        if px == py:
            return False
        if rank_critical[px] < rank_critical[py]:
            px, py = py, px
        parent_critical[py] = px
        if rank_critical[px] == rank_critical[py]:
            rank_critical[px] += 1
        return True
    
    total_cost = 0
    components = len(critical)
    
    for w, u, v in mst_edges:
        if u in critical and v in critical:
            if union_critical(u, v):
                total_cost += w
                components -= 1
                if components == 1:
                    break
        elif u in critical or v in critical:
            # One endpoint is critical, the other is not
            # We need to include this edge to connect the critical node
            if union_critical(u, v):
                total_cost += w
                # Mark the non-critical node as "connected"
                # But we don't reduce components because it's not a separate component
    
    print(total_cost)

threading.Thread(target=main).start()