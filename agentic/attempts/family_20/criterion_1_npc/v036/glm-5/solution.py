import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        idx += 2
        edges.append((u, v))
        adj[u].append((v, len(edges) - 1))
        adj[v].append((u, len(edges) - 1))
        
    ans = [0] * m
    
    # We use a 3-coloring algorithm for cubic graphs.
    # Since n is even and m = 3n/2, the graph is 3-regular.
    # We can always find a perfect matching in a 3-regular bridgeless graph.
    # We repeatedly find perfect matchings and assign them a color.
    # After removing 2 perfect matchings, the remaining graph is a disjoint union of even cycles,
    # which is 2-colorable.
    
    for color in range(1, 3):
        match = [0] * (n + 1)
        visited = [False] * (n + 1)
        
        def dfs(u):
            for v, edge_idx in adj[u]:
                if not visited[v] and ans[edge_idx] == 0:
                    visited[v] = True
                    if match[v] == 0 or dfs(match[v]):
                        match[u] = v
                        match[v] = u
                        return True
            return False
            
        for u in range(1, n + 1):
            if match[u] == 0:
                visited = [False] * (n + 1)
                visited[u] = True
                dfs(u)
                
        for u in range(1, n + 1):
            if match[u] > u:
                for v, edge_idx in adj[u]:
                    if v == match[u]:
                        ans[edge_idx] = color
                        break
                        
    # The remaining edges form a disjoint union of even cycles.
    # We can 2-color them using colors 3 and 4, but since we only need 3 colors
    # and the cycles are even, we can just use colors 3 and 1.
    # Wait, the problem requires colors from {1, 2, 3}.
    # Let's just use 3 and 4 for the cycle, then remap 4 to 1.
    # Since the cycle edges are disjoint from the 1st matching, 
    # assigning color 1 to the "4" edges won't violate the condition.
    
    for u in range(1, n + 1):
        for v, edge_idx in adj[u]:
            if ans[edge_idx] == 0:
                if u < v:
                    # To avoid double processing, we can just do a DFS/BFS for the remaining edges
                    pass
    
    # Let's properly 2-color the remaining cycles
    visited_nodes = [False] * (n + 1)
    for start_node in range(1, n + 1):
        if not visited_nodes[start_node]:
            # Find an uncolored edge to start
            start_edge = -1
            for v, edge_idx in adj[start_node]:
                if ans[edge_idx] == 0:
                    start_edge = edge_idx
                    break
            
            if start_edge != -1:
                # Traverse the cycle
                curr_node = start_node
                curr_color = 3
                prev_node = -1
                
                while True:
                    visited_nodes[curr_node] = True
                    next_node = -1
                    next_edge = -1
                    
                    for v, edge_idx in adj[curr_node]:
                        if ans[edge_idx] == 0:
                            if v != prev_node:
                                next_node = v
                                next_edge = edge_idx
                                
                    if next_node == -1:
                        break
                        
                    ans[next_edge] = curr_color
                    curr_color = 4 if curr_color == 3 else 3
                    prev_node = curr_node
                    curr_node = next_node
                    
                    if curr_node == start_node:
                        # Closed the cycle
                        # The last edge connects curr_node to start_node
                        # We already colored it
                        break

    # Remap color 4 to 1
    for i in range(m):
        if ans[i] == 4:
            ans[i] = 1
            
    print("YES")
    print(" ".join(map(str, ans)))

if __name__ == '__main__':
    solve()