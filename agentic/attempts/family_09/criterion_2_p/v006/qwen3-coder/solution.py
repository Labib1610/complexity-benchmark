import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m, k = map(int, sys.stdin.readline().split())
    
    # Build adjacency list
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Color the graph into two sets (bipartition)
    color = [-1] * (n + 1)
    set_a = []
    set_b = []
    
    def bfs(start):
        queue = deque()
        queue.append(start)
        color[start] = 0
        set_a.append(start)
        
        while queue:
            node = queue.popleft()
            current_color = color[node]
            next_color = 1 - current_color
            
            for neighbor in adj[node]:
                if color[neighbor] == -1:
                    color[neighbor] = next_color
                    if next_color == 0:
                        set_a.append(neighbor)
                    else:
                        set_b.append(neighbor)
                    queue.append(neighbor)
                elif color[neighbor] == current_color:
                    # This should not happen as per problem statement
                    return False
        return True
    
    # Check all components
    for i in range(1, n+1):
        if color[i] == -1:
            if not bfs(i):
                # Not bipartite - but problem guarantees it is
                pass
    
    # Now we have two sets: set_a and set_b
    # A harmonious team can take any subset from one set or combine subsets from both
    # But since all edges go between sets, we can pick any subset from either set
    
    if len(set_a) >= k:
        print("YES")
        print(' '.join(map(str, set_a[:k])))
    elif len(set_b) >= k:
        print("YES")
        print(' '.join(map(str, set_b[:k])))
    else:
        print("NO")

if __name__ == "__main__":
    main()