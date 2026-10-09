import sys
from collections import defaultdict, deque

def read_ints():
    return map(int, sys.stdin.readline().split())

def main():
    n, m, k = read_ints()
    
    # Build adjacency list
    adj = defaultdict(list)
    for _ in range(m):
        u, v = read_ints()
        adj[u].append(v)
        adj[v].append(u)
    
    # Since conflicts occur only when phase differences are odd,
    # the conflict graph is bipartite.
    # We can color the graph with 2 colors.
    color = [-1] * (n + 1)  # -1: unvisited, 0: color 0, 1: color 1
    
    def bfs(start):
        queue = deque([start])
        color[start] = 0
        count = [0, 0]  # count[color]
        count[0] = 1
        
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    count[color[v]] += 1
                    queue.append(v)
                elif color[v] == color[u]:
                    # This should not happen as per problem statement
                    # but we check for safety
                    return None, None
        return count[0], count[1]
    
    # Find all connected components and their bipartition sizes
    components = []
    for i in range(1, n + 1):
        if color[i] == -1:
            c0, c1 = bfs(i)
            if c0 is not None:
                components.append((c0, c1))
    
    # Now we need to select exactly k nodes such that no two conflicting nodes are selected.
    # In each component, we can select nodes from only one side of the bipartition.
    
    # DP: dp[i][j] = whether we can select exactly j nodes using first i components
    # But since n is large, we use a different approach.
    
    # For each component, we can choose either all nodes of color 0 or all nodes of color 1.
    # So for each component we have a choice: take c0 nodes or c1 nodes.
    # We want to select exactly k nodes in total.
    
    # This becomes a subset sum problem where we want to find if there's a way to 
    # choose exactly one value from each pair (c0, c1) such that their sum is k.
    
    # Let's think differently. Since the graph is bipartite, we can partition all nodes
    # into two sets U and V such that no edge connects two nodes within the same set.
    # Then we can take any subset of U or any subset of V as long as they don't have internal edges.
    # Wait, that's not right. We can take nodes from both U and V, as long as no edge exists between them.
    
    # Actually, let's re-color the entire graph.
    # Color all nodes. Nodes with color 0 form one independent set, nodes with color 1 form another.
    # An independent set means no two nodes in it are adjacent.
    
    red_nodes = []   # color 0
    blue_nodes = []  # color 1
    
    for i in range(1, n + 1):
        if color[i] == 0:
            red_nodes.append(i)
        elif color[i] == 1:
            blue_nodes.append(i)
    
    # Now we can take any combination of nodes from red_nodes and blue_nodes
    # as long as they don't have edges between them. But wait!
    # There might be edges between red and blue nodes.
    # No! In a bipartite graph colored properly, all edges go from red to blue.
    # So taking nodes only from red set or only from blue set ensures no conflicts.
    # But we can also mix them, as long as we don't pick conflicting pairs.
    # Actually, since we colored the whole graph, red set and blue set are both independent sets.
    # So we can take any subset of red nodes and any subset of blue nodes, and their union
    # will be a valid selection (no conflicts).
    
    # But that's not true either. We could have edges between red and blue nodes.
    # The key insight is that the conflict graph is bipartite.
    # So we can partition the nodes into two sets such that no edge exists within each set.
    # These two sets are our "red" and "blue" sets.
    # We can take any number of red nodes (up to |red|) and any number of blue nodes (up to |blue|)
    # such that total is k.
    
    r = len(red_nodes)
    b = len(blue_nodes)
    
    # We want to select x red nodes and y blue nodes such that x + y = k
    # where 0 <= x <= r and 0 <= y <= b
    
    found = False
    result_x = 0
    result_y = 0
    
    for x in range(min(r, k) + 1):
        y = k - x
        if 0 <= y <= b:
            found = True
            result_x = x
            result_y = y
            break
    
    if not found:
        print("NO")
        return
    
    # Select first result_x nodes from red_nodes and first result_y nodes from blue_nodes
    selected = red_nodes[:result_x] + blue_nodes[:result_y]
    
    print("YES")
    print(' '.join(map(str, selected)))

if __name__ == "__main__":
    main()