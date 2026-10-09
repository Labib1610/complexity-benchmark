import sys

# Increase recursion depth for deep DFS calls
sys.setrecursionlimit(300000)

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

    # We need to find a perfect matching in a bipartite graph.
    # Left side: ground arrays 1..q (indices 0..q-1)
    # Right side: orbital relays q+1..2q.
    # To use Hopcroft-Karp efficiently, we can compress the relay IDs.
    # Map relay ID b to index b - (q + 1) (range 0..q-1).

    adj = [[] for _ in range(q)]
    for _ in range(t):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - (q + 1)
        adj[u].append(v)

    # Hopcroft-Karp Algorithm
    INF = q + 10
    
    # pair_U[u] stores the relay matched with ground array u
    pair_U = [-1] * q
    # pair_V[v] stores the ground array matched with relay v
    pair_V = [-1] * q
    # dist[u] is the distance in BFS layering
    dist = [0] * q

    def bfs():
        queue = []
        for u in range(q):
            if pair_U[u] == -1:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = INF
        
        found_augmenting_path = False
        
        idx = 0
        while idx < len(queue):
            u = queue[idx]
            idx += 1
            
            for v in adj[u]:
                # If v is matched, explore its match next
                if pair_V[v] != -1:
                    if dist[pair_V[v]] == INF:
                        dist[pair_V[v]] = dist[u] + 1
                        queue.append(pair_V[v])
                else:
                    # We found a free node in V, so an augmenting path exists
                    found_augmenting_path = True
            
        return found_augmenting_path

    def dfs(u):
        for v in adj[u]:
            if pair_V[v] == -1 or (dist[pair_V[v]] == dist[u] + 1 and dfs(pair_V[v])):
                pair_U[u] = v
                pair_V[v] = u
                return True
        
        dist[u] = INF
        return False

    matching = 0
    while bfs():
        for u in range(q):
            if pair_U[u] == -1:
                if dfs(u):
                    matching += 1
    
    if matching == q:
        sys.stdout.write("YES\n")
        for u in range(q):
            v_original = pair_U[u] + (q + 1)
            u_original = u + 1
            sys.stdout.write(f"{u_original} {v_original}\n")
    else:
        sys.stdout.write("NO\n")

if __name__ == '__main__':
    solve()