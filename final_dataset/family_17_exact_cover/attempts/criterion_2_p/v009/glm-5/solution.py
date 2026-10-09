import sys
from collections import deque

# Set recursion limit for DFS in large graphs
sys.setrecursionlimit(3000000)

def solve():
    # Read all input at once for efficiency
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        q = int(next(iterator))
        t = int(next(iterator))
    except StopIteration:
        return

    # Controllers are 1..q, Platforms are q+1..2q
    # We map platforms to 0..q-1 for 0-based indexing
    # Controller c maps to c-1
    
    # Build adjacency list for the bipartite graph
    adj = [[] for _ in range(q)]
    
    for _ in range(t):
        u = int(next(iterator))
        v = int(next(iterator))
        # u is controller (1..q), v is platform (q+1..2q)
        # Add edge from u-1 to v-q-1
        adj[u - 1].append(v - q - 1)

    # Hopcroft-Karp algorithm for Maximum Bipartite Matching
    # match_u[u] stores the platform matched with controller u (0-based)
    # match_v[v] stores the controller matched with platform v (0-based)
    match_u = [-1] * q
    match_v = [-1] * q
    dist = [0] * q

    def bfs():
        queue = deque()
        for u in range(q):
            if match_u[u] == -1:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = -1
        
        found_augmenting_path = False
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                u_match = match_v[v]
                if u_match != -1:
                    if dist[u_match] == -1:
                        dist[u_match] = dist[u] + 1
                        queue.append(u_match)
                else:
                    found_augmenting_path = True
        return found_augmenting_path

    def dfs(u):
        for v in adj[u]:
            u_match = match_v[v]
            if u_match == -1 or (dist[u_match] == dist[u] + 1 and dfs(u_match)):
                match_u[u] = v
                match_v[v] = u
                return True
        dist[u] = -1
        return False

    matching_size = 0
    while bfs():
        for u in range(q):
            if match_u[u] == -1:
                if dfs(u):
                    matching_size += 1
    
    if matching_size == q:
        sys.stdout.write("YES\n")
        # Output the pairs
        # The problem requires outputting the original 1-based IDs
        # Controller u (0-based) is u+1
        # Platform v (0-based) is v+q+1
        out_lines = []
        for u in range(q):
            v = match_u[u]
            out_lines.append(f"{u + 1} {v + q + 1}")
        sys.stdout.write('\n'.join(out_lines))
        if q > 0: sys.stdout.write('\n')
    else:
        sys.stdout.write("NO\n")

if __name__ == '__main__':
    solve()