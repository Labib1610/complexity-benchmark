import sys
import collections

def solve():
    # Read all input
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        q = int(next(iterator))
        t = int(next(iterator))
    except StopIteration:
        return

    # Build adjacency list for modules 1..q (left side) and q+1..2q (right side)
    # We use zero-indexed or 1-indexed consistently.
    # Let's use 1-indexed modules, but for right side nodes in graph algorithms,
    # we might map them to a continuous range [1, q].
    
    # adj[u] for u in 1..q stores list of v (modules in q+1..2q)
    adj = [[] for _ in range(q + 1)]
    
    # Since we need to output specific edges, we need to track edge indices or store edges
    # and match them back. Storing original edge index is safer.
    # Format: adj[u].append(v)
    
    has_edge = [[False] * (q + 1) for _ in range(q + 1)] # Too large memory for q=100k
    
    # Optimization: For each left node u (1..q), we just need to store neighbors.
    # For matching, we don't need to check duplicates explicitly as multiple edges 
    # between same pair behave as one for matching purposes.
    
    edges = []
    for i in range(t):
        a = int(next(iterator))
        b = int(next(iterator))
        # Map b to 1..q range: b - q
        v_mapped = b - q
        adj[a].append(v_mapped)
        edges.append((a, b))
    
    # Hopcroft-Karp Algorithm to find maximum matching
    # matchL[u]: matched right-node for left-node u (1..q)
    # matchR[v]: matched left-node for right-node v (1..q)
    # dist[u]: distance for BFS in layered graph
    
    INF = float('inf')
    matchL = [0] * (q + 1)
    matchR = [0] * (q + 1)
    dist = [0] * (q + 1)
    
    def bfs():
        queue = collections.deque()
        for u in range(1, q + 1):
            if matchL[u] == 0:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = INF
        
        found_augmenting_path = False
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                u2 = matchR[v]
                if u2 != 0:
                    if dist[u2] == INF:
                        dist[u2] = dist[u] + 1
                        queue.append(u2)
                else:
                    # Found a free node on the right, so a path exists
                    found_augmenting_path = True
        return found_augmenting_path

    def dfs(u):
        for v in adj[u]:
            u2 = matchR[v]
            if u2 == 0 or (dist[u2] == dist[u] + 1 and dfs(u2)):
                matchL[u] = v
                matchR[v] = u
                return True
        dist[u] = INF
        return False

    matching = 0
    while bfs():
        for u in range(1, q + 1):
            if matchL[u] == 0:
                if dfs(u):
                    matching += 1
    
    if matching != q:
        sys.stdout.write("NO\n")
    else:
        sys.stdout.write("YES\n")
        # Output the edges corresponding to the matching
        # matchL[u] gives the mapped right-node index (1..q)
        # Original module ID is matchL[u] + q
        
        # To output a valid edge from input, we iterate input edges and check if 
        # it belongs to the matching set.
        matched_edges = set()
        for u in range(1, q + 1):
            if matchL[u] != 0:
                matched_edges.add((u, matchL[u]))
        
        # We need to print exactly q edges. The matching found gives q pairs (u, v_mapped).
        # Any input edge with these endpoints is valid.
        # Since the matching is perfect, we know for each u, there is a match.
        # We iterate through stored edges and print if they match.
        count = 0
        for a, b in edges:
            if matchL[a] == b - q:
                sys.stdout.write(f"{a} {b}\n")
                count += 1
                if count == q:
                    break

if __name__ == "__main__":
    solve()