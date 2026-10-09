import sys

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    
    num_nodes = 2 * n
    adj = [[] for _ in range(num_nodes)]
    
    idx = 2
    for _ in range(m):
        l1 = int(data[idx])
        l2 = int(data[idx+1])
        idx += 2
        
        u = (l1 - 1) * 2 if l1 > 0 else (-l1 - 1) * 2 + 1
        v = (l2 - 1) * 2 if l2 > 0 else (-l2 - 1) * 2 + 1
        
        # (~u -> v) and (~v -> u)
        adj[u ^ 1].append(v)
        adj[v ^ 1].append(u)
        
    # Tarjan's SCC iterative
    dfn = [-1] * num_nodes
    low = [-1] * num_nodes
    scc = [-1] * num_nodes
    in_stack = [False] * num_nodes
    stack = []
    
    timer = 0
    scc_cnt = 0
    
    for i in range(num_nodes):
        if dfn[i] != -1:
            continue
        
        call_stack = [(i, 0)]
        dfn[i] = low[i] = timer
        timer += 1
        stack.append(i)
        in_stack[i] = True
        
        while call_stack:
            u, edge_idx = call_stack[-1]
            
            if edge_idx < len(adj[u]):
                v = adj[u][edge_idx]
                call_stack[-1] = (u, edge_idx + 1)
                
                if dfn[v] == -1:
                    dfn[v] = low[v] = timer
                    timer += 1
                    stack.append(v)
                    in_stack[v] = True
                    call_stack.append((v, 0))
                elif in_stack[v]:
                    if dfn[v] < low[u]:
                        low[u] = dfn[v]
            else:
                call_stack.pop()
                if call_stack:
                    p = call_stack[-1][0]
                    if low[u] < low[p]:
                        low[p] = low[u]
                        
                if low[u] == dfn[u]:
                    while True:
                        v = stack.pop()
                        in_stack[v] = False
                        scc[v] = scc_cnt
                        if v == u:
                            break
                    scc_cnt += 1

    ans = []
    for i in range(n):
        if scc[2 * i] == scc[2 * i + 1]:
            print("NO")
            return
        ans.append(1 if scc[2 * i] < scc[2 * i + 1] else 0)
        
    print("YES")
    print(*(ans))

if __name__ == '__main__':
    main()