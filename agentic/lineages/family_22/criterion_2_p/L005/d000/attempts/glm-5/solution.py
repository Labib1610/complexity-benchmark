import sys
from collections import deque

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)
    
    for _ in range(m):
        a = int(next(it))
        b = int(next(it))
        adj[a].append(b)
        in_degree[b] += 1
    
    q = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            q.append(i)
    
    result = []
    while q:
        u = q.popleft()
        result.append(u)
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)
    
    if len(result) == n:
        print("YES")
        print(' '.join(map(str, result)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()