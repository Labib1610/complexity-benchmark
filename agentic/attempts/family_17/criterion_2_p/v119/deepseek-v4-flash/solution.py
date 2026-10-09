import sys
from collections import deque

input = sys.stdin.readline

def hopcroft_karp(n, adj, m):
    # n = number of nodes on left (Zone A)
    # m = number of nodes on right (Zone B)
    pair_u = [-1] * (n + 1)
    pair_v = [-1] * (m + 1)
    dist = [0] * (n + 1)

    def bfs():
        q = deque()
        for u in range(1, n + 1):
            if pair_u[u] == -1:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = float('inf')
        found = False
        while q:
            u = q.popleft()
            for v in adj[u]:
                pu = pair_v[v]
                if pu != -1 and dist[pu] == float('inf'):
                    dist[pu] = dist[u] + 1
                    q.append(pu)
                elif pu == -1:
                    found = True
        return found

    def dfs(u):
        for v in adj[u]:
            pu = pair_v[v]
            if pu == -1 or (dist[pu] == dist[u] + 1 and dfs(pu)):
                pair_u[u] = v
                pair_v[v] = u
                return True
        dist[u] = float('inf')
        return False

    matching = 0
    while bfs():
        for u in range(1, n + 1):
            if pair_u[u] == -1 and dfs(u):
                matching += 1
    return matching, pair_u

def main():
    q, t = map(int, input().split())
    adj = [[] for _ in range(q + 1)]
    for _ in range(t):
        a, b = map(int, input().split())
        adj[a].append(b - q)  # store as 1..q for right side

    matching, pair_u = hopcroft_karp(q, adj, q)
    if matching != q:
        print("NO")
    else:
        print("YES")
        for u in range(1, q + 1):
            v = pair_u[u] + q
            print(u, v)

if __name__ == "__main__":
    main()