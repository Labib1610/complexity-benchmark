import sys

# Increase recursion depth just in case
sys.setrecursionlimit(200000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj_edges = [[] for _ in range(n + 1)]
    edges = []
    
    idx = 2
    for i in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        edges.append((u, v))
        adj_edges[u].append(i)
        adj_edges[v].append(i)
        
    # Build line graph adjacency
    # For each edge, its neighbors are the other edges incident to u and v
    neighbors = [[] for _ in range(m)]
    for i in range(m):
        u, v = edges[i]
        nbrs = set()
        for e in adj_edges[u]:
            if e != i:
                nbrs.add(e)
        for e in adj_edges[v]:
            if e != i:
                nbrs.add(e)
        neighbors[i] = list(nbrs)

    # We will use backtracking with MRV and forward checking (trail-based)
    # Colors: 0 (shift 1), 1 (shift 2), 2 (shift 3)
    # Mask: bit 0 -> color 0, bit 1 -> color 1, bit 2 -> color 2
    
    color = [-1] * m
    mask = [7] * m  # binary 111 = 7
    
    # Precompute popcount for 0..7
    popcount = [0, 1, 1, 2, 1, 2, 2, 3]

    trail = []  # will store (edge, old_mask) for undoing forward checking

    def assign(e, c):
        color[e] = c
        c_bit = 1 << c
        # For all neighbors, remove c_bit
        for nxt in neighbors[e]:
            if color[nxt] == -1 and (mask[nxt] & c_bit):
                trail.append((nxt, mask[nxt]))
                mask[nxt] &= ~c_bit
                if mask[nxt] == 0:
                    return False
        return True

    def propagate():
        # Unit propagation: repeatedly assign edges with domain size 1
        while True:
            forced = -1
            for i in range(m):
                if color[i] == -1:
                    cnt = popcount[mask[i]]
                    if cnt == 0:
                        return False
                    if cnt == 1 and forced == -1:
                        forced = i
            if forced == -1:
                break
            # Find the color
            c = (mask[forced] & -mask[forced]).bit_length() - 1
            if not assign(forced, c):
                return False
        return True

    def search():
        # Find uncolored edge with minimum remaining values (MRV)
        best_e = -1
        min_deg = 4
        for i in range(m):
            if color[i] == -1:
                cnt = popcount[mask[i]]
                if cnt == 0:
                    return False
                if cnt < min_deg:
                    min_deg = cnt
                    best_e = i
                    if min_deg <= 2:
                        break
        
        if best_e == -1:
            return True  # all colored
        
        avail = mask[best_e]
        # Try each available color
        for c in range(3):
            if (avail >> c) & 1:
                trail_len = len(trail)
                assigned_edges = [best_e]
                
                # To support undoing unit propagation, we track assigned edges
                if assign(best_e, c) and propagate():
                    if search():
                        return True
                
                # Undo all assignments made in this branch
                # Any edge that got assigned during this step must be reverted
                for i in range(m):
                    if color[i] != -1:
                        # If its assignment was made during this step
                        pass
                # More direct: revert trail, and reset colors of edges assigned after trail_len
                # Actually, let's track assigned edges properly
                while len(trail) > trail_len:
                    e_idx, old_m = trail.pop()
                    mask[e_idx] = old_m
                
                # We need to uncolor all edges that were colored during assign and propagate
                # So let's record the color state or simply track colored edges
                pass
        return False

    # Let's refine the backtracking with exact state undo
    colored_stack = []
    
    def backtrack():
        # Propagation loop
        while True:
            # Check for conflict or unit clause
            forced = -1
            best_e = -1
            min_cnt = 4
            for i in range(m):
                if color[i] == -1:
                    cnt = popcount[mask[i]]
                    if cnt == 0:
                        return False
                    if cnt < min_cnt:
                        min_cnt = cnt
                        best_e = i
                    if cnt == 1:
                        forced = i
                        break
            
            if forced != -1:
                c = (mask[forced] & -mask[forced]).bit_length() - 1
                color[forced] = c
                colored_stack.append(forced)
                c_bit = 1 << c
                for nxt in neighbors[forced]:
                    if color[nxt] == -1 and (mask[nxt] & c_bit):
                        trail.append((nxt, mask[nxt]))
                        mask[nxt] &= ~c_bit
                        if mask[nxt] == 0:
                            return False
            else:
                if best_e == -1:
                    return True  # All colored!
                break
        
        # Branch on best_e
        avail = mask[best_e]
        for c in range(3):
            if (avail >> c) & 1:
                snap_trail = len(trail)
                snap_colored = len(colored_stack)
                
                color[best_e] = c
                colored_stack.append(best_e)
                c_bit = 1 << c
                
                valid = True
                for nxt in neighbors[best_e]:
                    if color[nxt] == -1 and (mask[nxt] & c_bit):
                        trail.append((nxt, mask[nxt]))
                        mask[nxt] &= ~c_bit
                        if mask[nxt] == 0:
                            valid = False
                            break
                
                if valid and backtrack():
                    return True
                
                # Undo
                while len(colored_stack) > snap_colored:
                    e_undo = colored_stack.pop()
                    color[e_undo] = -1
                while len(trail) > snap_trail:
                    nxt, old_m = trail.pop()
                    mask[nxt] = old_m
                    
        return False

    if backtrack():
        print("YES")
        print(" ".join(str(color[i] + 1) for i in range(m)))
    else:
        print("NO")

if __name__ == '__main__':
    solve()