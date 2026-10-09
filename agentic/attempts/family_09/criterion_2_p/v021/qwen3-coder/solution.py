import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    
    edges = []
    adj = defaultdict(list)
    
    idx = 3
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        idx += 2
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
    
    if m == 0:
        print("YES")
        print(' '.join(map(str, range(1, k+1))))
        return
    
    # Since the graph is bipartite (Proposer-Acceptor), we can color it
    # We'll use BFS to color the graph and separate into two groups
    color = [-1] * (n + 1)
    group0 = []
    group1 = []
    
    # Check if the graph is bipartite and get the two groups
    def bfs(start):
        queue = deque()
        queue.append(start)
        color[start] = 0
        group0.append(start) if color[start] == 0 else group1.append(start)
        
        while queue:
            node = queue.popleft()
            for neighbor in adj[node]:
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[node]
                    if color[neighbor] == 0:
                        group0.append(neighbor)
                    else:
                        group1.append(neighbor)
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    # This should not happen as per problem statement
                    return False
        return True
    
    # Process all components
    visited = [False] * (n + 1)
    all_group0 = []
    all_group1 = []
    
    for i in range(1, n+1):
        if color[i] == -1:
            group0.clear()
            group1.clear()
            if not bfs(i):
                # This shouldn't happen per problem constraints
                continue
            all_group0.extend(group0[:])
            all_group1.extend(group1[:])
    
    # Now we have the two groups
    # Check if we can take k nodes from either group
    if len(all_group0) >= k:
        print("YES")
        print(' '.join(map(str, all_group0[:k])))
    elif len(all_group1) >= k:
        print("YES")
        print(' '.join(map(str, all_group1[:k])))
    else:
        print("NO")

if __name__ == "__main__":
    main()