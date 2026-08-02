import sys
from collections import deque


def main():
    # Hopcroft-Karp bipartite matching, O(E*sqrt(V)). Repeatedly BFS to build the
    # layered graph of shortest augmenting paths, then DFS to augment along many
    # vertex-disjoint shortest paths at once. A perfect assignment exists iff all k
    # workers are matched. (The judge is custom and accepts ANY valid assignment.)
    data = sys.stdin.buffer.read().split()
    idx = 0
    k = int(data[idx]); idx += 1
    e = int(data[idx]); idx += 1
    adj = [[] for _ in range(k + 1)]
    for _ in range(e):
        x = int(data[idx]); y = int(data[idx + 1]); idx += 2
        adj[x].append(y)

    INF = float("inf")
    match_x = [0] * (k + 1)      # worker -> task
    match_y = [0] * (k + 1)      # task -> worker
    dist = [0] * (k + 1)

    def bfs():
        q = deque()
        for x in range(1, k + 1):
            if match_x[x] == 0:
                dist[x] = 0; q.append(x)
            else:
                dist[x] = INF
        reachable_free = False
        while q:
            x = q.popleft()
            for y in adj[x]:
                w = match_y[y]
                if w == 0:
                    reachable_free = True
                elif dist[w] == INF:
                    dist[w] = dist[x] + 1
                    q.append(w)
        return reachable_free

    def dfs(x):
        for y in adj[x]:
            w = match_y[y]
            if w == 0 or (dist[w] == dist[x] + 1 and dfs(w)):
                match_x[x] = y; match_y[y] = x
                return True
        dist[x] = INF
        return False

    matched = 0
    while bfs():
        for x in range(1, k + 1):
            if match_x[x] == 0 and dfs(x):
                matched += 1

    if matched < k:
        sys.stdout.write("NO\n")
        return
    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(str(match_x[x]) for x in range(1, k + 1)) + "\n")


main()
