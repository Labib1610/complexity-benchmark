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
    shift0 = []
    shift1 = []

    for i in range(n):
        if color[i] == -1:
            color[i] = 0
            q = deque([i])
            shift0.append(i)
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        if color[v] == 0:
                            shift0.append(v)
                        else:
                            shift1.append(v)
                        q.append(v)

    if len(shift0) >= k:
        team = shift0[:k]
    elif len(shift1) >= k:
        team = shift1[:k]
    else:
        print("NO")
        return

    print("YES")
    print(" ".join(str(x + 1) for x in team))

if __name__ == "__main__":
    main()