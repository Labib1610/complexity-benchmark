import sys
from collections import defaultdict, deque

def main():
    import sys
    import threading
    sys.setrecursionlimit(1 << 25)
    
    def solve():
        n, m, B = map(int, sys.stdin.readline().split())
        
        if m != n - 1:
            print("NO")
            return
            
        edges = []
        adj = defaultdict(list)
        for _ in range(m):
            u, v = map(int, sys.stdin.readline().split())
            edges.append((u, v))
            adj[u].append(v)
            adj[v].append(u)
            
        # Check if it's a tree
        visited = [False] * (n + 1)
        queue = deque([1])
        visited[1] = True
        node_count = 1
        
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)
                    node_count += 1
                    
        if node_count != n:
            print("NO")
            return
            
        # Find the center of the tree to minimize total distance
        # First, find one end of the diameter
        def bfs_farthest(start):
            visited = [False] * (n + 1)
            queue = deque([(start, 0)])
            visited[start] = True
            farthest_node = start
            max_dist = 0
            
            while queue:
                u, dist = queue.popleft()
                if dist > max_dist:
                    max_dist = dist
                    farthest_node = u
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        queue.append((v, dist + 1))
            return farthest_node, max_dist
            
        # Find one end of diameter
        end1, _ = bfs_farthest(1)
        # Find the other end and get diameter
        end2, diameter = bfs_farthest(end1)
        
        # BFS to get distances from end1
        visited = [False] * (n + 1)
        dist_from_end1 = [0] * (n + 1)
        queue = deque([end1])
        visited[end1] = True
        dist_from_end1[end1] = 0
        
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    dist_from_end1[v] = dist_from_end1[u] + 1
                    queue.append(v)
                    
        # BFS to get distances from end2
        visited = [False] * (n + 1)
        dist_from_end2 = [0] * (n + 1)
        queue = deque([end2])
        visited[end2] = True
        dist_from_end2[end2] = 0
        
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    dist_from_end2[v] = dist_from_end2[u] + 1
                    queue.append(v)
                    
        # Try placing nodes on a line to minimize total cost
        # We'll place them in order of their distance from end1
        nodes_order = list(range(1, n+1))
        nodes_order.sort(key=lambda x: dist_from_end1[x])
        
        # Calculate total cost for this arrangement
        position = [0] * (n + 1)
        for i in range(n):
            position[nodes_order[i]] = i + 1
            
        total_cost = 0
        for u, v in edges:
            total_cost += abs(position[u] - position[v])
            
        if total_cost <= B:
            print("YES")
            print(*[position[i] for i in range(1, n+1)])
            return
            
        # Try reverse order
        nodes_order.reverse()
        for i in range(n):
            position[nodes_order[i]] = i + 1
            
        total_cost = 0
        for u, v in edges:
            total_cost += abs(position[u] - position[v])
            
        if total_cost <= B:
            print("YES")
            print(*[position[i] for i in range(1, n+1)])
            return
            
        # If both fail, try a different approach: DFS ordering
        visited = [False] * (n + 1)
        dfs_order = []
        
        def dfs(u):
            visited[u] = True
            dfs_order.append(u)
            for v in adj[u]:
                if not visited[v]:
                    dfs(v)
                    
        # Find a node with minimum degree as root
        degrees = [(len(adj[i]), i) for i in range(1, n+1)]
        degrees.sort()
        root = degrees[0][1]
        
        # Reset and do DFS
        visited = [False] * (n + 1)
        dfs_order = []
        dfs(root)
        
        for i in range(n):
            position[dfs_order[i]] = i + 1
            
        total_cost = 0
        for u, v in edges:
            total_cost += abs(position[u] - position[v])
            
        if total_cost <= B:
            print("YES")
            print(*[position[i] for i in range(1, n+1)])
            return
            
        # Try reverse DFS order
        dfs_order.reverse()
        for i in range(n):
            position[dfs_order[i]] = i + 1
            
        total_cost = 0
        for u, v in edges:
            total_cost += abs(position[u] - position[v])
            
        if total_cost <= B:
            print("YES")
            print(*[position[i] for i in range(1, n+1)])
            return
            
        print("NO")
    
    threading.Thread(target=solve).start()

if __name__ == "__main__":
    main()