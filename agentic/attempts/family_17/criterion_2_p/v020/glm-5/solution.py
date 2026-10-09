import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    q = int(next(it))
    t = int(next(it))
    
    adj = [[] for _ in range(q + 1)]
    
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        adj[a].append(b)
    
    # The alkaline IDs are q+1 to 2q, representing match states 0 to q-1 for left side
    match_alkali = [0] * (2 * q + 1)  # match_alkali[b] = acid matched with b (or 0)
    match_acid = [0] * (q + 1)        # match_acid[a] = alkali matched with a (or 0)
    
    def bfs():
        dist = [-1] * (q + 1)
        dq = deque()
        for u in range(1, q + 1):
            if match_acid[u] == 0:
                dist[u] = 0
                dq.append(u)
        found = False
        while dq:
            u = dq.popleft()
            for v in adj[u]:
                u2 = match_alkali[v]
                if u2 != 0 and dist[u2] == -1:
                    dist[u2] = dist[u] + 1
                    dq.append(u2)
        return dist
    
    def dfs(u, dist):
        for v in adj[u]:
            u2 = match_alkali[v]
            if u2 == 0:
                match_acid[u] = v
                match_alkali[v] = u
                return True
            elif dist[u2] == dist[u] + 1 and dfs(u2, dist):
                match_acid[u] = v
                match_alkali[v] = u
                return True
        return False
    
    matching = 0
    while True:
        dist = bfs()
        progress = False
        for u in range(1, q + 1):
            if match_acid[u] == 0 and dfs(u, dist):
                matching += 1
                progress = True
        if not progress:
            break
    
    if matching == q:
        print("YES")
        for a in range(1, q + 1):
            print(f"{a} {match_acid[a]}")
    else:
        print("NO")

solve()