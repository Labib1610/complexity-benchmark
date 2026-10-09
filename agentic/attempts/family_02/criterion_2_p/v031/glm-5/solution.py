import sys
sys.setrecursionlimit(300000)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(2 * n)]
    
    for _ in range(m):
        l1 = int(next(it))
        l2 = int(next(it))
        
        u = abs(l1) - 1
        v = abs(l2) - 1
        su = 1 if l1 > 0 else 0
        sv = 1 if l2 > 0 else 0
        
        # Clause (su_u OR sv_v)
        # Implication: not su_u -> sv_v
        # not su_u is (1-su_u)
        from_node = 2 * u + (1 - su)
        to_node = 2 * v + sv
        adj[from_node].append(to_node)
        
        # Implication: not sv_v -> su_u
        from_node = 2 * v + (1 - sv)
        to_node = 2 * u + su
        adj[from_node].append(to_node)
    
    # Kosaraju's algorithm for SCC
    visited = [False] * (2 * n)
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
    
    for i in range(2 * n):
        if not visited[i]:
            dfs1(i)
    
    rev_adj = [[] for _ in range(2 * n)]
    for u in range(2 * n):
        for v in adj[u]:
            rev_adj[v].append(u)
            
    comp_id = [-1] * (2 * n)
    current_comp = 0
    
    def dfs2(u, cid):
        stack = [u]
        comp_id[u] = cid
        while stack:
            node = stack.pop()
            for child in rev_adj[node]:
                if comp_id[child] == -1:
                    comp_id[child] = cid
                    stack.append(child)
    
    for u in reversed(order):
        if comp_id[u] == -1:
            dfs2(u, current_comp)
            current_comp += 1
            
    assignment = [0] * n
    possible = True
    
    for i in range(n):
        node_true = 2 * i + 1
        node_false = 2 * i
        if comp_id[node_true] == comp_id[node_false]:
            possible = False
            break
        assignment[i] = 1 if comp_id[node_true] > comp_id[node_false] else 0
    
    if not possible:
        sys.stdout.write("NO\n")
    else:
        sys.stdout.write("YES\n")
        sys.stdout.write(" ".join(map(str, assignment)) + "\n")

if __name__ == "__main__":
    solve()