import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    
    adj = [[] for _ in range(n + 1)]
    idx = 3
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
        
    # 2-coloring to partition into L and R
    color = [-1] * (n + 1)
    for i in range(1, n + 1):
        if color[i] == -1:
            color[i] = 0
            queue = [i]
            head = 0
            while head < len(queue):
                u = queue[head]
                head += 1
                c = color[u]
                nc = 1 - c
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = nc
                        queue.append(v)

    # Hopcroft-Karp algorithm
    pair_u = [0] * (n + 1)
    pair_v = [0] * (n + 1)
    dist = [0] * (n + 1)
    
    # Separate adj_L for vertices in L (color == 0)
    adj_L = [[] for _ in range(n + 1)]
    for u in range(1, n + 1):
        if color[u] == 0:
            adj_L[u] = adj[u]

    INF = 10**9
    
    def bfs():
        queue = []
        for u in range(1, n + 1):
            if color[u] == 0:
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
                du1 = dist[u] + 1
                for v in adj_L[u]:
                    pv = pair_v[v]
                    if dist[pv] == INF:
                        dist[pv] = du1
                        queue.append(pv)
        return dist[0] != INF

    def dfs(u):
        if u != 0:
            du1 = dist[u] + 1
            for v in adj_L[u]:
                pv = pair_v[v]
                if dist[pv] == du1:
                    if dfs(pv):
                        pair_v[v] = u
                        pair_u[u] = v
                        return True
            dist[u] = INF
            return False
        return True

    matching = 0
    while bfs():
        for u in range(1, n + 1):
            if color[u] == 0 and pair_u[u] == 0:
                if dfs(u):
                    matching += 1

    max_is_size = n - matching
    if max_is_size < k:
        print("NO")
        return

    # Find reachable vertices Z from unmatched vertices in L
    # Directed graph:
    # L -> R for unmatched edges: v not in pair_u[u] (i.e. v != pair_u[u])
    # R -> L for matched edge: pair_v[v]
    visited_L = [False] * (n + 1)
    visited_R = [False] * (n + 1)
    
    queue = []
    for u in range(1, n + 1):
        if color[u] == 0 and pair_u[u] == 0:
            visited_L[u] = True
            queue.append(u)
            
    head = 0
    while head < len(queue):
        u = queue[head]
        head += 1
        for v in adj_L[u]:
            if v != pair_u[u]:
                if not visited_R[v]:
                    visited_R[v] = True
                    pu = pair_v[v]
                    if pu != 0 and not visited_L[pu]:
                        visited_L[pu] = True
                        queue.append(pu)

    # Max Independent Set: (L and visited_L) union (R and not visited_R)
    independent_set = []
    for u in range(1, n + 1):
        if color[u] == 0:
            if visited_L[u]:
                independent_set.append(u)
        else:
            if not visited_R[u]:
                independent_set.append(u)
                
    print("YES")
    print(*(independent_set[:k]))

if __name__ == '__main__':
    solve()