import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    
    n, m = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u, v = map(int, input().split())
        if u == v:
            print("NO")
            return
        adj[u].append(v)
        adj[v].append(u)
    
    assignment = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if assignment[i] == 0:
            queue = deque([i])
            assignment[i] = 1
            
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if assignment[v] == 0:
                        assignment[v] = 3 - assignment[u]
                        queue.append(v)
                    elif assignment[v] == assignment[u]:
                        print("NO")
                        return
    
    print("YES")
    print(" ".join(map(str, assignment[1:])))

solve()