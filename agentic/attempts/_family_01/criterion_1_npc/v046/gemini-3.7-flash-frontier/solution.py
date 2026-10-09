import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx+1]) - 1
        idx += 2
        if u != v:
            adj[u].append(v)
            adj[v].append(u)
    
    # Remove duplicate edges
    for i in range(n):
        adj[i] = list(set(adj[i]))
        
    color = [0] * n
    domain = [7] * n  # bitmask: bit 0 -> color 1, bit 1 -> color 2, bit 2 -> color 3
    
    # Precompute popcount for 0..7
    popcnt = [0, 1, 1, 2, 1, 2, 2, 3]
    
    def backtrack(assigned_count):
        if assigned_count == n:
            return True
        
        # MRV: Choose unassigned vertex with smallest domain size, break ties by degree
        best_u = -1
        min_size = 4
        max_deg = -1
        
        for u in range(n):
            if color[u] == 0:
                sz = popcnt[domain[u]]
                if sz < min_size or (sz == min_size and len(adj[u]) > max_deg):
                    min_size = sz
                    max_deg = len(adj[u])
                    best_u = u
                    if sz <= 1:
                        break
        
        if min_size == 0:
            return False
        
        u = best_u
        u_domain = domain[u]
        
        for c in range(3):
            if (u_domain & (1 << c)):
                color[u] = c + 1
                
                # Forward check / update neighbors
                changed = []
                possible = True
                for v in adj[u]:
                    if color[v] == 0:
                        if domain[v] & (1 << c):
                            domain[v] &= ~(1 << c)
                            changed.append(v)
                            if domain[v] == 0:
                                possible = False
                
                if possible:
                    if backtrack(assigned_count + 1):
                        return True
                
                # Restore
                for v in changed:
                    domain[v] |= (1 << c)
                color[u] = 0
                
        return False

    # Also handle symmetry breaking for the first vertex of each component
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            # BFS to find component
            comp = []
            queue = [i]
            visited[i] = True
            for u in queue:
                comp.append(u)
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        queue.append(v)

    if backtrack(0):
        print("YES")
        print(*(color[i] for i in range(n)))
    else:
        print("NO")

if __name__ == '__main__':
    solve()