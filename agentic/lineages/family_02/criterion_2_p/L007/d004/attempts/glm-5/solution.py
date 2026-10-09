import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    
    adj = [[] for _ in range(2 * n + 1)]
    
    idx = 2
    for _ in range(m):
        l1 = int(data[idx])
        l2 = int(data[idx+1])
        idx += 2
        
        u = abs(l1)
        v = abs(l2)
        sign1 = 1 if l1 > 0 else -1
        sign2 = 1 if l2 > 0 else -1
        
        # I(l1) + I(l2) > 0
        # I(l) = l * (2s_{|l|} - 1) + |l|
        # If s_{|l|} = 0, I(l) = -l + |l| = |l| - l
        # If s_{|l|} = 1, I(l) = l + |l| = |l| + l
        
        # We want to avoid the case where I(l1) + I(l2) <= 0
        # The minimum possible sum is when both are minimized.
        # Min I(l) = |l| - l
        # If Min I(l1) + Min I(l2) > 0, the constraint is always satisfied.
        # Otherwise, we must avoid the combination of assignments that minimizes both.
        
        min1 = u - l1
        min2 = v - l2
        
        if min1 + min2 > 0:
            continue
            
        # The forbidden assignment is s_u = 0 and s_v = 0
        # Implication: s_u = 1 OR s_v = 1
        # 2-SAT clauses: (~s_u -> s_v) and (~s_v -> s_u)
        # Nodes: 1..n for s_i = 1, n+1..2n for s_i = 0
        adj[u + n].append(v)
        adj[v + n].append(u)
        
    # Kosaraju's algorithm to find SCCs
    sys.setrecursionlimit(3000000)
    visited = [False] * (2 * n + 1)
    order = []
    
    def dfs1(u):
        stack = [(u, 0)]
        while stack:
            node, i = stack[-1]
            if i == 0:
                visited[node] = True
            if i < len(adj[node]):
                stack[-1] = (node, i + 1)
                v = adj[node][i]
                if not visited[v]:
                    stack.append((v, 0))
            else:
                stack.pop()
                order.append(node)
                
    for i in range(1, 2 * n + 1):
        if not visited[i]:
            dfs1(i)
            
    adj_rev = [[] for _ in range(2 * n + 1)]
    for u in range(1, 2 * n + 1):
        for v in adj[u]:
            adj_rev[v].append(u)
            
    comp_id = [0] * (2 * n + 1)
    c = 0
    
    def dfs2(u, c):
        stack = [u]
        comp_id[u] = c
        while stack:
            node = stack[-1]
            if adj_rev[node]:
                v = adj_rev[node].pop()
                if comp_id[v] == 0:
                    comp_id[v] = c
                    stack.append(v)
            else:
                stack.pop()
                
    for u in reversed(order):
        if comp_id[u] == 0:
            c += 1
            dfs2(u, c)
            
    for i in range(1, n + 1):
        if comp_id[i] == comp_id[i + n]:
            print("NO")
            return
            
    # Topological order of SCCs is given by c (since we process in reverse finish order)
    # We want to assign s_i = 1 if comp_id[i] > comp_id[i + n]
    ans = [0] * n
    for i in range(1, n + 1):
        if comp_id[i] > comp_id[i + n]:
            ans[i - 1] = 1
            
    print("YES")
    print(" ".join(map(str, ans)))

if __name__ == '__main__':
    solve()