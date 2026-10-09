import sys
from collections import defaultdict, deque

def main():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    
    # Map captain -> cruiser (since each captain has exactly one cruiser)
    cap_to_cruiser = {}
    # For each captain, list of allowed sectors
    cap_sectors = defaultdict(list)
    
    for _ in range(t):
        c, v, s = map(int, input().split())
        cap_to_cruiser[c] = v
        cap_sectors[c].append(s)
    
    # Build bipartite graph: left = captain index (0..k-1), right = sector index (0..k-1)
    # We'll use Hopcroft-Karp for maximum bipartite matching.
    
    adj = [[] for _ in range(k)]
    for c in range(1, k+1):
        for s in cap_sectors[c]:
            adj[c-1].append(s-1)
    
    # Hopcroft-Karp
    pairU = [-1] * k
    pairV = [-1] * k
    dist = [0] * k
    
    def bfs():
        q = deque()
        for u in range(k):
            if pairU[u] == -1:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = float('inf')
        found = False
        while q:
            u = q.popleft()
            for v in adj[u]:
                pu = pairV[v]
                if pu != -1 and dist[pu] == float('inf'):
                    dist[pu] = dist[u] + 1
                    q.append(pu)
                elif pu == -1:
                    found = True
        return found
    
    def dfs(u):
        for v in adj[u]:
            pu = pairV[v]
            if pu == -1 or (dist[pu] == dist[u] + 1 and dfs(pu)):
                pairU[u] = v
                pairV[v] = u
                return True
        dist[u] = float('inf')
        return False
    
    matching = 0
    while bfs():
        for u in range(k):
            if pairU[u] == -1 and dfs(u):
                matching += 1
    
    if matching != k:
        print("NO")
        return
    
    print("YES")
    for c in range(1, k+1):
        s = pairU[c-1] + 1
        v = cap_to_cruiser[c]
        print(c, v, s)

if __name__ == "__main__":
    main()