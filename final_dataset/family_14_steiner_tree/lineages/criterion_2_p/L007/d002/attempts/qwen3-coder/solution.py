import sys
from collections import defaultdict, deque

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    px, py = find_parent(parent, x), find_parent(parent, y)
    if px == py:
        return
    if rank[px] < rank[py]:
        px, py = py, px
    parent[py] = px
    if rank[px] == rank[py]:
        rank[px] += 1

def main():
    n, m, t = map(int, sys.stdin.readline().split())
    rented = set(map(int, sys.stdin.readline().split()))
    
    if t <= 1:
        print(0)
        return
    
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((w, u, v))
    
    edges.sort()
    
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    total_cost = 0
    components = t
    
    for w, u, v in edges:
        pu = find_parent(parent, u)
        pv = find_parent(parent, v)
        
        if pu != pv:
            union(parent, rank, u, v)
            if u in rented or v in rented or pu in rented or pv in rented:
                total_cost += w
                components -= 1
                if components == 1:
                    break
    
    print(total_cost)

if __name__ == "__main__":
    main()