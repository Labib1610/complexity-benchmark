import sys
from collections import defaultdict

def main():
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    if m == 0:
        print("YES")
        print(' '.join(['1'] * n))
        return
    
    edges = defaultdict(list)
    for i in range(m):
        u = int(data[2 + 2*i])
        v = int(data[3 + 2*i])
        edges[u].append(v)
        edges[v].append(u)
    
    def dfs(node, color):
        if node in colors:
            return colors[node] == color
        colors[node] = color
        for neighbor in edges[node]:
            if not dfs(neighbor, 3 - color):
                return False
        return True
    
    colors = {}
    valid = True
    for i in range(1, n + 1):
        if i not in colors:
            if not dfs(i, 1):
                valid = False
                break
    
    if valid:
        print("YES")
        print(' '.join(map(str, [colors[i] for i in range(1, n + 1)])))
    else:
        print("NO")

if __name__ == "__main__":
    main()