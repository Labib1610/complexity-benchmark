import sys
import threading

def main():
    import sys
    import threading
    sys.setrecursionlimit(1 << 25)
    
    n, m, t = map(int, sys.stdin.readline().split())
    observables = list(map(int, sys.stdin.readline().split()))
    
    if t <= 1:
        print(0)
        return
    
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((w, u-1, v-1))  # Convert to 0-indexed
    
    # Convert observables to 0-indexed set
    obs_set = set(x-1 for x in observables)
    
    # Sort edges by weight
    edges.sort()
    
    # Union-Find data structure
    parent = list(range(n))
    rank = [0] * n
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return
        if rank[px] < rank[py]:
            px, py = py, px
        parent[py] = px
        if rank[px] == rank[py]:
            rank[px] += 1
    
    total_cost = 0
    components = len(obs_set)
    
    for weight, u, v in edges:
        if find(u) != find(v):
            # Check if this union connects two components containing observables
            u_root, v_root = find(u), find(v)
            u_has_obs = u_root in obs_set
            v_has_obs = v_root in obs_set
            
            union(u, v)
            
            # Check if we just connected two observable components
            if u_has_obs and v_has_obs:
                components -= 1
                total_cost += weight
                if components == 1:
                    break
            elif u_has_obs or v_has_obs:
                # One of them had observables, so the new root has observables
                new_root = find(u)
                if u_root in obs_set:
                    obs_set.add(new_root)
                if v_root in obs_set:
                    obs_set.add(new_root)
                obs_set.discard(u_root)
                obs_set.discard(v_root)
    
    print(total_cost)

threading.Thread(target=main).start()