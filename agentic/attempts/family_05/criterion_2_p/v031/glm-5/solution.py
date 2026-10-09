import sys
from collections import deque

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    # For each agent x, store the set of allowed frequencies z
    agent_freqs = [set() for _ in range(k + 1)]
    
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        agent_freqs[x].add(z)
    
    # Bipartite matching between agents (1..k) and frequencies (1..k)
    # We use Hopcroft-Karp algorithm
    
    # Adjacency list: for each agent (left node), list of frequencies (right node)
    adj = agent_freqs
    
    # PairU[u] = frequency matched to agent u, 0 if free
    PairU = [0] * (k + 1)
    # PairV[v] = agent matched to frequency v, 0 if free
    PairV = [0] * (k + 1)
    # Dist for BFS layers
    Dist = [0] * (k + 1)
    NIL = 0
    
    def bfs():
        queue = deque()
        for u in range(1, k + 1):
            if PairU[u] == NIL:
                Dist[u] = 0
                queue.append(u)
            else:
                Dist[u] = float('inf')
        Dist[NIL] = float('inf')
        
        while queue:
            u = queue.popleft()
            if Dist[u] < Dist[NIL]:
                for v in adj[u]:
                    if Dist[PairV[v]] == float('inf'):
                        Dist[PairV[v]] = Dist[u] + 1
                        queue.append(PairV[v])
        return Dist[NIL] != float('inf')
    
    def dfs(u):
        if u != NIL:
            for v in adj[u]:
                if Dist[PairV[v]] == Dist[u] + 1:
                    if dfs(PairV[v]):
                        PairV[v] = u
                        PairU[u] = v
                        return True
            Dist[u] = float('inf')
            return False
        return True
    
    matching = 0
    while bfs():
        for u in range(1, k + 1):
            if PairU[u] == NIL:
                if dfs(u):
                    matching += 1
    
    if matching != k:
        print("NO")
    else:
        print("YES")
        # Output the matching: agent x uses frequency PairU[x], alias is x
        for x in range(1, k + 1):
            print(x, x, PairU[x])

if __name__ == "__main__":
    solve()