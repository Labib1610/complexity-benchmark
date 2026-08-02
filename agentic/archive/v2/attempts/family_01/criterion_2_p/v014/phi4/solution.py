import sys
from collections import defaultdict

def day_and_night():
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

    if n == 1:
        print("YES")
        print(1)
        return

    adj_list = defaultdict(list)
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)

    schedule = [0] * (n + 1)
    
    def dfs(node, period):
        if schedule[node]:
            return schedule[node] == period
        schedule[node] = period
        for neighbor in adj_list[node]:
            if not dfs(neighbor, 3 - period):
                return False
        return True
    
    possible = True
    for i in range(1, n + 1):
        if schedule[i] == 0:
            if not dfs(i, 1):
                possible = False
                break

    if possible:
        print("YES")
        print(' '.join(map(str, schedule[1:])))
    else:
        print("NO")

day_and_night()