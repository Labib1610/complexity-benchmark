import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1000000)
    
    try:
        line = sys.stdin.readline()
        if not line:
            return
        n, m, B = map(int, line.split())
    except:
        return
        
    if n == 1:
        if m == 0 and B >= 0:
            print("YES")
            print("1")
        elif m == 0 and B < 0:
            print("NO")
        else:
            # For a single node, m should be 0
            if m == 0 and B >= 0:
                print("YES")
                print("1")
            else:
                print("NO")
        return
    
    edges = []
    adj = defaultdict(list)
    
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        u -= 1
        v -= 1
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
    
    # Check if the graph is a tree
    if m != n - 1:
        print("NO")
        return
    
    # Check connectivity
    visited = [False] * n
    queue = deque()
    queue.append(0)
    visited[0] = True
    node_count = 1
    
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                node_count += 1
                queue.append(v)
    
    if node_count != n:
        print("NO")
        return
    
    # Try to find an optimal layout
    # We'll use a greedy approach by building a BFS tree and laying it out linearly
    
    # Build BFS tree from node 0
    parent = [-1] * n
    depth = [0] * n
    visited = [False] * n
    queue = deque()
    queue.append(0)
    visited[0] = True
    bfs_order = [0]
    
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                depth[v] = depth[u] + 1
                queue.append(v)
                bfs_order.append(v)
    
    # Assign slots based on BFS order
    assignment = [0] * n
    for i in range(n):
        assignment[bfs_order[i]] = i + 1
    
    # Calculate total wire length
    total_length = 0
    for u, v in edges:
        total_length += abs(assignment[u] - assignment[v])
    
    if total_length <= B:
        print("YES")
        print(' '.join(map(str, assignment)))
    else:
        # Try a different approach - DFS linear layout
        # This can give a better layout in some cases
        parent = [-1] * n
        visited = [False] * n
        dfs_tree = [[] for _ in range(n)]
        
        stack = [0]
        visited[0] = True
        order = []
        
        while stack:
            u = stack.pop()
            order.append(u)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    dfs_tree[u].append(v)
                    stack.append(v)
        
        # Layout in DFS order
        assignment_dfs = [0] * n
        for i in range(n):
            assignment_dfs[order[i]] = i + 1
            
        # Recalculate total wire length
        total_length_dfs = 0
        for u, v in edges:
            total_length_dfs += abs(assignment_dfs[u] - assignment_dfs[v])
            
        if total_length_dfs <= B:
            print("YES")
            print(' '.join(map(str, assignment_dfs)))
        else:
            print("NO")

if __name__ == "__main__":
    main()