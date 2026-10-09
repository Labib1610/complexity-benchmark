import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m = map(int, sys.stdin.readline().split())
    
    # For each variable x, we have two nodes: x (positive) and x + n (negative)
    # This is a standard 2-SAT transformation
    adj = [[] for _ in range(2 * n + 2)]  # 1-indexed, so 0 unused, 1..n positive, n+1..2n negative
    rev_adj = [[] for _ in range(2 * n + 2)]
    
    for _ in range(m):
        l1, l2 = map(int, sys.stdin.readline().split())
        # clause (l1 OR l2) is equivalent to (NOT l1 -> l2) AND (NOT l2 -> l1)
        # Convert to 0-indexed for internal processing, then back to 1-indexed for graph
        # If l1 is positive (1 to n), NOT l1 is l1 + n
        # If l1 is negative (-1 to -n), NOT l1 is -l1
        # Same for l2
        
        # First implication: NOT l1 -> l2
        if l1 > 0:
            # NOT (var l1) -> (var l2)
            # (l1 + n) -> l2
            from_node = l1 + n
        else:
            # NOT (NOT var |l1|) -> (var l2)
            # |l1| -> l2
            from_node = -l1
        
        if l2 > 0:
            to_node = l2
        else:
            to_node = -l2 + n
            
        adj[from_node].append(to_node)
        rev_adj[to_node].append(from_node)
        
        # Second implication: NOT l2 -> l1
        if l2 > 0:
            from_node = l2 + n
        else:
            from_node = -l2
            
        if l1 > 0:
            to_node = l1
        else:
            to_node = -l1 + n
            
        adj[from_node].append(to_node)
        rev_adj[to_node].append(from_node)
    
    # Kosaraju's algorithm for SCC
    visited = [False] * (2 * n + 2)
    order = []
    
    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
    
    for i in range(1, 2 * n + 1):
        if not visited[i]:
            dfs1(i)
    
    # Reverse graph DFS
    visited = [False] * (2 * n + 2)
    scc_id = [0] * (2 * n + 2)
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
            scc_count += 1
            dfs2(u)
    
    # Check if satisfiable
    for i in range(1, n + 1):
        if scc_id[i] == scc_id[i + n]:
            print("NO")
            return
    
    # Assign values
    assignment = [0] * (n + 1)
    # Process SCCs in reverse topological order
    # We can do this by processing nodes in order of decreasing scc_id
    # But since we just need a valid assignment, we can use the fact that
    # if scc_id[i] > scc_id[i+n], then x_i should be False
    # if scc_id[i] < scc_id[i+n], then x_i should be True
    
    for i in range(1, n + 1):
        if scc_id[i] > scc_id[i + n]:
            assignment[i] = 0
        else:
            assignment[i] = 1
    
    print("YES")
    print(' '.join(map(str, assignment[1:])))

threading.Thread(target=main).start()