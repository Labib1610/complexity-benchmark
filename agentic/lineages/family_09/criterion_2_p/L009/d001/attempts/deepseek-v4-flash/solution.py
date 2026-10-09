import sys
from collections import deque

input = sys.stdin.readline

def hopcroft_karp(n, adj, U):
    pairU = [-1] * n
    pairV = [-1] * n
    dist = [0] * n

    def bfs():
        q = deque()
        for u in U:
            if pairU[u] == -1:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = float('inf')
        found = False
        while q:
            u = q.popleft()
            for v in adj[u]:
                pu = pairV[v]
                if pu != -1 and dist[pu] == float('inf'):
                    dist[pu] = dist[u] + 1
                    q.append(pu)
                elif pu == -1:
                    found = True
        return found

    def dfs(u):
        for v in adj[u]:
            pu = pairV[v]
            if pu == -1 or (dist[pu] == dist[u] + 1 and dfs(pu)):
                pairU[u] = v
                pairV[v] = u
                return True
        dist[u] = float('inf')
        return False

    matching = 0
    while bfs():
        for u in U:
            if pairU[u] == -1 and dfs(u):
                matching += 1
    return matching, pairU, pairV

def main():
    n, m, k = map(int, input().split())
    adj = [[] for _ in range(n)]
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))

    # Bipartite coloring
    color = [-1] * n
    left = []
    right = []
    for i in range(n):
        if color[i] == -1:
            color[i] = 0
            q = deque([i])
            left.append(i)
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        if color[v] == 0:
                            left.append(v)
                        else:
                            right.append(v)
                        q.append(v)

    # Build adjacency from left to right only
    adj_left = [[] for _ in range(n)]
    for u, v in edges:
        if color[u] == 0:
            adj_left[u].append(v)
        else:
            adj_left[v].append(u)

    matching_size, pairU, pairV = hopcroft_karp(n, adj_left, left)

    max_independent = n - matching_size
    if k > max_independent:
        print("NO")
        return

    # Build independent set
    chosen = [False] * n
    # Take all unmatched left vertices
    for u in left:
        if pairU[u] == -1:
            chosen[u] = True
    # Take all unmatched right vertices
    for v in right:
        if pairV[v] == -1:
            chosen[v] = True

    # Now we have a maximum independent set (size = max_independent)
    # We need exactly k, so remove extras if too many
    indep = [i for i in range(n) if chosen[i]]
    if len(indep) > k:
        indep = indep[:k]
    elif len(indep) < k:
        # Add more from the remaining vertices that are not adjacent to chosen
        chosen_set = set(indep)
        for i in range(n):
            if len(indep) == k:
                break
            if i not in chosen_set:
                # check if adding i keeps independent
                ok = True
                for v in adj[i]:
                    if v in chosen_set:
                        ok = False
                        break
                if ok:
                    indep.append(i)
                    chosen_set.add(i)

    print("YES")
    print(" ".join(str(x+1) for x in indep))

if __name__ == "__main__":
    main()