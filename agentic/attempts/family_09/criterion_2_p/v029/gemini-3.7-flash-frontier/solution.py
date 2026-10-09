import sys

# Increase recursion depth just in case
sys.setrecursionlimit(200000)

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
        
    # 2-color the graph into L (color 0) and R (color 1)
    color = [-1] * (n + 1)
    L = []
    R = []
    
    for i in range(1, n + 1):
        if color[i] == -1:
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
    
    for i in range(1, n + 1):
        if color[i] == 0:
            L.append(i)
        else:
            R.append(i)
            
    # Hopcroft-Karp algorithm
    INF = 10**9
    pair_u = [0] * (n + 1)
    pair_v = [0] * (n + 1)
    dist = [0] * (n + 1)
    
    def bfs():
        q = []
        for u in L:
            if pair_u[u] == 0:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF
        dist[0] = INF
        
        head = 0
        while head < len(q):
            u = q[head]
            head += 1
            if dist[u] < dist[0]:
                for v in adj[u]:
                    if dist[pair_v[v]] == INF:
                        dist[pair_v[v]] = dist[u] + 1
                        q.append(pair_v[v])
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

    matching_size = 0
    while bfs():
        for u in L:
            if pair_u[u] == 0:
                if dfs(u):
                    matching_size += 1

    mis_size = n - matching_size
    if mis_size < k:
        print("NO")
        return

    # Find reachable vertices Z to construct the Maximum Independent Set
    visited_L = [False] * (n + 1)
    visited_R = [False] * (n + 1)
    
    q = []
    for u in L:
        if pair_u[u] == 0:
            visited_L[u] = True
            q.append(u)
            
    head = 0
    while head < len(q):
        u = q[head]
        head += 1
        for v in adj[u]:
            if v != pair_u[u] and not visited_R[v]:
                visited_R[v] = True
                match_u = pair_v[v]
                if match_u != 0 and not visited_L[match_u]:
                    visited_L[match_u] = True
                    q.append(match_u)
                    
    ans = []
    for u in L:
        if visited_L[u]:
            ans.append(u)
    for v in R:
        if not visited_R[v]:
            ans.append(v)
            
    ans = ans[:k]
    print("YES")
    print(*(ans))

if __name__ == '__main__':
    solve()