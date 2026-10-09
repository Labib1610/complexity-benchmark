import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    k = int(data[0])
    t = int(data[1])
    
    specialist_machine = {}
    adj = [[] for _ in range(k + 1)]
    
    idx = 2
    for _ in range(t):
        x = int(data[idx])
        y = int(data[idx+1])
        z = int(data[idx+2])
        idx += 3
        specialist_machine[x] = y
        adj[x].append(z)
        
    # If not all specialists have at least one machine / edge, matching can't be of size k
    if len(specialist_machine) < k:
        print("NO")
        return
        
    # Hopcroft-Karp Bipartite Matching
    # Left: specialists 1..k
    # Right: time slots 1..k
    
    pair_u = [0] * (k + 1)
    pair_v = [0] * (k + 1)
    dist = [0] * (k + 1)
    
    from collections import deque
    
    def bfs():
        queue = deque()
        for u in range(1, k + 1):
            if pair_u[u] == 0:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = float('inf')
        dist[0] = float('inf')
        
        while queue:
            u = queue.popleft()
            if dist[u] < dist[0]:
                for v in adj[u]:
                    if dist[pair_v[v]] == float('inf'):
                        dist[pair_v[v]] = dist[u] + 1
                        queue.append(pair_v[v])
        return dist[0] != float('inf')

    def dfs(u):
        if u != 0:
            for v in adj[u]:
                if dist[pair_v[v]] == dist[u] + 1:
                    if dfs(pair_v[v]):
                        pair_v[v] = u
                        pair_u[u] = v
                        return True
            dist[u] = float('inf')
            return False
        return True

    matching = 0
    while bfs():
        for u in range(1, k + 1):
            if pair_u[u] == 0:
                if dfs(u):
                    matching += 1
                    
    if matching == k:
        out = ["YES"]
        for u in range(1, k + 1):
            out.append(f"{u} {specialist_machine[u]} {pair_u[u]}")
        sys.stdout.write("\n".join(out) + "\n")
    else:
        print("NO")

if __name__ == '__main__':
    solve()