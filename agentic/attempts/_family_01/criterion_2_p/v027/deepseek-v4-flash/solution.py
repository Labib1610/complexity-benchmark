import sys
from collections import deque

def solve():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    
    adj = [[] for _ in range(n)]
    indeg = [0] * n
    
    for _ in range(m):
        u = int(data[idx]) - 1; idx += 1
        v = int(data[idx]) - 1; idx += 1
        adj[u].append(v)
        indeg[v] += 1
    
    q = deque()
    for i in range(n):
        if indeg[i] == 0:
            q.append(i)
    
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    
    if len(order) != n:
        print("NO")
    else:
        print("YES")
        for i in range(n):
            print(i + 1, order[i] + 1)

if __name__ == "__main__":
    solve()