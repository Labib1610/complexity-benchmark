import sys

# Increase recursion depth for deep DFS
sys.setrecursionlimit(500000)

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # 2n nodes:
    # For variable x (1-indexed):
    # positive x (x is 1) -> 2*(x-1)
    # negative x (x is 0) -> 2*(x-1) + 1
    
    num_nodes = 2 * n
    adj = [[] for _ in range(num_nodes)]
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        
        # u is literal 1, v is literal 2
        # (u or v) is equivalent to:
        # not u -> v
        # not v -> u
        
        if u > 0:
            pos_u = 2 * (u - 1)
            neg_u = 2 * (u - 1) + 1
        else:
            pos_u = 2 * (-u - 1) + 1
            neg_u = 2 * (-u - 1)
            
        if v > 0:
            pos_v = 2 * (v - 1)
            neg_v = 2 * (v - 1) + 1
        else:
            pos_v = 2 * (-v - 1) + 1
            neg_v = 2 * (-v - 1)
            
        adj[neg_u].append(pos_v)
        adj[neg_v].append(pos_u)
        
    # Tarjan's SCC algorithm
    dfn = [-1] * num_nodes
    low = [-1] * num_nodes
    scc_id = [-1] * num_nodes
    in_stack = [False] * num_nodes
    stack = []
    timer = 0
    scc_cnt = 0
    
    for i in range(num_nodes):
        if dfn[i] != -1:
            continue
        
        # Iterative or recursive DFS
        # Let's do standard recursion
        def dfs(u):
            nonlocal timer, scc_cnt
            dfn[u] = low[u] = timer
            timer += 1
            stack.append(u)
            in_stack[u] = True
            
            for v in adj[u]:
                if dfn[v] == -1:
                    dfs(v)
                    low[u] = min(low[u], low[v])
                elif in_stack[v]:
                    low[u] = min(low[u], dfn[v])
                    
            if low[u] == dfn[u]:
                while True:
                    v = stack.pop()
                    in_stack[v] = False
                    scc_id[v] = scc_cnt
                    if v == u:
                        break
                scc_cnt += 1
                
        dfs(i)
        
    ans = [0] * n
    for i in range(n):
        pos_node = 2 * i
        neg_node = 2 * i + 1
        if scc_id[pos_node] == scc_id[neg_node]:
            print("NO")
            return
        # If scc_id[pos_node] < scc_id[neg_node], pos_node is in a later SCC in topological order
        # which means pos_node is reached from neg_node, so pos_node should be true.
        if scc_id[pos_node] < scc_id[neg_node]:
            ans[i] = 1
        else:
            ans[i] = 0
            
    print("YES")
    print(*(ans))

if __name__ == '__main__':
    solve()