import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    
    index = 3
    edges = []
    adj = defaultdict(list)
    
    for _ in range(m):
        u = int(data[index])
        v = int(data[index+1])
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
        index += 2
    
    if m == 0:
        print("YES")
        print(' '.join(map(str, range(1, k+1))))
        return
    
    # Color the graph with two colors (0 and 1)
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
    
    # Check if the graph is bipartite and find the two sets
    set0 = []
    set1 = []
    
    for i in range(1, n+1):
        if not visited[i]:
            if not bfs(i):
                # This shouldn't happen according to problem statement
                print("NO")
                return
    
    for i in range(1, n+1):
        if color[i] == 0:
            set0.append(i)
        else:
            set1.append(i)
    
    # Now we have two independent sets
    if len(set0) >= k:
        print("YES")
        print(' '.join(map(str, set0[:k])))
    elif len(set1) >= k:
        print("YES")
        print(' '.join(map(str, set1[:k])))
    else:
        print("NO")

if __name__ == "__main__":
    main()