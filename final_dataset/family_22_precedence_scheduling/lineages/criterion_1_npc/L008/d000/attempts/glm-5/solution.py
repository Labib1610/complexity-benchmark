import sys
from collections import deque

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    M = int(next(it))
    T = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    in_deg = [0] * (n + 1)
    
    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        adj[a].append(b)
        in_deg[b] += 1
    
    # Kahn's algorithm with level assignment
    stage = [0] * (n + 1)
    q = deque()
    
    for i in range(1, n + 1):
        if in_deg[i] == 0:
            stage[i] = 1
            q.append(i)
    
    processed = 0
    
    while q:
        u = q.popleft()
        processed += 1
        for v in adj[u]:
            in_deg[v] -= 1
            if in_deg[v] == 0:
                stage[v] = stage[u] + 1
                q.append(v)
    
    if processed != n:
        print("NO")
        return
    
    # Check if any stage exceeds T
    if max(stage[1:]) > T:
        print("NO")
        return
    
    # Check capacity constraints
    stage_count = [0] * (T + 1)
    for i in range(1, n + 1):
        stage_count[stage[i]] += 1
    
    for s in range(1, T + 1):
        if stage_count[s] > M:
            print("NO")
            return
    
    print("YES")
    print(' '.join(map(str, stage[1:])))

if __name__ == "__main__":
    solve()