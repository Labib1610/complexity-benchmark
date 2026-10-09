import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    Nin = int(input_data[0])
    Nout = int(input_data[1])
    M = int(input_data[2])
    
    if M == 0:
        print("YES")
        print()
        return

    deg_L = [0] * (Nin + 1)
    deg_R = [0] * (Nout + 1)
    
    edges = []
    idx = 3
    for i in range(M):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        deg_L[u] += 1
        deg_R[v] += 1
        edges.append((u, v, i))
    
    D = max(max(deg_L), max(deg_R))
    
    free_L = [set(range(1, deg_L[u] + 1)) for u in range(Nin + 1)]
    free_R = [set(range(1, deg_R[v] + 1)) for v in range(Nout + 1)]
    
    match_L = [{} for _ in range(Nin + 1)]
    match_R = [{} for _ in range(Nout + 1)]
    
    ans = [0] * M
    
    for u, v, e_idx in edges:
        c1 = next(iter(free_L[u]))
        if c1 in free_R[v]:
            free_L[u].remove(c1)
            free_R[v].remove(c1)
            match_L[u][c1] = (v, e_idx)
            match_R[v][c1] = (u, e_idx)
            ans[e_idx] = c1
            continue
        
        c2 = next(iter(free_R[v]))
        if c2 in free_L[u]:
            free_L[u].remove(c2)
            free_R[v].remove(c2)
            match_L[u][c2] = (v, e_idx)
            match_R[v][c2] = (u, e_idx)
            ans[e_idx] = c2
            continue
        
        free_L[u].remove(c1)
        free_R[v].remove(c2)
        
        path = []
        cur_v = v
        while True:
            u1, e1 = match_R[cur_v][c1]
            path.append((u1, cur_v, e1, c1, c2))
            if c2 in match_L[u1]:
                v2, e2 = match_L[u1][c2]
                path.append((u1, v2, e2, c2, c1))
                if c1 in match_R[v2]:
                    cur_v = v2
                else:
                    end_node = v2
                    end_side = 'R'
                    break
            else:
                end_node = u1
                end_side = 'L'
                break
        
        for u_i, v_i, e_i, old_c, new_c in path:
            del match_L[u_i][old_c]
            del match_R[v_i][old_c]
            
        for u_i, v_i, e_i, old_c, new_c in path:
            match_L[u_i][new_c] = (v_i, e_i)
            match_R[v_i][new_c] = (u_i, e_i)
            ans[e_i] = new_c
            
        if end_side == 'L':
            free_L[end_node].remove(c2)
            free_L[end_node].add(c1)
        else:
            free_R[end_node].remove(c1)
            free_R[end_node].add(c2)
            
        match_L[u][c1] = (v, e_idx)
        match_R[v][c1] = (u, e_idx)
        ans[e_idx] = c1

    print("YES")
    print(*(ans))

if __name__ == '__main__':
    solve()