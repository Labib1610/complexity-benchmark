import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    
    color = [-1] * n
    cnt0 = 0
    cnt1 = 0
    for i in range(n):
        if color[i] == -1:
            color[i] = 0
            cnt0 += 1
            q = deque([i])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        if color[v] == 0:
                            cnt0 += 1
                        else:
                            cnt1 += 1
                        q.append(v)
    
    if k > max(cnt0, cnt1):
        print("NO")
        return
    
    # pick from larger color class
    if cnt0 >= cnt1:
        chosen = [i+1 for i in range(n) if color[i] == 0][:k]
    else:
        chosen = [i+1 for i in range(n) if color[i] == 1][:k]
    
    print("YES")
    print(" ".join(map(str, chosen)))

if __name__ == "__main__":
    solve()