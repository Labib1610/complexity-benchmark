import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    q = int(next(iterator))
    t = int(next(iterator))

    # Controllers: 1..q, Platforms: q+1..2q
    # Remap platforms to 0-indexed: platform b -> b - q - 1 (range 0..q-1)
    # Controllers 1..q -> 0..q-1
    
    adj = [[] for _ in range(q)]
    # Store edges for output reconstruction
    edges = []
    
    for _ in range(t):
        u = int(next(iterator))
        v = int(next(iterator))
        u0 = u - 1
        v0 = v - q - 1
        adj[u0].append(v0)
        edges.append((u0, v0))
    
    # Hopcroft-Karp Algorithm
    pair_u = [-1] * q
    pair_v = [-1] * q
    dist = [0] * q
    
    def bfs():
        queue = deque()
        for u in range(q):
            if pair_u[u] == -1:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = -1
        
        found_augmenting_path = False
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                pu = pair_v[v]
                if pu != -1:
                    if dist[pu] == -1:
                        dist[pu] = dist[u] + 1
                        queue.append(pu)
                else:
                    found_augmenting_path = True
        return found_augmenting_path

    def dfs(u):
        for v in adj[u]:
            pu = pair_v[v]
            if pu == -1 or (dist[pu] == dist[u] + 1 and dfs(pu)):
                pair_u[u] = v
                pair_v[v] = u
                return True
        dist[u] = -1
        return False

    matching_size = 0
    while bfs():
        for u in range(q):
            if pair_u[u] == -1:
                if dfs(u):
                    matching_size += 1
    
    if matching_size != q:
        print("NO")
    else:
        print("YES")
        # Reconstruct the matching edges to output
        # We need to output the edges in some order.
        # The problem asks for q lines.
        # We can iterate through controllers 1..q and print their match.
        # To ensure we output valid edges from the input, we can check.
        # Since it's a valid matching, pair_u[u] is a valid platform.
        # We can just print u+1 and pair_u[u]+q+1.
        # The problem statement says "print q lines each with the two items of one chosen pair".
        # It doesn't strictly require the line to be identical to an input line if order differs,
        # but typically it implies the pair (u, v).
        # Let's output in controller order 1 to q.
        
        results = []
        for u in range(q):
            v = pair_u[u]
            # Convert back to 1-based
            print(f"{u + 1} {v + q + 1}")

if __name__ == '__main__':
    solve()