import sys
from collections import defaultdict, deque

def main():
    input = sys.stdin.readline
    k, t = map(int, input().split())
    
    # Map from control board to its fixed sensor array
    board_to_sensor = {}
    # Map from control board to list of possible power modules
    board_to_modules = defaultdict(list)
    
    for _ in range(t):
        x, y, z = map(int, input().split())
        board_to_sensor[x] = y
        board_to_modules[x].append(z)
    
    # Build bipartite graph: left = control boards, right = power modules
    # We need perfect matching of size k
    
    # Hopcroft-Karp algorithm for maximum bipartite matching
    # Left side: 1..k (control boards)
    # Right side: 1..k (power modules)
    
    adj = [[] for _ in range(k+1)]
    for board in range(1, k+1):
        for mod in board_to_modules[board]:
            adj[board].append(mod)
    
    pairU = [0]*(k+1)  # pairU[u] = v matched to u, 0 if unmatched
    pairV = [0]*(k+1)  # pairV[v] = u matched to v, 0 if unmatched
    dist = [0]*(k+1)
    
    def bfs():
        q = deque()
        for u in range(1, k+1):
            if pairU[u] == 0:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = float('inf')
        dist[0] = float('inf')
        while q:
            u = q.popleft()
            if dist[u] < dist[0]:
                for v in adj[u]:
                    if dist[pairV[v]] == float('inf'):
                        dist[pairV[v]] = dist[u] + 1
                        q.append(pairV[v])
        return dist[0] != float('inf')
    
    def dfs(u):
        if u != 0:
            for v in adj[u]:
                if dist[pairV[v]] == dist[u] + 1:
                    if dfs(pairV[v]):
                        pairV[v] = u
                        pairU[u] = v
                        return True
            dist[u] = float('inf')
            return False
        return True
    
    matching = 0
    while bfs():
        for u in range(1, k+1):
            if pairU[u] == 0:
                if dfs(u):
                    matching += 1
    
    if matching != k:
        print("NO")
        return
    
    print("YES")
    for board in range(1, k+1):
        mod = pairU[board]
        sensor = board_to_sensor[board]
        print(board, sensor, mod)

if __name__ == "__main__":
    main()