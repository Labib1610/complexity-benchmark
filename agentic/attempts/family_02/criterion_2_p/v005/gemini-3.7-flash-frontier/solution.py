import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Literals: for variable x (1-based):
    # +x -> 2*(x-1)
    # -x -> 2*(x-1) + 1
    # negation of lit is lit ^ 1
    
    num_nodes = 2 * n
    adj = [[] for _ in range(num_nodes)]
    rev_adj = [[] for _ in range(num_nodes)]
    
    idx = 2
    for _ in range(m):
        u_val = int(input_data[idx])
        v_val = int(input_data[idx+1])
        idx += 2
        
        u_lit = 2 * (abs(u_val) - 1) + (1 if u_val < 0 else 0)
        v_lit = 2 * (abs(v_val) - 1) + (1 if v_val < 0 else 0)
        
        # u or v <=> (not u -> v) and (not v -> u)
        not_u = u_lit ^ 1
        not_v = v_lit ^ 1
        
        adj[not_u].append(v_lit)
        rev_adj[v_lit].append(not_u)
        
        adj[not_v].append(u_lit)
        rev_adj[u_lit].append(not_v)
        
    # Kosaraju's algorithm
    visited = [False] * num_nodes
    order = []
    
    for i in range(num_nodes):
        if not visited[i]:
            stack = [i]
            visited[i] = True
            it_stack = [0]
            while stack:
                u = stack[-1]
                it = it_stack[-1]
                if it < len(adj[u]):
                    v = adj[u][it]
                    it_stack[-1] += 1
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
                        it_stack.append(0)
                else:
                    order.append(u)
                    stack.pop()
                    it_stack.pop()
                    
    comp = [-1] * num_nodes
    comp_id = 0
    
    for i in reversed(order):
        if comp[i] == -1:
            stack = [i]
            comp[i] = comp_id
            while stack:
                u = stack.pop()
                for v in rev_adj[u]:
                    if comp[v] == -1:
                        comp[v] = comp_id
                        stack.append(v)
            comp_id += 1
            
    ans = [0] * n
    for i in range(n):
        pos = 2 * i
        neg = 2 * i + 1
        if comp[pos] == comp[neg]:
            print("NO")
            return
        ans[i] = 1 if comp[pos] < comp[neg] else 0
        
    print("YES")
    print(*(ans))

if __name__ == '__main__':
    solve()