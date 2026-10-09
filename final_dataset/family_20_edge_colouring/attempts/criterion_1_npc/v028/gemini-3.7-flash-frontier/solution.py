import sys

# Increase recursion depth just in case
sys.setrecursionlimit(10000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    edges = []
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for i in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        edges.append((u, v))
        adj[u].append(i)
        adj[v].append(i)
        
    # Build edge adjacency (edges that share a vertex)
    edge_adj = [[] for _ in range(m)]
    for v in range(1, n + 1):
        v_edges = adj[v]
        l = len(v_edges)
        for i in range(l):
            for j in range(i + 1, l):
                e1, e2 = v_edges[i], v_edges[j]
                edge_adj[e1].append(e2)
                edge_adj[e2].append(e1)
                
    # Remove duplicates in edge_adj
    for i in range(m):
        edge_adj[i] = list(set(edge_adj[i]))

    # Edge coloring using MRV (Minimum Remaining Values) backtracking
    # Mask of available colors for each edge: bit 0 -> color 1, bit 1 -> color 2, bit 2 -> color 3
    # 7 = 0b111 (all 3 available)
    avail = [7] * m
    color = [0] * m  # 0 means uncolored, 1..3 assigned

    # Precompute bit count for masks 0..7
    bit_count = [0, 1, 1, 2, 1, 2, 2, 3]

    def get_best_edge():
        min_c = 4
        best_e = -1
        max_deg = -1
        for e in range(m):
            if color[e] == 0:
                c = bit_count[avail[e]]
                if c < min_c:
                    min_c = c
                    best_e = e
                    max_deg = len(edge_adj[e])
                    if min_c == 0:
                        return e, 0
                elif c == min_c:
                    deg = len(edge_adj[e])
                    if deg > max_deg:
                        max_deg = deg
                        best_e = e
        return best_e, min_c

    def backtrack(unassigned_count):
        if unassigned_count == 0:
            return True

        e, c = get_best_edge()
        if c == 0:
            return False

        mask = avail[e]
        for clr_idx in range(3):
            clr_bit = 1 << clr_idx
            if mask & clr_bit:
                clr = clr_idx + 1
                color[e] = clr
                
                # Forward check / eliminate color from neighbors
                changed_neighbors = []
                conflict = False
                for ne in edge_adj[e]:
                    if color[ne] == 0 and (avail[ne] & clr_bit):
                        avail[ne] ^= clr_bit
                        changed_neighbors.append(ne)
                        if avail[ne] == 0:
                            conflict = True

                if not conflict:
                    if backtrack(unassigned_count - 1):
                        return True

                # Restore
                for ne in changed_neighbors:
                    avail[ne] |= clr_bit
                color[e] = 0

        return False

    if backtrack(m):
        print("YES")
        print(*(color[i] for i in range(m)))
    else:
        print("NO")

if __name__ == '__main__':
    solve()