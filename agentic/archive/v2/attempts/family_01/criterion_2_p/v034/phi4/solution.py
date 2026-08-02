import sys
from collections import defaultdict

def main():
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    if m == 0:
        print("YES")
        print('1 ' * (n - 1) + "1")
        return
    
    edges = defaultdict(list)
    for i in range(m):
        u = int(data[2 + 2*i])
        v = int(data[3 + 2*i])
        edges[u].append(v)
        edges[v].append(u)
    
    color = [0] * (n + 1)
    
    def is_valid(node, c):
        for neighbor in edges[node]:
            if color[neighbor] == c:
                return False
        return True
    
    def dfs(node, c):
        stack = [node]
        while stack:
            current = stack.pop()
            if color[current] != 0:
                continue
            color[current] = c
            for neighbor in edges[current]:
                if color[neighbor] == 0 and is_valid(neighbor, 3 - c):
                    stack.append(neighbor)
    
    for i in range(1, n + 1):
        if color[i] == 0:
            if not any(is_valid(i, c) for c in [1, 2]):
                print("NO")
                return
            dfs(i, 1)
    
    result = []
    for i in range(1, n + 1):
        result.append(color[i])
    
    print("YES")
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()