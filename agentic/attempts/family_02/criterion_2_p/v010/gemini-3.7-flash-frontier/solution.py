import sys

def solve():
    sys.setrecursionlimit(500000)
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    
    adj = [[] for _ in range(2 * n)]
    
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        idx += 2
        
        # u: positive -> 2*(u-1), negative -> 2*(|u|-1) + 1
        node_u = 2 * (u - 1) if u > 0 else 2 * (-u - 1) + 1
        node_v = 2 * (v - 1) if v > 0 else 2 * (-v - 1) + 1
        
        neg_u = node_u ^ 1
        neg_v = node_v ^ 1
        
        # (u or v) <=> (~u -> v) and (~v -> u)
        adj[neg_u].append(node_v)
        adj[neg_v].append(node_u)
        
    num_nodes = 2 * n
    dfn = [-1] * num_nodes
    low = [-1] * num_nodes
    scc = [-1] * num_nodes
    in_stack = [False] * num_nodes
    stack = []
    timer = 0
    scc_cnt = 0
    
    for i in range(num_nodes):
        if dfn[i] == -1:
            call_stack = [(i, 0)]
            while call_stack:
                u, edge_idx = call_stack.pop()
                if edge_idx == 0:
                    dfn[u] = low[u] = timer
                    timer += 1
                    stack.append(u)
                    in_stack[u] = True
                
                advanced = False
                while edge_idx < len(adj[u]):
                    v = adj[u][edge_idx]
                    edge_idx += 1
                    if dfn[v] == -1:
                        call_stack.append((u, edge_idx))
                        call_stack.append((v, 0))
                        advanced = True
                        break
                    elif in_stack[v]:
                        low[u] = min(low[u], dfn[v])
                
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
                
                if call_stack:
                    p = call_stack[-1][0]
                    low[p] = min(low[p], low[u])

    ans = []
    for i in range(n):
        if scc[2 * i] == scc[2 * i + 1]:
            print("NO")
            return
        if scc[2 * i] < scc[2 * i + 1]:
            ans.append(1)
        else:
            ans.append(0)
            
    print("YES")
    print(*(ans))

if __name__ == '__main__':
    solve()