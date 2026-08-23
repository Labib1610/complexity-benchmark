import sys
from collections import defaultdict, deque

def bfs(start, team, graph, teams):
    queue = deque([start])
    teams[start] = team
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if teams[neighbor] == -1:
                teams[neighbor] = 3 - teams[node]
                queue.append(neighbor)
            elif teams[neighbor] == teams[node]:
                return False
    return True

def main():
    input = sys.stdin.read
    data = input().splitlines()
    
    n, m = map(int, data[0].split())
    graph = defaultdict(list)
    
    for i in range(1, m + 1):
        u, v = map(int, data[i].split())
        graph[u].append(v)
        graph[v].append(u)
    
    teams = [-1] * (n + 1)  # -1 means unassigned
    possible = True
    
    for i in range(1, n + 1):
        if teams[i] == -1:
            if not bfs(i, 1, graph, teams):
                possible = False
                break
    
    if not possible:
        print("NO")
    else:
        print("YES")
        print(" ".join(str(teams[i]) for i in range(1, n + 1)))

main()