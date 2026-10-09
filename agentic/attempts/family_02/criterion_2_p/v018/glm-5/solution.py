import sys
sys.setrecursionlimit(1 << 25)

def solve():
    it = iter(sys.stdin.read().split())
    try:
        n = int(next(it))
        m = int(next(it))
    except StopIteration:
        return

    # Build implication graph for 2-SAT
    # Variable x has two nodes: 2*x for False, 2*x+1 for True
    # For clause (a OR b): add edges (~a -> b) and (~b -> a)
    
    N = 2 * n
    adj = [[] for _ in range(N)]
    radj = [[] for _ in range(N)]
    
    edge_counter = 0
    
    for _ in range(m):
        try:
            l1 = int(next(it))
            l2 = int(next(it))
        except StopIteration:
            break
        
        # Convert literal to node index
        # l > 0: switch l should be 1 -> node 2*(l-1)+1
        # l < 0: switch -l should be 0 -> node 2*(-l-1)
        def lit_to_node(l):
            x = abs(l) - 1  # 0-indexed switch
            if l > 0:
                return 2 * x + 1  # True
            else:
                return 2 * x  # False
        
        def neg_node(u):
            return u ^ 1
        
        u = lit_to_node(l1)
        v = lit_to_node(l2)
        
        # (u OR v) --> (~u -> v) and (~v -> u)
        adj[neg_node(u)].append(v)
        adj[neg_node(v)].append(u)
        radj[v].append(neg_node(u))
        radj[u].append(neg_node(v))
        edge_counter += 2
    
    # Kosaraju's algorithm for SCC
    visited = [False] * N
    order = []
    
    def dfs1(u):
        stack = [(u, 0)]
        while stack:
            node, idx = stack[-1]
            if not visited[node]:
                visited[node] = True
            if idx < len(adj[node]):
                neighbor = adj[node][idx]
                stack[-1] = (node, idx + 1)
                if not visited[neighbor]:
                    stack.append((neighbor, 0))
            else:
                stack.pop()
                order.append(node)
    
    for i in range(N):
        if not visited[i]:
            dfs1(i)
    
    comp = [-1] * N
    current_comp = 0
    
    def dfs2(u, c):
        stack = [u]
        comp[u] = c
        while stack:
            node = stack.pop()
            for neighbor in radj[node]:
                if comp[neighbor] == -1:
                    comp[neighbor] = c
                    stack.append(neighbor)
    
    for u in reversed(order):
        if comp[u] == -1:
            dfs2(u, current_comp)
            current_comp += 1
    
    # Check satisfiability: for each variable, True and False must be in different SCCs
    # Also, True must be in a later SCC (topologically)
    assignment = [0] * n
    
    for i in range(n):
        true_node = 2 * i + 1
        false_node = 2 * i
        if comp[true_node] == comp[false_node]:
            print("NO")
            return
        assignment[i] = 1 if comp[true_node] > comp[false_node] else 0
    
    print("YES")
    print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    solve()