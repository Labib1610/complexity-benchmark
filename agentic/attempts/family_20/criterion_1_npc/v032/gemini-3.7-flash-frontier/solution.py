import sys

# Increase recursion depth just in case
sys.setrecursionlimit(3000)

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
    
    # Check degree: every hub must have 3 links
    for u in range(1, n + 1):
        if len(adj[u]) != 3:
            print("NO")
            return

    # Build neighbor edge lists
    nbr_edges = [[] for _ in range(m)]
    for i in range(m):
        u, v = edges[i]
        nbrs = set()
        for e in adj[u]:
            if e != i:
                nbrs.add(e)
        for e in adj[v]:
            if e != i:
                nbrs.add(e)
        nbr_edges[i] = list(nbrs)

    avail = [7] * m  # 3 bits: 1, 2, 4
    color = [-1] * m
    
    # Symmetry breaking: color the 3 edges incident to vertex 1 with 0, 1, 2
    e0, e1, e2 = adj[1]
    
    def assign(e, c, changes):
        color[e] = c
        bit = 1 << c
        for nbr in nbr_edges[e]:
            if color[nbr] == -1 and (avail[nbr] & bit):
                avail[nbr] ^= bit
                changes.append((nbr, bit))

    def backtrack():
        # Unit propagation & MRV
        forced_stack = []
        local_changes = []
        
        while True:
            # Find an unassigned edge with min available colors
            min_c = 4
            best_e = -1
            for e in range(m):
                if color[e] == -1:
                    mask = avail[e]
                    cnt = (mask & 1) + ((mask >> 1) & 1) + ((mask >> 2) & 1)
                    if cnt == 0:
                        # Conflict, undo all local changes
                        for nbr, bit in reversed(local_changes):
                            avail[nbr] |= bit
                        for fe in forced_stack:
                            color[fe] = -1
                        return False
                    if cnt < min_c:
                        min_c = cnt
                        best_e = e
                        if cnt == 1:
                            break
            
            if best_e == -1:
                # All edges colored
                return True
            
            if min_c == 1:
                mask = avail[best_e]
                c = 0 if (mask & 1) else (1 if (mask & 2) else 2)
                forced_stack.append(best_e)
                assign(best_e, c, local_changes)
            else:
                # Branch on best_e
                break

        # best_e has 2 or 3 choices
        mask = avail[best_e]
        choices = []
        for c in range(3):
            if mask & (1 << c):
                choices.append(c)
                
        for c in choices:
            branch_changes = []
            assign(best_e, c, branch_changes)
            if backtrack():
                return True
            # Undo branch
            for nbr, bit in reversed(branch_changes):
                avail[nbr] |= bit
            color[best_e] = -1

        # Undo forced assignments
        for nbr, bit in reversed(local_changes):
            avail[nbr] |= bit
        for fe in forced_stack:
            color[fe] = -1

        return False

    # Apply initial symmetry breaking
    initial_changes = []
    assign(e0, 0, initial_changes)
    assign(e1, 1, initial_changes)
    assign(e2, 2, initial_changes)

    if backtrack():
        print("YES")
        print(*(color[i] + 1 for i in range(m)))
    else:
        print("NO")

if __name__ == '__main__':
    solve()