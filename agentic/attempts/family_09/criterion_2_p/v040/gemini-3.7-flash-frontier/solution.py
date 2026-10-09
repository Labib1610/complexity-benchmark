import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    k = int(input_data[2])
    
    adj = [[] for _ in range(n + 1)]
    idx = 3
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    # 2-color the graph
    color = [-1] * (n + 1)
    left_nodes = []
    right_nodes = []
    
    for i in range(1, n + 1):
        if color[i] != -1:
            continue
        color[i] = 0
        queue = [i]
        head = 0
        while head < len(queue):
            u = queue[head]
            head += 1
            c = color[u]
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - c
                    queue.append(v)

    # Hopcroft-Karp
    # Left nodes: color == 0, Right nodes: color == 1
    # Note: adj for left nodes only needs to contain right neighbors
    # (which is already true since graph is bipartite)
    
    pair_u = [0] * (n + 1)  # match for left (and right)
    pair_v = [0] * (n + 1)
    dist = [0] * (n + 1)
    INF = 10**9
    
    # Collect all left nodes
    L = [i for i in range(1, n + 1) if color[i] == 0]
    
    def bfs():
        queue = []
        for u in L:
            if pair_u[u] == 0:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = INF
        dist[0] = INF
        
        head = 0
        while head < len(queue):
            u = queue[head]
            head += 1
            if dist[u] < dist[0]:
                for v in adj[u]:
                    if dist[pair_v[v]] == INF:
                        dist[pair_v[v]] = dist[u] + 1
                        queue.append(pair_v[v])
        return dist[0] != INF

    def dfs(u):
        if u != 0:
            for v in adj[u]:
                if dist[pair_v[v]] == dist[u] + 1:
                    if dfs(pair_v[v]):
                        pair_v[v] = u
                        pair_u[u] = v
                        return True
            dist[u] = INF
            return False
        return True

    sys.setrecursionlimit(max(200000, n + 1000))
    
    while bfs():
        for u in L:
            if pair_u[u] == 0:
                dfs(u)

    # Minimum Vertex Cover and Maximum Independent Set
    # Reachability from unmatched left vertices
    # Left -> Right along non-matching edges
    # Right -> Left along matching edges
    reachable = [False] * (n + 1)
    queue = [u for u in L if pair_u[u] == 0]
    for u in queue:
        reachable[u] = True
        
    head = 0
    while head < len(queue):
        u = queue[head]
        head += 1
        if color[u] == 0:
            for v in adj[u]:
                if v != pair_u[u] and not reachable[v]:
                    reachable[v] = True
                    queue.append(v)
        else:
            v = pair_v[u]
            if v != 0 and not reachable[v]:
                reachable[v] = True
                queue.append(v)
                
    # Maximum Independent Set:
    # L_reachable U (R \ R_reachable)
    mis = []
    for i in range(1, n + 1):
        if color[i] == 0:
            if reachable[i]:
                mis.append(i)
        else:
            if not reachable[i]:
                mis.append(i)
                
    if len(mis) >= k:
        print("YES")
        print(*(mis[:k]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()