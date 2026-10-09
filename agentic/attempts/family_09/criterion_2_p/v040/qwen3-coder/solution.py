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
    adj = defaultdict(set)
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    
    # Since it's a bipartite graph (routing-storage), we can color it
    # Try to 2-color the graph
    color = {}
    for i in range(1, n+1):
        if i not in color:
            # BFS to color component
            queue = deque([i])
            color[i] = 0
            while queue:
                node = queue.popleft()
                for neighbor in adj[node]:
                    if neighbor not in color:
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:
                        # This should not happen according to problem statement
                        pass
    
    # Separate nodes by color
    set0 = [node for node in range(1, n+1) if color.get(node, 0) == 0]
    set1 = [node for node in range(1, n+1) if color.get(node, 0) == 1]
    
    # Check if we can take k nodes
    # In a bipartite graph, we can take all nodes from one side
    if len(set0) >= k:
        return "YES", set0[:k]
    elif len(set1) >= k:
        return "YES", set1[:k]
    else:
        # We need to check if there's an independent set of size k
        # But since it's bipartite, max independent set = max(|set0|, |set1|)
        # So if k > max(|set0|, |set1|), then NO
        return "NO", []

def main():
    n, m, k, edges = read_input()
    result, selection = solve(n, m, k, edges)
    print(result)
    if result == "YES":
        print(' '.join(map(str, selection)))

if __name__ == "__main__":
    main()