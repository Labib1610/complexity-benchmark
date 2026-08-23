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
    adj = [[] for _ in range(n + 1)]
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
        index += 2
    
    # The XOR condition: key[u] ^ key[v] = 3
    # Since keys are 1 or 2:
    # 1 ^ 2 = 3
    # So adjacent nodes must have different keys.
    # This is a bipartite graph check.
    
    color = [0] * (n + 1)  # 0: unvisited, 1: color1, 2: color2
    
    # Check if the graph is bipartite
    for start in range(1, n + 1):
        if color[start] == 0:
            queue = deque()
            queue.append(start)
            color[start] = 1
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        print("NO")
                        return
    
    # If bipartite, assign keys based on color
    # We want lexicographically smallest assignment
    # So we prefer key 1 over key 2
    # Assign color 1 -> key 1, color 2 -> key 2
    
    result = []
    for i in range(1, n + 1):
        if color[i] == 1:
            result.append("1")
        else:
            result.append("2")
    
    print("YES")
    print(" ".join(result))

if __name__ == "__main__":
    main()