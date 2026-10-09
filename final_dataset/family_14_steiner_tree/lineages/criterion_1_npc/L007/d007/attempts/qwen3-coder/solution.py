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

def solve():
    n, m, t = map(int, sys.stdin.readline().split())
    committee = list(map(int, sys.stdin.readline().split()))
    
    if t <= 1:
        print(0)
        return
    
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((w, u, v))
    
    # Sort edges by weight
    edges.sort()
    
    # We want to ensure all members of the committee are connected
    # This is equivalent to finding the minimum cost to connect all committee members
    # We can use a modified Kruskal's algorithm or think of it as a Steiner tree problem
    # But since t is small (<= 10), we can try a different approach
    
    # The optimal solution is to make sure all committee members are in the same component
    # So we can try to find the minimum cost to connect all of them
    # This is essentially finding the minimum spanning tree that connects all committee members
    
    # We'll use a greedy approach:
    # Try to connect all committee members with minimum cost
    # We can use Union-Find and Kruskal's algorithm but stop when all committee members are connected
    
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    # Count how many committee members are in each component
    committee_in_component = defaultdict(int)
    for c in committee:
        committee_in_component[c] = 1
    
    total_cost = 0
    components_with_committee = len(committee)
    
    # Continue until all committee members are in the same component
    for w, u, v in edges:
        pu, pv = find(parent, u), find(parent, v)
        if pu != pv:
            # Check how many committee members are in each component
            count_u = sum(1 for c in committee if find(parent, c) == pu)
            count_v = sum(1 for c in committee if find(parent, c) == pv)
            
            # If connecting these two would merge components with committee members
            if count_u > 0 and count_v > 0:
                total_cost += w
                union(parent, rank, u, v)
            elif count_u > 0 or count_v > 0:
                total_cost += w
                union(parent, rank, u, v)
                
        # Check if all committee members are now in the same component
        first_component = find(parent, committee[0])
        if all(find(parent, c) == first_component for c in committee):
            break
            
    print(total_cost)

solve()