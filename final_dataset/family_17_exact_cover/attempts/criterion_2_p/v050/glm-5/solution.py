import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    q = int(next(it))
    t = int(next(it))

    # Build adjacency list for left side (command units 1..q)
    adj = [[] for _ in range(q + 1)]
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        adj[a].append(b)

    # Match array for right side (response units q+1..2q)
    # match_r[v] = u means response unit v is matched with command unit u
    match_r = [0] * (2 * q + 1)
    
    def bfs():
        dist = [-1] * (q + 1)
        dq = deque()
        for u in range(1, q + 1):
            if match_r_inv[u] == 0:
                dist[u] = 0
                dq.append(u)
        found = False
        while dq:
            u = dq.popleft()
            for v in adj[u]:
                u2 = match_r[v]
                if u2 != 0 and dist[u2] == -1:
                    dist[u2] = dist[u] + 1
                    dq.append(u2)
                elif u2 == 0:
                    found = True
        return dist, found

    def dfs(u, dist):
        for v in adj[u]:
            u2 = match_r[v]
            if u2 == 0 or (dist[u2] == dist[u] + 1 and dfs(u2, dist)):
                match_r[v] = u
                match_r_inv[u] = v
                return True
        dist[u] = -1
        return False

    # match_r_inv[u] = v means command unit u is matched with response unit v
    match_r_inv = [0] * (q + 1)
    matching_size = 0
    
    while True:
        dist, found = bfs()
        if not found:
            break
        for u in range(1, q + 1):
            if match_r_inv[u] == 0:
                if dfs(u, dist):
                    matching_size += 1

    if matching_size != q:
        print("NO")
    else:
        print("YES")
        for u in range(1, q + 1):
            print(u, match_r_inv[u])

if __name__ == "__main__":
    solve()