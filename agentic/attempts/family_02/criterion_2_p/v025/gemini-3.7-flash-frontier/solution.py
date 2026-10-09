import sys

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    
    adj = [[] for _ in range(2 * n)]
    
    def get_lit(c):
        if c > 0:
            return 2 * (c - 1)
        else:
            return 2 * (-c - 1) + 1
            
    def get_neg(lit):
        return lit ^ 1

    idx = 2
    for _ in range(m):
        c1 = int(data[idx])
        c2 = int(data[idx + 1])
        idx += 2
        
        u = get_lit(c1)
        v = get_lit(c2)
        
        # u or v => (~u -> v) and (~v -> u)
        adj[get_neg(u)].append(v)
        adj[get_neg(v)].append(u)
        
    num_nodes = 2 * n
    dfn = [-1] * num_nodes
    low = [-1] * num_nodes
    in_stack = [False] * num_nodes
    st = []
    scc = [-1] * num_nodes
    scc_cnt = 0
    timer = 0
    
    for i in range(num_nodes):
        if dfn[i] != -1:
            continue
        call_stack = [(i, 0)]
        dfn[i] = low[i] = timer
        timer += 1
        st.append(i)
        in_stack[i] = True
        
        while call_stack:
            u, edge_idx = call_stack[-1]
            if edge_idx < len(adj[u]):
                v = adj[u][edge_idx]
                call_stack[-1] = (u, edge_idx + 1)
                if dfn[v] == -1:
                    dfn[v] = low[v] = timer
                    timer += 1
                    st.append(v)
                    in_stack[v] = True
                    call_stack.append((v, 0))
                elif in_stack[v]:
                    low[u] = min(low[u], dfn[v])
            else:
                call_stack.pop()
                if call_stack:
                    p = call_stack[-1][0]
                    low[p] = min(low[p], low[u])
                if low[u] == dfn[u]:
                    while True:
                        v = st.pop()
                        in_stack[v] = False
                        scc[v] = scc_cnt
                        if v == u:
                            break
                    scc_cnt += 1
                    
    ans = [0] * n
    for i in range(n):
        pos = 2 * i
        neg = 2 * i + 1
        if scc[pos] == scc[neg]:
            print("NO")
            return
        # If pos has smaller SCC id, it is closer to sink in condensation graph => True
        if scc[pos] < scc[neg]:
            ans[i] = 1
        else:
            ans[i] = 0
            
    print("YES")
    print(" ".join(map(str, ans)))

if __name__ == '__main__':
    main()