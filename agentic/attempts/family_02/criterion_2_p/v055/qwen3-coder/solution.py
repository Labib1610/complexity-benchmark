import sys
from collections import defaultdict

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["0"] * n))
        return
    
    # For each variable x_i, we'll have two nodes: i*2 (for x_i = 0) and i*2+1 (for x_i = 1)
    # But it's easier to work with implications.
    # We reduce to 2-SAT.
    
    # For each clause (l1 OR l2), we add edges:
    # (~l1 -> l2) and (~l2 -> l1)
    
    adj = defaultdict(list)
    rev_adj = defaultdict(list)
    
    def var_to_node(x):
        # x is +i or -i
        # node id: (i-1)*2 for x_i = 0, (i-1)*2+1 for x_i = 1
        if x > 0:
            return (x - 1) * 2 + 1  # x_i = 1
        else:
            return (-x - 1) * 2     # x_i = 0
            
    def neg_node(u):
        # 0 -> 1, 1 -> 0, 2 -> 3, 3 -> 2, etc.
        if u % 2 == 0:
            return u + 1
        else:
            return u - 1
            
    for _ in range(m):
        l1, l2 = map(int, sys.stdin.readline().split())
        # Clause: l1 OR l2
        # This is equivalent to (~l1 -> l2) AND (~l2 -> l1)
        
        n1 = var_to_node(l1)
        n2 = var_to_node(l2)
        
        adj[neg_node(n1)].append(n2)
        adj[neg_node(n2)].append(n1)
        
        rev_adj[n2].append(neg_node(n1))
        rev_adj[n1].append(neg_node(n2))
    
    # Now run Kosaraju's algorithm to find strongly connected components
    order = []
    visited = [False] * (2 * n)
    
    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
        
    for i in range(2 * n):
        if not visited[i]:
            dfs1(i)
            
    # Second DFS on transpose graph
    comp = [-1] * (2 * n)
    cnt = 0
    
    def dfs2(u, c):
        comp[u] = c
        for v in rev_adj[u]:
            if comp[v] == -1:
                dfs2(v, c)
                
    for u in reversed(order):
        if comp[u] == -1:
            dfs2(u, cnt)
            cnt += 1
            
    # Check for contradictions
    for i in range(n):
        node_false = i * 2
        node_true = i * 2 + 1
        if comp[node_false] == comp[node_true]:
            print("NO")
            return
            
    # Assign values based on component numbers
    # Component with higher number was finished later in dfs1, so should be true
    result = [0] * n
    for i in range(n):
        node_false = i * 2
        node_true = i * 2 + 1
        if comp[node_true] > comp[node_false]:
            result[i] = 1
        else:
            result[i] = 0
            
    print("YES")
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()