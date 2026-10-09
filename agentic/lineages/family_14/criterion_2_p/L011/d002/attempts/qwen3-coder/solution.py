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
    
    reserve_currencies = list(map(int, data[idx:idx+t]))
    idx += t
    
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
    
    # Convert reserve currencies to a set for faster lookup
    reserve_set = set(reserve_currencies)
    
    # Sort edges by weight
    edges.sort()
    
    # Initialize Union-Find structure
    parent = list(range(n + 1))
    rank = [0] * (n + 1)
    
    total_cost = 0
    connected_reserves = 0
    
    # First, connect all reserve currencies
    for weight, u, v in edges:
        if find(parent, u) != find(parent, v):
            # Check if this edge connects to any reserve currency
            u_is_reserve = u in reserve_set
            v_is_reserve = v in reserve_set
            
            u_root = find(parent, u)
            v_root = find(parent, v)
            
            root_u_has_reserve = any(find(parent, x) == u_root for x in reserve_set)
            root_v_has_reserve = any(find(parent, x) == v_root for x in reserve_set)
            
            # If both roots have reserves, we're connecting two reserve groups
            if root_u_has_reserve and root_v_has_reserve:
                union(parent, rank, u, v)
                total_cost += weight
                connected_reserves += 1
                if connected_reserves == t - 1:
                    break
            elif u_is_reserve or v_is_reserve or root_u_has_reserve or root_v_has_reserve:
                # One side has a reserve, so connect them
                union(parent, rank, u, v)
                total_cost += weight
                if find(parent, u) == find(parent, v):  # Successfully connected
                    # Check if we've connected all reserves
                    roots_with_reserves = set()
                    for curr in reserve_set:
                        roots_with_reserves.add(find(parent, curr))
                    if len(roots_with_reserves) == 1:
                        break
    
    print(total_cost)

if __name__ == "__main__":
    main()