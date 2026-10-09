import sys
from collections import deque

def main():
    input = sys.stdin.readline
    q, t = map(int, input().split())
    adj = [[] for _ in range(q)]
    for _ in range(t):
        a, b = map(int, input().split())
        adj[a-1].append(b - q - 1)  # map b to 0..q-1

    n_left = q
    n_right = q

    pair_U = [-1] * n_left
    pair_V = [-1] * n_right
    dist = [0] * n_left

    INF = 10**9

    def bfs():
        dq = deque()
        for u in range(n_left):
            if pair_U[u] == -1:
                dist[u] = 0
                dq.append(u)
            else:
                dist[u] = INF
        found = False
        while dq:
            u = dq.popleft()
            for v in adj[u]:
                pu = pair_V[v]
                if pu != -1 and dist[pu] == INF:
                    dist[pu] = dist[u] + 1
                    dq.append(pu)
                elif pu == -1:
                    found = True
        return found

    def dfs(u):
        for v in adj[u]:
            pu = pair_V[v]
            if pu == -1 or (dist[pu] == dist[u] + 1 and dfs(pu)):
                pair_U[u] = v
                pair_V[v] = u
                return True
        dist[u] = INF
        return False

    matching = 0
    while bfs():
        for u in range(n_left):
            if pair_U[u] == -1 and dfs(u):
                matching += 1

    if matching != q:
        print("NO")
        return

    print("YES")
    for u in range(q):
        v = pair_U[u]
        print(u + 1, v + q + 1)

if __name__ == "__main__":
    main()