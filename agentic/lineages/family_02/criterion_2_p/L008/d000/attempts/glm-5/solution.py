import sys
sys.setrecursionlimit(300000)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # 2-SAT: variables are relays 1..n
    # For each relay i: node 2*i is False (Mode 0), node 2*i+1 is True (Mode 1)
    # Implication: (a -> b) adds edge a -> b
    
    N = 2 * n + 2
    adj = [[] for _ in range(N)]
    radj = [[] for _ in range(N)]

    def get_node(relay, mode):
        # mode is 0 or 1
        return 2 * relay + mode

    def add_implication(u, v):
        adj[u].append(v)
        radj[v].append(u)

    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        
        # Rule: (target1) OR (target2)
        # target x: positive -> relay |x| is 1; negative -> relay |x| is 0
        r1 = abs(l1)
        m1 = 1 if l1 > 0 else 0
        
        r2 = abs(l2)
        m2 = 1 if l2 > 0 else 0
        
        # Clause (r1=m1) OR (r2=m2)
        # Implications: (r1!=m1) -> (r2=m2)  AND  (r2!=m2) -> (r1=m1)
        # Negation of mode m is 1-m
        
        u = get_node(r1, 1 - m1)
        v = get_node(r2, m2)
        add_implication(u, v)
        
        u = get_node(r2, 1 - m2)
        v = get_node(r1, m1)
        add_implication(u, v)

    # Kosaraju's algorithm to find SCCs
    visited = [False] * N
    order = []
    
    def dfs1(u):
        stack = [(u, 0)]
        while stack:
            node, idx = stack[-1]
            if not visited[node]:
                visited[node] = True
            
            if idx < len(adj[node]):
                child = adj[node][idx]
                stack[-1] = (node, idx + 1)
                if not visited[child]:
                    stack.append((child, 0))
            else:
                stack.pop()
                order.append(node)

    for i in range(2, N):
        if not visited[i]:
            dfs1(i)

    comp = [-1] * N
    current_comp = 0
    
    def dfs2(u, label):
        stack = [u]
        while stack:
            node = stack.pop()
            if comp[node] == -1:
                comp[node] = label
                for v in radj[node]:
                    if comp[v] == -1:
                        stack.append(v)

    for u in reversed(order):
        if comp[u] == -1:
            dfs2(u, current_comp)
            current_comp += 1

    # Check for contradiction and assign values
    res = [0] * (n + 1)
    possible = True
    
    for i in range(1, n + 1):
        node_false = get_node(i, 0)
        node_true = get_node(i, 1)
        
        if comp[node_false] == comp[node_true]:
            possible = False
            break
        
        # If component of True is "greater" (appears later in topological order),
        # it can reach False, so we must pick False.
        # Else we can pick True.
        if comp[node_true] > comp[node_false]:
            res[i] = 1
        else:
            res[i] = 0

    if not possible:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, res[1:])))

if __name__ == '__main__':
    solve()