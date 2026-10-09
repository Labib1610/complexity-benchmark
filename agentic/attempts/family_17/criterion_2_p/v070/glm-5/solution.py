import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    q = int(next(it))
    t = int(next(it))
    
    # Build adjacency list: left side (1 to q) to right side (q+1 to 2q)
    adj = [[] for _ in range(q + 1)]
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        adj[a].append(b)
    
    # Match array: matchR[j] = i means right node j is matched to left node i
    # j ranges from q+1 to 2q, so we use index j - (q + 1) for 0-based array
    matchR = [0] * q  # matchR[idx] = left node matched to right node (q+1+idx)
    
    def bfs():
        dist = [-1] * (q + 1)
        queue = deque()
        for u in range(1, q + 1):
            if pairU[u] == 0:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = -1
        
        found_augmenting = False
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                # v is a right node (q+1 to 2q)
                u2 = matchR[v - (q + 1)]
                if u2 != 0:
                    if dist[u2] == -1:
                        dist[u2] = dist[u] + 1
                        queue.append(u2)
                else:
                    found_augmenting = True
        return dist, found_augmenting
    
    def dfs(u, dist):
        for v in adj[u]:
            u2 = matchR[v - (q + 1)]
            if u2 == 0 or (dist[u2] == dist[u] + 1 and dfs(u2, dist)):
                pairU[u] = v
                matchR[v - (q + 1)] = u
                return True
        dist[u] = -1
        return False
    
    pairU = [0] * (q + 1)  # pairU[u] = v (right node matched to left node u)
    
    matching = 0
    while True:
        dist, found = bfs()
        if not found:
            break
        for u in range(1, q + 1):
            if pairU[u] == 0:
                if dfs(u, dist):
                    matching += 1
    
    if matching != q:
        print("NO")
    else:
        print("YES")
        for u in range(1, q + 1):
            print(u, pairU[u])

if __name__ == "__main__":
    solve()