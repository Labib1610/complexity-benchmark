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
    
    # Since the graph is bipartite, we can color it with two colors
    # We'll use BFS to 2-color the graph
    color = [-1] * (n + 1)  # -1: unvisited, 0: color A, 1: color B
    cohort_a = []
    cohort_b = []
    
    # Process each connected component
    visited = [False] * (n + 1)
    
    for start in range(1, n + 1):
        if visited[start]:
            continue
            
        queue = deque()
        queue.append(start)
        color[start] = 0
        visited[start] = True
        
        while queue:
            node = queue.popleft()
            if color[node] == 0:
                cohort_a.append(node)
            else:
                cohort_b.append(node)
                
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    color[neighbor] = 1 - color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    # This should never happen due to problem constraint
                    pass
    
    # Now we have two independent sets (cohort_a and cohort_b)
    # We need to pick k nodes such that none are adjacent
    # So we can pick from either cohort_a or cohort_b
    
    if len(cohort_a) >= k:
        print("YES")
        print(' '.join(map(str, cohort_a[:k])))
    elif len(cohort_b) >= k:
        print("YES")
        print(' '.join(map(str, cohort_b[:k])))
    else:
        print("NO")

if __name__ == "__main__":
    main()