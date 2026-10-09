import sys
from collections import defaultdict, deque

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    edges = []
    adj = defaultdict(list)
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1
        v = int(data[index+1]) - 1
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
        index += 2
    
    # Color with 2 colors (1 and 2) using BFS
    color = [-1] * n
    for i in range(n):
        if color[i] == -1:
            queue = deque()
            queue.append(i)
            color[i] = 1
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 3 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        return
    
    # If bipartite, output the coloring
    print("YES")
    result = []
    for i in range(n):
        if color[i] == 1:
            result.append("1")
        else:
            result.append("2")
    print(" ".join(result))

if __name__ == "__main__":
    main()