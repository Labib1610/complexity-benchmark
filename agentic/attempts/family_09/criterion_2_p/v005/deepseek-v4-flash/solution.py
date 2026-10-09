import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    
    color = [-1] * (n + 1)
    camp0 = []
    camp1 = []
    
    for i in range(1, n + 1):
        if color[i] == -1:
            color[i] = 0
            camp0.append(i)
            q = deque([i])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        if color[v] == 0:
                            camp0.append(v)
                        else:
                            camp1.append(v)
                        q.append(v)
    
    if len(camp0) >= k:
        print("YES")
        print(" ".join(map(str, camp0[:k])))
    elif len(camp1) >= k:
        print("YES")
        print(" ".join(map(str, camp1[:k])))
    else:
        print("NO")

if __name__ == "__main__":
    solve()