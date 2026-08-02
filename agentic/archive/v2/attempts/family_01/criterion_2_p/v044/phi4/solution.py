import sys
from collections import defaultdict

def solve():
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    if m == 0:
        print("YES")
        print('1 ' * (n - 1) + '1')
        return
    
    edges = defaultdict(list)
    index = 2
    for _ in range(m):
        u, v = int(data[index]), int(data[index+1])
        edges[u].append(v)
        edges[v].append(u)
        index += 2

    colors = [0] * (n + 1)

    def is_valid(node, color):
        for neighbor in edges[node]:
            if colors[neighbor] == color:
                return False
        return True

    def assign_colors():
        for node in range(1, n + 1):
            if colors[node] == 0:
                if not (is_valid(node, 1) or is_valid(node, 2)):
                    return False
                colors[node] = 1 if is_valid(node, 1) else 2
        return True

    def dfs(node, color):
        stack = [node]
        while stack:
            current = stack.pop()
            if colors[current] == 0:
                colors[current] = color
                next_color = 3 - color
                for neighbor in edges[current]:
                    if colors[neighbor] == 0:
                        stack.append(neighbor)
                        colors[neighbor] = next_color

    for node in range(1, n + 1):
        if colors[node] == 0:
            dfs(node, 1)

    if assign_colors():
        print("YES")
        print(' '.join(map(str, colors[1:])))
    else:
        print("NO")

if __name__ == "__main__":
    solve()