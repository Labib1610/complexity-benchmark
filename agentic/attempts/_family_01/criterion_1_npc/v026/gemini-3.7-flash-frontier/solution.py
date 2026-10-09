import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n)]
    adj_set = [set() for _ in range(n)]
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx+1]) - 1
        idx += 2
        if u != v and v not in adj_set[u]:
            adj_set[u].add(v)
            adj_set[v].add(u)
            adj[u].append(v)
            adj[v].append(u)
            
    # Degree <= 2 peeling
    degree = [len(adj[i]) for i in range(n)]
    active = [True] * n
    peeled = []
    
    queue = [i for i in range(n) if degree[i] <= 2]
    head = 0
    while head < len(queue):
        u = queue[head]
        head += 1
        if not active[u]:
            continue
        active[u] = False
        peeled.append(u)
        for v in adj[u]:
            if active[v]:
                degree[v] -= 1
                if degree[v] <= 2:
                    queue.append(v)
                    
    remaining = [i for i in range(n) if active[i]]
    
    color = [0] * n
    
    if remaining:
        # Build subproblem
        # masks for available colors: 1 (1), 2 (2), 3 (4) -> initially 7 (111 in binary)
        masks = [7] * n
        
        def backtrack():
            # Find unassigned vertex with minimum available colors
            min_c = 4
            best_v = -1
            all_done = True
            
            for v in remaining:
                if color[v] == 0:
                    all_done = False
                    c = bin(masks[v]).count('1')
                    if c < min_c:
                        min_c = c
                        best_v = v
                        if min_c == 0:
                            return False
                        if min_c == 1:
                            break
                            
            if all_done:
                return True
                
            v = best_v
            v_mask = masks[v]
            
            for col in (1, 2, 3):
                col_bit = 1 << (col - 1)
                if v_mask & col_bit:
                    color[v] = col
                    # Forward checking
                    changed = []
                    valid = True
                    for u in adj[v]:
                        if active[u] and color[u] == 0:
                            if masks[u] & col_bit:
                                masks[u] ^= col_bit
                                changed.append(u)
                                if masks[u] == 0:
                                    valid = False
                    
                    if valid and backtrack():
                        return True
                        
                    # Undo
                    for u in changed:
                        masks[u] |= col_bit
                    color[v] = 0
                    
            return False

        if not backtrack():
            print("NO")
            return

    # Color peeled vertices in reverse order
    for u in reversed(peeled):
        used = set()
        for v in adj[u]:
            if color[v] != 0:
                used.add(color[v])
        for c in (1, 2, 3):
            if c not in used:
                color[u] = c
                break

    print("YES")
    print(*(color[i] for i in range(n)))

if __name__ == '__main__':
    solve()