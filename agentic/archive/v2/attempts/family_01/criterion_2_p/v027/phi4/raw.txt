from collections import defaultdict

def dual_isolation_protocol():
    import sys
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
    
    adj_list = defaultdict(list)
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    def dfs(node, color):
        if node in colors:
            return colors[node] == color
        colors[node] = color
        for neighbor in adj_list[node]:
            if not dfs(neighbor, 3 - color):
                return False
        return True
    
    colors = {}
    possible = True
    for i in range(1, n + 1):
        if i not in colors:
            if not dfs(i, 1):
                possible = False
                break

    if possible:
        result = ['YES']
        assignment = []
        for i in range(1, n + 1):
            assignment.append(str(colors[i]))
        result.append(' '.join(assignment))
        print('\n'.join(result))
    else:
        print("NO")

if __name__ == "__main__":
    dual_isolation_protocol()