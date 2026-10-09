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
        index += 2
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
    
    # Since every cycle has even length, the graph is bipartite
    # We can color it with two colors
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
                    # This should not happen as per problem statement
                    return False
        return True
    
    for i in range(1, n+1):
        if not visited[i]:
            if not bfs(i):
                # This shouldn't happen according to problem statement
                print("NO")
                return
    
    # Count nodes in each color class
    count_0 = 0
    count_1 = 0
    nodes_0 = []
    nodes_1 = []
    
    for i in range(1, n+1):
        if color[i] == 0:
            count_0 += 1
            nodes_0.append(i)
        else:
            count_1 += 1
            nodes_1.append(i)
    
    # Check if we can form a stable set of size k
    # A stable set can take all nodes from one side of the bipartition
    if k <= count_0:
        print("YES")
        print(' '.join(map(str, nodes_0[:k])))
    elif k <= count_1:
        print("YES")
        print(' '.join(map(str, nodes_1[:k])))
    else:
        print("NO")

if __name__ == "__main__":
    main()