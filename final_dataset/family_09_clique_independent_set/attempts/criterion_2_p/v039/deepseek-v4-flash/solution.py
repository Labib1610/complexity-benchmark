import sys
from collections import deque

def main():
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
    dept = [[], []]
    
    for i in range(n):
        if color[i] == -1:
            color[i] = 0
            dept[0].append(i)
            q = deque([i])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        dept[color[v]].append(v)
                        q.append(v)
    
    # Choose the larger department
    if len(dept[0]) >= k:
        chosen = dept[0][:k]
    elif len(dept[1]) >= k:
        chosen = dept[1][:k]
    else:
        print("NO")
        return
    
    print("YES")
    print(" ".join(str(x+1) for x in chosen))

if __name__ == "__main__":
    main()