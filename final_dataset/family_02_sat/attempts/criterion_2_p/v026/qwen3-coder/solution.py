import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m = map(int, sys.stdin.readline().split())
    
    # For each variable x (1 to n):
    # node 2*x represents x = False (standby = 0)
    # node 2*x + 1 represents x = True (active = 1)
    # So for literal l:
    # if l > 0: node = 2*l + 1
    # if l < 0: node = 2*abs(l)
    
    def literal_to_node(l):
        if l > 0:
            return 2 * l + 1
        else:
            return 2 * (-l)
    
    def node_to_literal(node):
        if node % 2 == 1:
            return (node - 1) // 2
        else:
            return -(node // 2)
    
    # Build implication graph
    # Total nodes: 0 to 2*n+1
    adj = [[] for _ in range(2 * (n + 1))]
    rev_adj = [[] for _ in range(2 * (n + 1))]
    
    for _ in range(m):
        l1, l2 = map(int, sys.stdin.readline().split())
        # clause (l1 OR l2) is equivalent to (~l1 -> l2) AND (~l2 -> l1)
        node1 = literal_to_node(l1)
        node2 = literal_to_node(l2)
        not_node1 = node1 ^ 1
        not_node2 = node2 ^ 1
        
        adj[not_node1].append(node2)
        adj[not_node2].append(node1)
        rev_adj[node2].append(not_node1)
        rev_adj[node1].append(not_node2)
    
    # Kosaraju's algorithm for SCC
    visited = [False] * (2 * (n + 1))
    order = []
    
    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
    
    for i in range(2, 2 * n + 2):
        if not visited[i]:
            dfs1(i)
    
    visited = [False] * (2 * (n + 1))
    scc_id = [-1] * (2 * (n + 1))
    scc_count = 0
    
    def dfs2(u):
        visited[u] = True
        scc_id[u] = scc_count
        for v in rev_adj[u]:
            if not visited[v]:
                dfs2(v)
    
    while order:
        u = order.pop()
        if not visited[u]:
            dfs2(u)
            scc_count += 1
    
    # Check if satisfiable
    for i in range(1, n + 1):
        node_true = 2 * i + 1
        node_false = 2 * i
        if scc_id[node_true] == scc_id[node_false]:
            print("NO")
            return
    
    # Extract solution
    print("YES")
    assignment = [0] * (n + 1)
    
    # Process SCCs in reverse topological order
    for i in range(1, n + 1):
        node_true = 2 * i + 1
        node_false = 2 * i
        if scc_id[node_true] > scc_id[node_false]:
            assignment[i] = 1
        else:
            assignment[i] = 0
    
    print(' '.join(map(str, assignment[1:])))

threading.Thread(target=main).start()