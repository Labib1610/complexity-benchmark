import sys
from collections import deque

def main():
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * n
    sides = [[], []]
    for i in range(n):
        if color[i] == -1:
            color[i] = 0
            sides[0].append(i)
            q = deque([i])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        sides[color[v]].append(v)
                        q.append(v)

    # Maximum independent set size = n - maximum matching
    # But we can also just take the larger color class as a starting independent set.
    # We can always adjust size by moving vertices from the other side if they have no conflicts with chosen ones.
    # Simpler: take the larger side, then add vertices from the other side that have no edges to chosen ones.
    # But to get exactly k, we can just take the larger side and then add from the other side if possible.

    # Actually, in a bipartite graph, the maximum independent set can be built by taking all vertices of one side
    # and then adding vertices from the other side that have no neighbors in the chosen set.
    # But for exact k, we can just take the larger side and then add from the other side if possible.

    # Let's just take the larger side first.
    if len(sides[0]) < len(sides[1]):
        sides[0], sides[1] = sides[1], sides[0]

    chosen = set(sides[0])
    # Try to add from the other side
    for v in sides[1]:
        if len(chosen) == k:
            break
        if all(u not in chosen for u in adj[v]):
            chosen.add(v)

    if len(chosen) < k:
        # We can also remove from chosen and add from other side to adjust size.
        # But if max independent set >= k, we can always get exactly k.
        # Let's compute max independent set size via Hopcroft-Karp.
        # But simpler: we can just remove from chosen until size k if we have enough.
        # Actually if max independent set >= k, we can always shrink.
        # So we just need to check if max independent set >= k.
        # Let's compute maximum matching.

        # Hopcroft-Karp
        from collections import deque

        pair_u = [-1] * n
        pair_v = [-1] * n
        dist = [0] * n

        def bfs():
            q = deque()
            for u in sides[0]:
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
            for u in sides[0]:
                if pair_u[u] == -1 and dfs(u):
                    matching += 1

        max_independent = n - matching
        if max_independent < k:
            print("NO")
            return

        # Build an independent set of size k
        # Take all vertices from sides[0] not matched, then add from sides[1] not matched,
        # then add from matched vertices carefully.
        # Standard construction: take all free vertices from left, then all free from right,
        # then for each matched edge, take the right vertex.
        # This gives maximum independent set.
        # Then we can remove vertices to get exactly k.

        left_free = [u for u in sides[0] if pair_u[u] == -1]
        right_free = [v for v in sides[1] if pair_v[v] == -1]
        ind_set = set(left_free + right_free)
        for u in sides[0]:
            if pair_u[u] != -1:
                v = pair_u[u]
                ind_set.add(v)  # take right side of matched edge

        # Now ind_set is a maximum independent set. We can remove elements to get size k.
        ind_set = list(ind_set)
        # Remove until size k
        chosen = set(ind_set[:k])
        print("YES")
        print(" ".join(str(x+1) for x in sorted(chosen)))
        return

    print("YES")
    print(" ".join(str(x+1) for x in sorted(chosen)[:k]))

if __name__ == "__main__":
    main()