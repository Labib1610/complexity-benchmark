import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m, k = map(int, sys.stdin.readline().split())
    
    # Build adjacency list
    adj = defaultdict(list)
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # Since the graph is bipartite (frequency isolation property),
    # we can color it with two colors.
    # We'll use BFS to color the graph.
    color = [-1] * (n + 1)  # -1: unvisited, 0: color A, 1: color B
    
    def bfs(start):
        queue = deque()
        queue.append(start)
        color[start] = 0
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    queue.append(v)
                elif color[v] == color[u]:
                    # This should never happen due to problem guarantee
                    return False
        return True
    
    # Color all components
    for i in range(1, n + 1):
        if color[i] == -1:
            if not bfs(i):
                # Should not happen per problem statement
                print("NO")
                return
    
    # Count nodes in each color class
    count_a = 0
    count_b = 0
    nodes_a = []
    nodes_b = []
    
    for i in range(1, n + 1):
        if color[i] == 0:
            count_a += 1
            nodes_a.append(i)
        else:
            count_b += 1
            nodes_b.append(i)
    
    # Now we want to select exactly k nodes such that no two are adjacent.
    # In a bipartite graph, this means selecting nodes from the same partition.
    # So we can select up to count_a nodes from partition A or up to count_b from partition B.
    # But we want exactly k.
    
    # Check if it's possible:
    # We can form any subset from A or B as long as its size is <= count_a or <= count_b respectively.
    # But we need exactly k.
    # The maximum number of nodes we can select without interference is max(count_a, count_b).
    # Actually, we can select any number of nodes from A (up to count_a) and any number from B (up to count_b),
    # as long as there are no edges between them. But since A and B are partitions, there are no edges within A or within B.
    # So we can select any subset of A or any subset of B.
    # Wait, that's not right. We can select any combination of nodes from A and B,
    # as long as there are no edges between selected nodes from A and selected nodes from B.
    # But since ALL edges go between A and B, we can select any subset of A and any subset of B.
    # That means we can select any number of nodes from 0 to n, because we can take i nodes from A and (k-i) from B,
    # as long as 0 <= i <= count_a and 0 <= k-i <= count_b.
    
    # So, we need to find if there exists an integer i such that:
    # 0 <= i <= count_a
    # 0 <= k - i <= count_b
    # Which simplifies to:
    # max(0, k - count_b) <= i <= min(count_a, k)
    
    # Check if such an i exists
    low = max(0, k - count_b)
    high = min(count_a, k)
    
    if low <= high:
        # There exists such an i. Let's pick one.
        i = low  # For example
        j = k - i  # Number of nodes from B
        
        # Select i nodes from A and j nodes from B
        result = nodes_a[:i] + nodes_b[:j]
        
        print("YES")
        print(' '.join(map(str, result)))
    else:
        print("NO")

if __name__ == "__main__":
    main()