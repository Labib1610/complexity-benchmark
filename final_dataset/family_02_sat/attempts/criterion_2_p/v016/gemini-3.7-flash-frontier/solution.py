import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    
    # Map literal to node index:
    # If literal x > 0: x is variable x, node = 2 * (x - 1)
    # If literal x < 0: not variable |x|, node = 2 * (|x| - 1) + 1
    # Negation of node u is u ^ 1.
    def lit_to_node(x):
        if x > 0:
            return 2 * (x - 1)
        else:
            return 2 * (-x - 1) + 1

    num_nodes = 2 * n
    adj = [[] for _ in range(num_nodes)]
    rev_adj = [[] for _ in range(num_nodes)]
    
    idx = 2
    for _ in range(m):
        c1 = int(data[idx])
        c2 = int(data[idx+1])
        idx += 2
        
        u = lit_to_node(c1)
        v = lit_to_node(c2)
        
        # (c1 or c2) <=> (not c1 => c2) and (not c2 => c1)
        not_u = u ^ 1
        not_v = v ^ 1
        
        adj[not_u].append(v)
        adj[not_v].append(u)
        rev_adj[v].append(not_u)
        rev_adj[u].append(not_v)
        
    # Kosaraju's algorithm
    order = []
    visited = [False] * num_nodes
    
    for i in range(num_nodes):
        if not visited[i]:
            stack = [i]
            visited[i] = True
            it = [0] * num_nodes
            while stack:
                u = stack[-1]
                if it[u] < len(adj[u]):
                    v = adj[u][it[u]]
                    it[u] += 1
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
                else:
                    stack.pop()
                    order.append(u)
                    
    scc = [-1] * num_nodes
    scc_count = 0
    
    for i in reversed(order):
        if scc[i] == -1:
            stack = [i]
            scc[i] = scc_count
            while stack:
                u = stack.pop()
                for v in rev_adj[u]:
                    if scc[v] == -1:
                        scc[v] = scc_count
                        stack.append(v)
            scc_count += 1
            
    res = [0] * n
    for i in range(n):
        pos_node = 2 * i
        neg_node = 2 * i + 1
        if scc[pos_node] == scc[neg_node]:
            print("NO")
            return
        # In Kosaraju on rev_adj, components are numbered in topological order of SCC DAG
        # An implication u => v means scc[u] <= scc[v].
        # If scc[pos_node] > scc[neg_node], pos is reachable from neg, so pos must be true.
        if scc[pos_node] > scc[neg_node]:
            res[i] = 1
        else:
            res[i] = 0
            
    print("YES")
    print(*(res))

if __name__ == '__main__':
    solve()