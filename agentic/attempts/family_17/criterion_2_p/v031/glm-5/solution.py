import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    q = int(next(it))
    t = int(next(it))

    # Plugs: 1..q, Sockets: q+1..2q
    # We relabel sockets to 0..q-1 for 0-indexed arrays
    # Plug p (1-indexed) -> p-1 (0-indexed)
    # Socket s (1-indexed) -> s-q-1 (0-indexed)
    
    adj = [[] for _ in range(q)]
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        u = a - 1
        v = b - q - 1
        adj[u].append(v)

    # Hopcroft-Karp
    pair_U = [-1] * q
    pair_V = [-1] * q
    dist = [0] * q

    def bfs():
        queue = deque()
        for u in range(q):
            if pair_U[u] == -1:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = -1
        
        found_augmenting_path = False
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                # If v is matched, go to its pair
                if pair_V[v] != -1:
                    if dist[pair_V[v]] == -1:
                        dist[pair_V[v]] = dist[u] + 1
                        queue.append(pair_V[v])
                else:
                    # v is unmatched, so we found a path to NIL
                    found_augmenting_path = True
        return found_augmenting_path

    def dfs(u):
        for v in adj[u]:
            if pair_V[v] == -1 or (dist[pair_V[v]] == dist[u] + 1 and dfs(pair_V[v])):
                pair_U[u] = v
                pair_V[v] = u
                return True
        dist[u] = -1 # mark as visited in this phase to avoid reprocessing
        return False

    matching_size = 0
    while bfs():
        for u in range(q):
            if pair_U[u] == -1:
                if dfs(u):
                    matching_size += 1
    
    if matching_size == q:
        sys.stdout.write("YES\n")
        for u in range(q):
            v = pair_U[u]
            sys.stdout.write(f"{u+1} {v+q+1}\n")
    else:
        sys.stdout.write("NO\n")

if __name__ == '__main__':
    solve()