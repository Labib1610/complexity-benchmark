import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    num_vars = n
    num_nodes = 2 * num_vars
    
    adj = [[] for _ in range(num_nodes)]
    
    def to_node(lit):
        if lit > 0:
            return 2 * (lit - 1)
        else:
            return 2 * (-lit - 1) + 1
    
    def neg(node):
        return node ^ 1

    idx = 2
    for _ in range(m):
        l1 = int(input_data[idx])
        l2 = int(input_data[idx + 1])
        idx += 2
        
        u = to_node(l1)
        v = to_node(l2)
        
        # (u or v) <=> (not u -> v) and (not v -> u)
        adj[neg(u)].append(v)
        adj[neg(v)].append(u)
        
    # Tarjan's SCC algorithm (iterative)
    dfn = [-1] * num_nodes
    low = [-1] * num_nodes
    in_stack = [False] * num_nodes
    stack = []
    scc = [-1] * num_nodes
    scc_cnt = 0
    timer = 0
    
    for i in range(num_nodes):
        if dfn[i] != -1:
            continue
        
        # Iterative DFS
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
        pos_node = 2 * i
        neg_node = 2 * i + 1
        if scc[pos_node] == scc[neg_node]:
            print("NO")
            return
        if scc[pos_node] < scc[neg_node]:
            ans.append("1")
        else:
            ans.append("0")
            
    print("YES")
    print(" ".join(ans))

if __name__ == '__main__':
    solve()