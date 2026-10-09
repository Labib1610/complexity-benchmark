import sys
import collections

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        adj[u].append(v)
        adj[v].append(u)

    # We want the lexicographically smallest assignment.
    # Since 1 < 2, we want to assign 1 to projector i if possible.
    # This is equivalent to finding the assignment that minimizes the number of 2s,
    # or equivalently, maximizes the number of 1s.
    # This problem is equivalent to finding the minimum vertex cover in a bipartite graph,
    # or finding the maximum independent set.
    # The set of vertices assigned 1 forms an independent set (no edges between them).
    # To maximize the number of 1s, we need the maximum independent set.
    # In a bipartite graph, |Max Independent Set| = |V| - |Min Vertex Cover|.
    # By Konig's Theorem, |Min Vertex Cover| = |Max Matching|.
    # So, we find the maximum matching, derive the minimum vertex cover, and the
    # complement of the vertex cover is the maximum independent set.
    # Vertices in the independent set are assigned 1, others 2.
    
    # First, check if the graph is bipartite and partition the vertices.
    color = [-1] * n
    is_bipartite = True
    for i in range(n):
        if color[i] == -1:
            color[i] = 0
            queue = collections.deque([i])
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        is_bipartite = False
                        break
                if not is_bipartite:
                    break
        if not is_bipartite:
            break

    if not is_bipartite:
        print("NO")
        return

    # Build bipartite graph for matching
    # Left set: color 0, Right set: color 1
    pair_U = [-1] * n
    pair_V = [-1] * n
    dist = [0] * n

    def bfs():
        queue = collections.deque()
        for u in range(n):
            if color[u] == 0 and pair_U[u] == -1:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = -1
        
        found_augmenting_path = False
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                # v must be in the other partition
                # u is in set U (color 0), so v must be in set V (color 1)
                # This is guaranteed by bipartiteness check
                if pair_V[v] != -1:
                    if dist[pair_V[v]] == -1:
                        dist[pair_V[v]] = dist[u] + 1
                        queue.append(pair_V[v])
                else:
                    found_augmenting_path = True
        return found_augmenting_path

    def dfs(u):
        for v in adj[u]:
            if pair_V[v] == -1 or (dist[pair_V[v]] == dist[u] + 1 and dfs(pair_V[v])):
                pair_U[u] = v
                pair_V[v] = u
                return True
        dist[u] = -1
        return False

    # Hopcroft-Karp
    matching = 0
    while bfs():
        for u in range(n):
            if color[u] == 0 and pair_U[u] == -1:
                if dfs(u):
                    matching += 1
    
    # Find Minimum Vertex Cover using Konig's Theorem
    # Z = set of vertices reachable by alternating paths from unmatched vertices in U
    # Min Vertex Cover = (U \ Z) U (V intersect Z)
    # We want the complement: (U intersect Z) U (V \ Z)
    # These are the vertices we assign 1.
    
    reachable_from_unmatched_U = [False] * n
    
    queue = collections.deque()
    for u in range(n):
        if color[u] == 0 and pair_U[u] == -1:
            reachable_from_unmatched_U[u] = True
            queue.append(u)
    
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            # u is in U, v is in V
            if pair_V[v] != -1 and not reachable_from_unmatched_U[pair_V[v]]:
                reachable_from_unmatched_U[pair_V[v]] = True
                queue.append(pair_V[v])
                
    result = [2] * n
    for u in range(n):
        if color[u] == 0:
            if reachable_from_unmatched_U[u]:
                result[u] = 1
        else:
            # color[u] == 1 (V set)
            # We need V \ Z
            # Z contains v if reachable_from_unmatched_U[v] is true?
            # No, Z is defined on U vertices.
            # v is in Z if it is reachable.
            # v is reachable if it is matched to a reachable u.
            # Actually, simpler logic:
            # Min Vertex Cover K = (U \ Z) U (V intersect Z)
            # We want complement V \ K = (U intersect Z) U (V \ Z)
            # U vertices in Z get 1.
            # V vertices NOT in Z get 1.
            # V vertices are in Z if they are reachable.
            # v is reachable if pair_V[v] is reachable.
            if pair_V[v] != -1 and reachable_from_unmatched_U[pair_V[v]]:
                pass # v is in Z, so in K, so result is 2
            else:
                result[v] = 1

    print("YES")
    print(*(result))

if __name__ == '__main__':
    solve()