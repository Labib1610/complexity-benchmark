import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    nL = int(input_data[0])
    nR = int(input_data[1])
    m = int(input_data[2])
    
    if m == 0:
        print("YES")
        print("")
        return
        
    edges = []
    for i in range(m):
        u = int(input_data[3 + 2*i])
        v = int(input_data[3 + 2*i + 1])
        edges.append((u, v))
        
    deg_L = [0] * (nL + 1)
    deg_R = [0] * (nR + 1)
    
    for u, v in edges:
        deg_L[u] += 1
        deg_R[v] += 1
        
    Delta = max(max(deg_L), max(deg_R))
    
    if Delta == 0:
        print("YES")
        print("")
        return
        
    adj_L = [[] for _ in range(nL + 1)]
    adj_R = [[] for _ in range(nR + 1)]
    
    for i, (u, v) in enumerate(edges):
        adj_L[u].append((v, i))
        adj_R[v].append((u, i))
        
    match_L = [-1] * (nL + 1)
    match_R = [-1] * (nR + 1)
    
    for d in range(1, Delta + 1):
        for u in range(1, nL + 1):
            if match_L[u] == -1:
                visited = [False] * (nR + 1)
                stack = [(u, 0)]
                path_v = [-1] * (nR + 1)
                path_u = [-1] * (nR + 1)
                found = False
                
                while stack:
                    curr, state = stack.pop()
                    if state == 0:
                        for v, edge_idx in adj_L[curr]:
                            if not visited[v]:
                                visited[v] = True
                                path_v[v] = curr
                                path_u[v] = edge_idx
                                if match_R[v] == -1:
                                    cv = v
                                    while cv != -1:
                                        cu = path_v[cv]
                                        e_idx = path_u[cv]
                                        prev_match = match_L[cu]
                                        match_L[cu] = cv
                                        match_R[cv] = cu
                                        cv = prev_match
                                    found = True
                                    break
                                else:
                                    stack.append((match_R[v], 0))
                        if found:
                            break
                    # state 1 is not needed since we don't backtrack and reset visited
                    
                if not found:
                    # This should theoretically never happen due to the bipartite graph properties
                    pass
                    
    ans = [0] * m
    for u in range(1, nL + 1):
        if match_L[u] != -1:
            for v, edge_idx in adj_L[u]:
                if v == match_L[u]:
                    ans[edge_idx] = 1
                    break
                    
    for d in range(2, Delta + 1):
        for v in range(1, nR + 1):
            if match_R[v] != -1:
                u = match_R[v]
                match_L[u] = -1
                match_R[v] = -1
                
        for u in range(1, nL + 1):
            if match_L[u] == -1:
                visited = [False] * (nR + 1)
                stack = [(u, 0)]
                path_v = [-1] * (nR + 1)
                path_u = [-1] * (nR + 1)
                found = False
                
                while stack:
                    curr, state = stack.pop()
                    if state == 0:
                        for v, edge_idx in adj_L[curr]:
                            if not visited[v]:
                                visited[v] = True
                                path_v[v] = curr
                                path_u[v] = edge_idx
                                if match_R[v] == -1:
                                    cv = v
                                    while cv != -1:
                                        cu = path_v[cv]
                                        e_idx = path_u[cv]
                                        prev_match = match_L[cu]
                                        match_L[cu] = cv
                                        match_R[cv] = cu
                                        cv = prev_match
                                    found = True
                                    break
                                else:
                                    stack.append((match_R[v], 0))
                        if found:
                            break
                            
        for u in range(1, nL + 1):
            if match_L[u] != -1:
                for v, edge_idx in adj_L[u]:
                    if v == match_L[u]:
                        ans[edge_idx] = d
                        break
                        
    print("YES")
    print(" ".join(map(str, ans)))

if __name__ == '__main__':
    solve()