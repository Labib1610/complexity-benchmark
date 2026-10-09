import sys

# Increase recursion depth just in case
sys.setrecursionlimit(300000)

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
        v = int(input_data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
        
    # 2-color the graph to divide into Left (L) and Right (R)
    color = [0] * (n + 1)
    for i in range(1, n + 1):
        if color[i] == 0:
            color[i] = 1
            queue = [i]
            for u in queue:
                c = color[u]
                next_c = 2 if c == 1 else 1
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = next_c
                        queue.append(v)

    # Hopcroft-Karp for Maximum Bipartite Matching
    # Left vertices: color[u] == 1, Right vertices: color[v] == 2
    match_L = [0] * (n + 1)
    match_R = [0] * (n + 1)
    dist = [0] * (n + 1)
    INF = 10**9

    def bfs():
        q = []
        for u in range(1, n + 1):
            if color[u] == 1:
                if match_L[u] == 0:
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
                    if dist[match_R[v]] == INF:
                        dist[match_R[v]] = dist[u] + 1
                        q.append(match_R[v])
        return dist[0] != INF

    def dfs(u):
        if u != 0:
            for v in adj[u]:
                if dist[match_R[v]] == dist[u] + 1:
                    if dfs(match_R[v]):
                        match_R[v] = u
                        match_L[u] = v
                        return True
            dist[u] = INF
            return False
        return True

    while bfs():
        for u in range(1, n + 1):
            if color[u] == 1 and match_L[u] == 0:
                dfs(u)

    # Finding Minimum Vertex Cover / Maximum Independent Set using König's Theorem
    # Reachable vertices from unmatched vertices in L via alternating paths:
    # L -> R along non-matching edges, R -> L along matching edges.
    visited_L = [False] * (n + 1)
    visited_R = [False] * (n + 1)
    
    q = []
    for u in range(1, n + 1):
        if color[u] == 1 and match_L[u] == 0:
            visited_L[u] = True
            q.append(u)
            
    head = 0
    while head < len(q):
        u = q[head]
        head += 1
        for v in adj[u]:
            if not visited_R[v] and match_L[u] != v:
                visited_R[v] = True
                match_u = match_R[v]
                if match_u != 0 and not visited_L[match_u]:
                    visited_L[match_u] = True
                    q.append(match_u)

    # Max Independent Set:
    # Vertices in L that ARE visited, and vertices in R that are NOT visited.
    independent_set = []
    for u in range(1, n + 1):
        if color[u] == 1:
            if visited_L[u]:
                independent_set.append(u)
        else:
            if not visited_R[u]:
                independent_set.append(u)

    if len(independent_set) >= k:
        sys.stdout.write("YES\n")
        sys.stdout.write(" ".join(map(str, independent_set[:k])) + "\n")
    else:
        sys.stdout.write("NO\n")

if __name__ == '__main__':
    solve()