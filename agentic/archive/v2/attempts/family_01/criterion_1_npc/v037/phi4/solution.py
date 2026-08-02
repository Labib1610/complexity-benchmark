import sys
from collections import defaultdict

def trichrome_shifts():
    def dfs(worker):
        for neighbor in graph[worker]:
            if not colors[neighbor]:
                colors[neighbor] = 6 - colors[worker]
                if not dfs(neighbor):
                    return False
            elif colors[neighbor] == colors[worker]:
                return False
        return True
    
    input_data = sys.stdin.read().strip().split()
    
    idx = 0
    n = int(input_data[idx])
    m = int(input_data[idx + 1])
    idx += 2

    graph = defaultdict(list)
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        graph[u].append(v)
        graph[v].append(u)
        idx += 2
    
    colors = [0] * (n + 1)
    
    for worker in range(1, n + 1):
        if not colors[worker]:
            colors[worker] = 1
            if not dfs(worker):
                print("NO")
                return
    
    result = ["YES"]
    result.append(' '.join(map(str, colors[1:])))
    print('\n'.join(result))

trichrome_shifts()