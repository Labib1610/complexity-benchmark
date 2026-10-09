import sys
from collections import defaultdict, deque

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    n, m, k = map(int, sys.stdin.readline().split())
    
    if m == 0:
        print("YES")
        print(' '.join(map(str, range(1, k+1))))
        return
    
    adj = defaultdict(list)
    degree = [0] * (n + 1)
    
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
        degree[u] += 1
        degree[v] += 1
    
    # Color the graph with BFS to get bipartition
    color = [-1] * (n + 1)
    visited = [False] * (n + 1)
    
    def bfs(start):
        queue = deque()
        queue.append(start)
        color[start] = 0
        visited[start] = True
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    color[v] = 1 - color[u]
                    queue.append(v)
                elif color[v] == color[u]:
                    return False
        return True
    
    # Check if graph is bipartite and get the partition
    for i in range(1, n+1):
        if not visited[i] and adj[i]:  # Only start BFS if node has edges
            if not bfs(i):
                # This shouldn't happen according to problem statement
                print("NO")
                return
    
    # Handle isolated nodes (nodes with no conflicts) - they can be assigned any color
    for i in range(1, n+1):
        if color[i] == -1:
            color[i] = 0
    
    # Separate nodes into two groups based on color
    group0 = []
    group1 = []
    for i in range(1, n+1):
        if color[i] == 0:
            group0.append(i)
        else:
            group1.append(i)
    
    # Since there are no conflicts within groups, we can choose from either group
    # We want exactly k members total
    # We can take up to len(group0) from group0 and up to len(group1) from group1
    # But since the graph is bipartite and all edges go between groups,
    # a harmonious delegation is any subset that doesn't contain conflicting members
    # which means we can take any combination from the two groups as long as total = k
    
    # Try to find a valid combination
    found = False
    selected = []
    
    # Greedy approach: try taking as many as possible from one group
    if len(group0) >= k:
        selected = group0[:k]
        found = True
    elif len(group1) >= k:
        selected = group1[:k]
        found = True
    else:
        # Need to combine both groups
        take_from_0 = min(len(group0), k)
        need_from_1 = k - take_from_0
        if need_from_1 <= len(group1):
            selected = group0[:take_from_0] + group1[:need_from_1]
            found = True
        else:
            # Try the other way around
            take_from_1 = min(len(group1), k)
            need_from_0 = k - take_from_1
            if need_from_0 <= len(group0):
                selected = group1[:take_from_1] + group0[:need_from_0]
                found = True
    
    if found:
        print("YES")
        print(' '.join(map(str, selected)))
    else:
        print("NO")

if __name__ == "__main__":
    main()