import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    try:
        q = int(next(iterator))
        t = int(next(iterator))
    except StopIteration:
        return

    adj = [[] for _ in range(q + 1)]
    
    # Indices for pairing edges to their reverse
    # For edge index 2*i, its pair is 2*i + 1
    # Pair(u, v) match id: 2*i
    # Pair(v, u) match id: 2*i + 1
    
    match_from_u = [0] * (q + 1)
    match_from_v = [0] * (q * 2 + 1)

    for _ in range(t):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)

    def bfs():
        # dist[u] is distance to free u, or 0 if not reachable
        dist = [0] * (q + 1)
        queue = deque()
        for u in range(1, q + 1):
            if match_from_u[u] == 0:
                dist[u] = 1
                queue.append(u)
            else:
                dist[u] = 0
        
        found = False
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                # If v is matched, we can go to its partner u'
                u_prime = match_from_v[v]
                if u_prime != 0:
                    if dist[u_prime] == 0:
                        dist[u_prime] = dist[u] + 1
                        queue.append(u_prime)
                else:
                    # Found a free vertex in V
                    found = True
        return found, dist

    def dfs(u, dist):
        for v in adj[u]:
            u_prime = match_from_v[v]
            if u_prime == 0:
                # Free vertex in V
                match_from_u[u] = v
                match_from_v[v] = u
                return True
            elif dist[u] + 1 == dist[u_prime]:
                if dfs(u_prime, dist):
                    match_from_u[u] = v
                    match_from_v[v] = u
                    return True
        dist[u] = 0 # Optimization: mark as unusable for this phase
        return False

    matching_size = 0
    while True:
        found, dist = bfs()
        if not found:
            break
        
        for u in range(1, q + 1):
            if match_from_u[u] == 0:
                if dfs(u, dist):
                    matching_size += 1
    
    if matching_size == q:
        sys.stdout.write("YES\n")
        for u in range(1, q + 1):
            sys.stdout.write(f"{u} {match_from_u[u]}\n")
    else:
        sys.stdout.write("NO\n")

if __name__ == '__main__':
    solve()