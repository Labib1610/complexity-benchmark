import sys

# Increase recursion depth just in case
sys.setrecursionlimit(100000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    
    idx = 2
    for i in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        edges.append((u, v))
        adj[u].append(i)
        adj[v].append(i)
        
    edge_color = [0] * m
    edge_mask = [7] * m  # bitmask of available colors: 1 (bit 0), 2 (bit 1), 3 (bit 2) -> 7 = 1|2|4
    
    # Precompute adjacent edges for each edge
    adj_edges = [[] for _ in range(m)]
    for e in range(m):
        u, v = edges[e]
        neighbors = set()
        for e2 in adj[u]:
            if e2 != e:
                neighbors.add(e2)
        for e2 in adj[v]:
            if e2 != e:
                neighbors.add(e2)
        adj_edges[e] = list(neighbors)

    popcount = [0, 1, 1, 2, 1, 2, 2, 3]

    def propagate(forced_assignments):
        history = []  # list of (edge, old_color, old_mask)
        q = list(forced_assignments)
        
        while q:
            e, c = q.pop()
            c_bit = 1 << (c - 1)
            
            if edge_color[e] != 0:
                if edge_color[e] != c:
                    return False, history
                continue
                
            if not (edge_mask[e] & c_bit):
                return False, history
                
            history.append((e, edge_color[e], edge_mask[e]))
            edge_color[e] = c
            edge_mask[e] = c_bit
            
            u, v = edges[e]
            for vertex in (u, v):
                uncolored = []
                used_colors = 0
                for e2 in adj[vertex]:
                    if edge_color[e2] != 0:
                        if used_colors & (1 << (edge_color[e2] - 1)):
                            return False, history
                        used_colors |= (1 << (edge_color[e2] - 1))
                    else:
                        uncolored.append(e2)
                
                if len(uncolored) == 1:
                    rem_mask = 7 ^ used_colors
                    rem_c = (rem_mask & -rem_mask).bit_length()
                    q.append((uncolored[0], rem_c))
                elif len(uncolored) == 0:
                    if used_colors != 7:
                        return False, history
            
            for e2 in adj_edges[e]:
                if edge_color[e2] == 0:
                    if edge_mask[e2] & c_bit:
                        history.append((e2, edge_color[e2], edge_mask[e2]))
                        edge_mask[e2] &= ~c_bit
                        if edge_mask[e2] == 0:
                            return False, history
                        if popcount[edge_mask[e2]] == 1:
                            rem_c = (edge_mask[e2]).bit_length()
                            q.append((e2, rem_c))
                            
        return True, history

    def rollback(history):
        for e, old_c, old_m in reversed(history):
            edge_color[e] = old_c
            edge_mask[e] = old_m

    def backtrack():
        # Find unassigned edge with minimum remaining values
        best_e = -1
        min_vals = 4
        
        for e in range(m):
            if edge_color[e] == 0:
                cnt = popcount[edge_mask[e]]
                if cnt < min_vals:
                    min_vals = cnt
                    best_e = e
                    if min_vals <= 1:
                        break
                        
        if best_e == -1:
            return True
            
        mask = edge_mask[best_e]
        for c in (1, 2, 3):
            if mask & (1 << (c - 1)):
                success, history = propagate([(best_e, c)])
                if success:
                    if backtrack():
                        return True
                rollback(history)
                
        return False

    if backtrack():
        print("YES")
        print(*(edge_color[i] for i in range(m)))
    else:
        print("NO")

if __name__ == '__main__':
    solve()