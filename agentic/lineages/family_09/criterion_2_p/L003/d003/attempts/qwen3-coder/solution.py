import sys
from collections import defaultdict, deque

def read_input():
    n, m, k = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        edges.append((u, v))
    return n, m, k, edges

def solve(n, m, k, edges):
    # Build adjacency list
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Since interference happens when bias voltages sum to zero,
    # nodes can be partitioned into two groups where nodes in the same group
    # have the same absolute bias value (but opposite signs).
    # This forms a bipartite graph.
    
    color = {}
    
    # Check if the graph is bipartite
    def bfs(start):
        queue = deque([start])
        color[start] = 0
        while queue:
            node = queue.popleft()
            for neighbor in adj[node]:
                if neighbor not in color:
                    color[neighbor] = 1 - color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False
        return True
    
    # Try to color all components
    for i in range(1, n+1):
        if i not in color:
            if not bfs(i):
                return "NO", []
    
    # Separate nodes into two groups based on coloring
    group0 = [node for node in range(1, n+1) if color.get(node, 0) == 0]
    group1 = [node for node in range(1, n+1) if color.get(node, 0) == 1]
    
    # Try to take k nodes from one group or combination
    # But since we want maximum independent set in a bipartite graph,
    # we can take all nodes from the larger group up to size k if possible
    
    # Actually, in a bipartite graph, the maximum independent set is 
    # max(|group0|, |group1|)
    # But we need exactly k nodes.
    
    # In a bipartite graph with no edges within groups, we can take
    # any subset of nodes as long as they don't contain both endpoints of an edge.
    # So we can take all nodes from one side of the bipartition.
    
    if len(group0) >= k:
        return "YES", group0[:k]
    elif len(group1) >= k:
        return "YES", group1[:k]
    else:
        # We might be able to combine nodes from both groups
        # But we need to make sure no edge connects selected nodes
        
        # Since the graph is bipartite, we can only pick from one side
        # or we need to check if there's another way
        
        # Let's reconsider: in a bipartite graph, maximum independent set
        # is the larger of the two partitions.
        
        # But we want exactly k nodes.
        # If k <= max(|group0|, |group1|), then it's possible.
        max_independent = max(len(group0), len(group1))
        if max_independent >= k:
            if len(group0) >= k:
                return "YES", group0[:k]
            else:
                return "YES", group1[:k]
        else:
            # Even the maximum independent set is smaller than k
            return "NO", []

def main():
    n, m, k, edges = read_input()
    result, nodes = solve(n, m, k, edges)
    print(result)
    if result == "YES":
        print(' '.join(map(str, nodes)))

if __name__ == "__main__":
    main()