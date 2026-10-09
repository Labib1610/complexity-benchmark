import sys
from collections import defaultdict
import heapq

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    px, py = find(parent, x), find(parent, y)
    if px == py:
        return False
    if rank[px] < rank[py]:
        px, py = py, px
    parent[py] = px
    if rank[px] == rank[py]:
        rank[px] += 1
    return True

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    t = int(data[idx])
    idx += 1
    
    qc_stations = set()
    for _ in range(t):
        qc_stations.add(int(data[idx]))
        idx += 1
    
    edges = []
    for _ in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        w = int(data[idx])
        idx += 1
        edges.append((w, u, v))
    
    if t <= 1:
        print(0)
        return
    
    # Sort edges by weight
    edges.sort()
    
    # Initialize Union-Find
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    total_cost = 0
    connected_qc = set()
    
    for w, u, v in edges:
        if union(parent, rank, u, v):
            total_cost += w
            # Check if either endpoint is a QC station
            if u in qc_stations:
                connected_qc.add(u)
            if v in qc_stations:
                connected_qc.add(v)
            
            # If all QC stations are connected, we're done
            if len(connected_qc) == t:
                # Verify all QC stations are in the same component
                root = find(parent, next(iter(qc_stations)))
                if all(find(parent, qc) == root for qc in qc_stations):
                    break
    
    print(total_cost)

if __name__ == "__main__":
    main()