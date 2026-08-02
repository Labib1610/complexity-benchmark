import sys

def main():
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    if m == 0:
        print("YES")
        print('1 ' * (n - 1) + '2')
        return

    edges = []
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1
        v = int(data[index + 1]) - 1
        edges.append((u, v))
        index += 2
    
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    assigned = [-1] * n
    
    def can_assign(node, color):
        for neighbor in graph[node]:
            if assigned[neighbor] == color:
                return False
        return True

    def assign_colors(node):
        if node == n:
            print("YES")
            print(' '.join(map(str, (assigned[i] + 1 for i in range(n)))))
            sys.exit(0)
        
        for color in [1, 2, 3]:
            if can_assign(node, color):
                assigned[node] = color
                assign_colors(node + 1)
                assigned[node] = -1
    
    assign_colors(0)
    print("NO")

if __name__ == "__main__":
    main()