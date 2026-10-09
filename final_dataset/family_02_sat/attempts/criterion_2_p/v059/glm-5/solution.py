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
        v1 = int(next(it))
        v2 = int(next(it))
        # v1 > 0: database v1 is synchronous (1)
        # v1 < 0: database |v1| is asynchronous (0)
        # We map database i, setting 1 to index 2*i
        # We map database i, setting 0 to index 2*i + 1
        
        # Clause: (setting for v1) OR (setting for v2)
        # Implications: NOT v1 -> v2, NOT v2 -> v1
        
        # Process v1
        if v1 > 0:
            node_v1_true = 2 * v1       # v1 is 1
            node_v1_false = 2 * v1 + 1  # v1 is 0
        else:
            node_v1_true = 2 * (-v1) + 1 # v1 is 0 (since v1 < 0)
            node_v1_false = 2 * (-v1)    # v1 is 1
            
        # Process v2
        if v2 > 0:
            node_v2_true = 2 * v2
            node_v2_false = 2 * v2 + 1
        else:
            node_v2_true = 2 * (-v2) + 1
            node_v2_false = 2 * (-v2)
            
        # Add edges for implications
        adj[node_v1_false].append(node_v2_true)
        adj[node_v2_false].append(node_v1_true)
    
    N = 2 * n
    visited = [False] * (N + 1)
    order = []
    
    def dfs(u):
        stack = [(u, 0)]
        while stack:
            node, idx = stack.pop()
            if idx == 0:
                if visited[node]:
                    continue
                visited[node] = True
                stack.append((node, 1))
                for neighbor in adj[node]:
                    if not visited[neighbor]:
                        stack.append((neighbor, 0))
            else:
                order.append(node)

    for i in range(1, N + 1):
        if not visited[i]:
            dfs(i)
            
    visited = [False] * (N + 1)
    comp_id = [0] * (N + 1)
    current_comp = 0
    
    # Process in reverse order of finishing times
    for u in reversed(order):
        if not visited[u]:
            current_comp += 1
            stack = [u]
            visited[u] = True
            while stack:
                node = stack.pop()
                comp_id[node] = current_comp
                # Iterate reverse graph
                # Since adj is the implication graph, reverse graph is just adj^T
                # We need to iterate neighbors that point TO node.
                # We can build a reverse adjacency list or just iterate all nodes.
                # Given constraints, building reverse adjacency is better.
                # Let's build radj.
                pass

    # We need the reverse graph for the second pass
    radj = [[] for _ in range(N + 1)]
    for u in range(1, N + 1):
        for v in adj[u]:
            radj[v].append(u)
            
    visited = [False] * (N + 1)
    current_comp = 0
    
    for u in reversed(order):
        if not visited[u]:
            current_comp += 1
            stack = [u]
            visited[u] = True
            while stack:
                node = stack.pop()
                comp_id[node] = current_comp
                for neighbor in radj[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)
    
    assignment = [0] * (n + 1)
    possible = True
    
    for i in range(1, n + 1):
        node_true = 2 * i
        node_false = 2 * i + 1
        if comp_id[node_true] == comp_id[node_false]:
            possible = False
            break
        if comp_id[node_true] > comp_id[node_false]:
            assignment[i] = 1
        else:
            assignment[i] = 0
            
    if not possible:
        print("NO")
    else:
        print("YES")
        print(*(assignment[1:]))

if __name__ == '__main__':
    solve()