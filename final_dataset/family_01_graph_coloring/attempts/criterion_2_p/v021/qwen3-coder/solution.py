import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m = map(int, sys.stdin.readline().split())
    
    # Build adjacency list
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Color array: 0 = unvisited, 1 = color 1, 2 = color 2
    color = [0] * (n + 1)
    
    # Check if bipartite using BFS
    def bfs(start):
        queue = deque()
        queue.append(start)
        color[start] = 1
        
        while queue:
            u = queue.popleft()
            current_color = color[u]
            next_color = 2 if current_color == 1 else 1
            
            for v in adj[u]:
                if color[v] == 0:
                    color[v] = next_color
                    queue.append(v)
                elif color[v] == current_color:
                    return False
        return True
    
    # Process each connected component
    for i in range(1, n + 1):
        if color[i] == 0:
            if not bfs(i):
                print("NO")
                return
    
    # If we reach here, it's bipartite
    # Ensure lexicographically smallest: prefer color 1 for earlier nodes
    # Since we're doing BFS from node 1 upwards, and always assigning 1 first,
    # this naturally gives us the lex smallest assignment.
    
    # But to be safe, let's re-assign ensuring lex smallest:
    # For each component, if we can choose the color of the first node,
    # we choose 1 to get lex smallest.
    # However, our BFS already does that since we start with color[1] = 1 if 1 exists.
    # For components not containing node 1, we start with color = 1 for the smallest node.
    
    # Actually, our BFS traversal ensures that for each component, 
    # the first node (in terms of iteration) gets color 1, which may not be lex smallest.
    # Let's redo this properly.
    
    # Re-initialize
    color = [0] * (n + 1)
    visited = [False] * (n + 1)
    
    def bfs_lex(start):
        queue = deque()
        queue.append(start)
        # To get lexicographically smallest, node 'start' should be 1
        color[start] = 1
        visited[start] = True
        
        while queue:
            u = queue.popleft()
            current_color = color[u]
            next_color = 2 if current_color == 1 else 1
            
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    color[v] = next_color
                    queue.append(v)
                elif color[v] != next_color:
                    return False
        return True
    
    # Process components in order
    for i in range(1, n + 1):
        if not visited[i]:
            if not bfs_lex(i):
                print("NO")
                return
    
    print("YES")
    # For nodes with no edges, assign 1 (to be lex smallest)
    result = []
    for i in range(1, n + 1):
        if color[i] == 0:
            result.append('1')
        else:
            result.append(str(color[i]))
    print(' '.join(result))

if __name__ == "__main__":
    main()