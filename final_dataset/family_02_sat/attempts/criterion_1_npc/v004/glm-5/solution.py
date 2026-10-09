import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    
    # 2-SAT setup
    # Variable i (1-based) corresponds to:
    # True: 2*i
    # False: 2*i + 1
    N = 2 * (n + 1)
    adj = [[] for _ in range(N)]
    radj = [[] for _ in range(N)]
    
    idx = 2
    for _ in range(m):
        l1 = int(input_data[idx])
        l2 = int(input_data[idx+1])
        l3 = int(input_data[idx+2])
        idx += 3
        
        # For a clause (a OR b OR c), we add implications:
        # ~a -> b, ~b -> a, ~a -> c, ~c -> a, ~b -> c, ~c -> b
        # We represent x as 2*|x| if x > 0, and 2*|x|+1 if x < 0
        # We represent ~x as 2*|x|+1 if x > 0, and 2*|x| if x < 0
        
        def get_node(x):
            if x > 0:
                return 2 * x
            else:
                return 2 * (-x) + 1
                
        def get_neg(x):
            if x > 0:
                return 2 * x + 1
            else:
                return 2 * (-x)
        
        a, b, c = l1, l2, l3
        na, nb, nc = get_neg(a), get_neg(b), get_neg(c)
        va, vb, vc = get_node(a), get_node(b), get_node(c)
        
        adj[na].append(vb)
        adj[nb].append(va)
        adj[na].append(vc)
        adj[nc].append(va)
        adj[nb].append(vc)
        adj[nc].append(vb)
        
        radj[vb].append(na)
        radj[va].append(nb)
        radj[vc].append(na)
        radj[va].append(nc)
        radj[vc].append(nb)
        radj[vb].append(nc)

    # Kosaraju's algorithm to find Strongly Connected Components
    visited = [False] * N
    order = []
    
    def dfs1(u):
        stack = [(u, 0)]
        while stack:
            node, i = stack[-1]
            if not visited[node]:
                visited[node] = True
            if i < len(adj[node]):
                stack[-1] = (node, i + 1)
                neighbor = adj[node][i]
                if not visited[neighbor]:
                    stack.append((neighbor, 0))
            else:
                stack.pop()
                order.append(node)
                
    for i in range(2, N):
        if not visited[i]:
            dfs1(i)
            
    comp_id = [-1] * N
    c = 0
    
    def dfs2(u, c):
        stack = [u]
        while stack:
            node = stack[-1]
            if comp_id[node] == -1:
                comp_id[node] = c
                for neighbor in radj[node]:
                    if comp_id[neighbor] == -1:
                        stack.append(neighbor)
                        break
            else:
                stack.pop()

    for u in reversed(order):
        if comp_id[u] == -1:
            dfs2(u, c)
            c += 1
            
    # Check for unsatisfiability
    for i in range(1, n + 1):
        if comp_id[2 * i] == comp_id[2 * i + 1]:
            print("NO")
            return
            
    # Topological order of components is given by c - comp_id
    # Assign values based on component order
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        if comp_id[2 * i] > comp_id[2 * i + 1]:
            ans[i] = 1
        else:
            ans[i] = 0
            
    print("YES")
    print(" ".join(map(str, ans[1:])))

if __name__ == '__main__':
    solve()