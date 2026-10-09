import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    try:
        q = int(next(iterator))
        t = int(next(iterator))
    except StopIteration:
        return

    adj = [[] for _ in range(q + 1)]
    
    for _ in range(t):
        a = int(next(iterator))
        b = int(next(iterator))
        adj[a].append(b)

    # We need to find a perfect matching in a bipartite graph
    # Left side: 1..q, Right side: q+1..2q
    # Using Hopcroft-Karp algorithm
    
    pair_U = [0] * (q + 1)
    pair_V = [0] * (2 * q + 1)
    dist = [0] * (q + 1)
    NIL = 0

    def bfs():
        queue = deque()
        for u in range(1, q + 1):
            if pair_U[u] == NIL:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = float('inf')
        dist[NIL] = float('inf')
        
        while queue:
            u = queue.popleft()
            if dist[u] < dist[NIL]:
                for v in adj[u]:
                    if pair_V[v] == NIL:
                        if dist[NIL] == float('inf'):
                            dist[NIL] = dist[u] + 1
                    elif dist[pair_V[v]] == float('inf'):
                        dist[pair_V[v]] = dist[u] + 1
                        queue.append(pair_V[v])
        
        return dist[NIL] != float('inf')

    def dfs(u):
        if u != NIL:
            for v in adj[u]:
                if pair_V[v] == NIL:
                    if dist[NIL] == dist[u] + 1:
                        if dfs(NIL):
                            pair_U[u] = v
                            pair_V[v] = u
                            return True
                elif dist[pair_V[v]] == dist[u] + 1:
                    if dfs(pair_V[v]):
                        pair_U[u] = v
                        pair_V[v] = u
                        return True
            dist[u] = float('inf')
            return False
        return True

    matching = 0
    while bfs():
        for u in range(1, q + 1):
            if pair_U[u] == NIL:
                if dfs(u):
                    matching += 1
    
    if matching == q:
        print("YES")
        for u in range(1, q + 1):
            print(u, pair_U[u])
    else:
        print("NO")

if __name__ == '__main__':
    solve()