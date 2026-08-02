import sys
from collections import defaultdict

def main():
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        edges.append((u, v))
        index += 2
    
    # Create adjacency list
    adj_list = defaultdict(list)
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    mode = [0] * (n + 1)
    
    def dfs(node, current_mode):
        if mode[node]:
            return mode[node] == current_mode
        mode[node] = current_mode
        for neighbor in adj_list[node]:
            if not dfs(neighbor, 3 - current_mode):
                return False
        return True
    
    possible = True
    for i in range(1, n + 1):
        if not mode[i]:
            if not dfs(i, 1):
                possible = False
                break
    
    if possible:
        print("YES")
        result = [str(mode[i]) if mode[i] else "1" for i in range(1, n + 1)]
        print(" ".join(result))
    else:
        print("NO")

if __name__ == "__main__":
    main()