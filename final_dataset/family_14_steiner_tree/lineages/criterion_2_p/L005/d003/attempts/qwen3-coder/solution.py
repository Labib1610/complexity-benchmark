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
    priorities = set(map(int, sys.stdin.readline().split()))
    
    if t <= 1:
        print(0)
        return

    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((w, u, v))
    
    # Sort edges by weight
    edges.sort()
    
    # Build the tree with only edges connecting priority nodes
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    total_cost = 0
    components = len(priorities)
    
    for w, u, v in edges:
        # Check if u or v is a priority node
        u_is_priority = u in priorities
        v_is_priority = v in priorities
        
        pu = find_parent(parent, u)
        pv = find_parent(parent, v)
        
        if pu != pv:
            # Union the components
            union(parent, rank, u, v)
            
            # If both were priority nodes in different components, we reduce component count
            if u_is_priority and v_is_priority:
                components -= 1
                if components == 1:
                    break
            # If one was priority and the other connects to a priority component
            # we still need to count this edge if it helps connect priority nodes
            
            total_cost += w
    
    print(total_cost)

if __name__ == "__main__":
    main()