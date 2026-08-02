import sys
from collections import defaultdict

def can_assign_channels(n, m, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    channels = [0] * (n + 1)  # To store channel assignments for each post
    valid = True

    def dfs(post, ch):
        nonlocal valid
        if not valid:
            return
        
        if channels[post] != 0:  # Post already visited and assigned a channel
            if channels[post] != ch:
                valid = False
            return
        
        channels[post] = ch

        for neighbor in graph[post]:
            dfs(neighbor, 3 - ch)  # Assign the opposite channel to neighbors

    for post in range(1, n + 1):
        if channels[post] == 0:  # Not yet visited
            dfs(post, 1)

    return valid, channels

def main():
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    n = int(data[index])
    m = int(data[index + 1])
    index += 2
    
    edges = []
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        edges.append((u, v))
        index += 2

    valid, channels = can_assign_channels(n, m, edges)

    if not valid:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, channels[1:])))  # Ignore channels[0] as posts are 1-indexed

if __name__ == "__main__":
    main()