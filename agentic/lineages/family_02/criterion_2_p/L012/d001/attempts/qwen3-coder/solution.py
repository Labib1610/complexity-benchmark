import sys
sys.setrecursionlimit(1000000)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    clauses = []
    index = 2
    for _ in range(m):
        l1 = int(data[index])
        l2 = int(data[index+1])
        clauses.append((l1, l2))
        index += 2
    
    # Build implication graph for 2-SAT
    # Variables: 1 to n (positive), -1 to -n (negative)
    # Nodes: 0 to 2n-1
    # node 2*i represents variable i+1 being false
    # node 2*i+1 represents variable i+1 being true
    
    adj = [[] for _ in range(2 * n)]
    adj_rev = [[] for _ in range(2 * n)]
    
    for (l1, l2) in clauses:
        # Convert literals to node indices
        # l1 OR l2 is equivalent to (NOT l1 -> l2) AND (NOT l2 -> l1)
        # l1 is positive literal x: NOT l1 is (x is false) = node 2*(x-1)
        # l1 is negative literal -x: NOT l1 is (-x is false) = (x is true) = node 2*(x-1)+1
        # l2 is positive literal y: l2 is (y is true) = node 2*(y-1)+1
        # l2 is negative literal -y: l2 is (-y is true) = (y is false) = node 2*(y-1)
        
        # For l1 OR l2:
        # NOT l1 -> l2
        # NOT l2 -> l1
        
        # Convert l1
        if l1 > 0:
            x = l1 - 1
            not_l1_node = 2 * x      # x is false
            l2_node = 2 * (abs(l2) - 1) + (1 if l2 > 0 else 0)  # l2 is true
        else:
            x = -l1 - 1
            not_l1_node = 2 * x + 1  # x is true
            l2_node = 2 * (abs(l2) - 1) + (1 if l2 > 0 else 0)
            
        # Convert l2
        if l2 > 0:
            y = l2 - 1
            not_l2_node = 2 * y      # y is false
            l1_node = 2 * (abs(l1) - 1) + (1 if l1 > 0 else 0)
        else:
            y = -l2 - 1
            not_l2_node = 2 * y + 1  # y is true
            l1_node = 2 * (abs(l1) - 1) + (1 if l1 > 0 else 0)
            
        adj[not_l1_node].append(l2_node)
        adj[not_l2_node].append(l1_node)
        adj_rev[l2_node].append(not_l1_node)
        adj_rev[l1_node].append(not_l2_node)
    
    # Kosaraju's algorithm for SCC
    visited = [False] * (2 * n)
    order = []
    
    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
    
    for i in range(2 * n):
        if not visited[i]:
            dfs1(i)
    
    # Reverse graph DFS
    visited = [False] * (2 * n)
    scc_id = [-1] * (2 * n)
    scc_count = 0
    
    def dfs2(u):
        visited[u] = True
        scc_id[u] = scc_count
        for v in adj_rev[u]:
            if not visited[v]:
                dfs2(v)
    
    while order:
        u = order.pop()
        if not visited[u]:
            dfs2(u)
            scc_count += 1
    
    # Check if satisfiable
    for i in range(n):
        # Variable i+1: nodes 2*i (false) and 2*i+1 (true)
        if scc_id[2*i] == scc_id[2*i+1]:
            print("NO")
            return
    
    # Build assignment
    assignment = [False] * n
    # Process SCCs in reverse topological order
    # Since we used Kosaraju, SCC ids are in reverse topological order
    for i in range(n):
        false_node = 2 * i
        true_node = 2 * i + 1
        # The one with higher SCC id comes first in topological order
        if scc_id[false_node] > scc_id[true_node]:
            assignment[i] = False  # False comes first, so we set it to false
        else:
            assignment[i] = True   # True comes first, so we set it to true
    
    print("YES")
    result = []
    for b in assignment:
        result.append('1' if b else '0')
    print(' '.join(result))

if __name__ == "__main__":
    main()