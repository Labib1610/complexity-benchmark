import sys

# Increase recursion depth just in case, but iterative is safer
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # 2-SAT Graph construction
    # For variable i (0 to n-1):
    # 2*i: False, 2*i + 1: True
    # negation of u is u ^ 1
    
    adj = [[] for _ in range(2 * n)]
    
    idx = 2
    for _ in range(m):
        l1 = int(input_data[idx])
        l2 = int(input_data[idx+1])
        idx += 2
        
        # Convert literal to node
        u = (l1 - 1) * 2 + 1 if l1 > 0 else (-l1 - 1) * 2
        v = (l2 - 1) * 2 + 1 if l2 > 0 else (-l2 - 1) * 2
        
        # (u or v) <=> (not u -> v) and (not v -> u)
        adj[u ^ 1].append(v)
        adj[v ^ 1].append(u)
        
    num_nodes = 2 * n
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
        while call_stack:
            u, edge_idx = call_stack[-1]
            
            if edge_idx == 0:
                dfn[u] = low[u] = timer
                timer += 1
                stack.append(u)
                in_stack[u] = True
            
            advanced = False
            for j in range(edge_idx, len(adj[u])):
                v = adj[u][j]
                if dfn[v] == -1:
                    call_stack[-1] = (u, j + 1)
                    call_stack.append((v, 0))
                    advanced = True
                    break
                elif in_stack[v]:
                    if dfn[v] < low[u]:
                        low[u] = dfn[v]
            
            if advanced:
                continue
                
            if low[u] == dfn[u]:
                while True:
                    node = stack.pop()
                    in_stack[node] = False
                    scc[node] = scc_cnt
                    if node == u:
                        break
                scc_cnt += 1
            
            call_stack.pop()
            if call_stack:
                p, _ = call_stack[-1]
                if low[u] < low[p]:
                    low[p] = low[u]

    ans = [0] * n
    for i in range(n):
        if scc[2 * i] == scc[2 * i + 1]:
            print("NO")
            return
        ans[i] = 1 if scc[2 * i + 1] < scc[2 * i] else 0
        
    print("YES")
    print(*(ans))

if __name__ == '__main__':
    solve()