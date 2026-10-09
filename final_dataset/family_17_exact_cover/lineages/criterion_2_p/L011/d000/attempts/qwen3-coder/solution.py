from collections import defaultdict, deque

def find_maximum_matching(graph, n):
    match_op = [-1] * (n + 1)
    match_veh = [-1] * (n + 1)
    
    def bfs():
        dist = [-1] * (n + 1)
        queue = deque()
        for u in range(1, n + 1):
            if match_op[u] == -1:
                dist[u] = 0
                queue.append(u)
        
        found = False
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if match_veh[v - n] == -1:
                    found = True
                elif dist[match_veh[v - n]] == -1:
                    dist[match_veh[v - n]] = dist[u] + 1
                    queue.append(match_veh[v - n])
        
        return found
    
    def dfs(u):
        for v in graph[u]:
            if match_veh[v - n] == -1 or (dist[match_veh[v - n]] == dist[u] + 1 and dfs(match_veh[v - n])):
                match_op[u] = v
                match_veh[v - n] = u
                return True
        return False
    
    while bfs():
        for u in range(1, n + 1):
            if match_op[u] == -1:
                dfs(u)
    
    return match_op

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    q = int(data[0])
    t = int(data[1])
    
    graph = defaultdict(list)
    idx = 2
    for _ in range(t):
        a = int(data[idx])
        b = int(data[idx + 1])
        graph[a].append(b)
        idx += 2
    
    match_op = find_maximum_matching(graph, q)
    
    if -1 in match_op[1:]:
        print("NO")
    else:
        print("YES")
        for i in range(1, q + 1):
            print(i, match_op[i])

if __name__ == "__main__":
    main()