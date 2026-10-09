import sys
from collections import deque


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    k = int(data[idx]); t = int(data[idx + 1]); idx += 2
    Y = [0] * (k + 1)           # Y[x] = the single machine specialist x works with (functional promise)
    zopts = [[] for _ in range(k + 1)]
    for _ in range(t):
        x = int(data[idx]); y = int(data[idx + 1]); z = int(data[idx + 2]); idx += 3
        Y[x] = y
        zopts[x].append(z)

    # Each specialist is tied to exactly one machine (the machines are all distinct), so the only
    # freedom is the time slot: this is a bipartite matching between specialists (X) and slots (Z),
    # with an edge x--z whenever crew (x, Y[x], z) is allowed. A perfect matching == a valid plan.
    INF = float("inf")
    matchX = [0] * (k + 1)      # specialist -> slot
    matchZ = [0] * (k + 1)      # slot -> specialist
    dist = [0] * (k + 1)

    def bfs():
        q = deque()
        for x in range(1, k + 1):
            if matchX[x] == 0:
                dist[x] = 0; q.append(x)
            else:
                dist[x] = INF
        found = False
        while q:
            x = q.popleft()
            for z in zopts[x]:
                w = matchZ[z]
                if w == 0:
                    found = True
                elif dist[w] == INF:
                    dist[w] = dist[x] + 1; q.append(w)
        return found

    def dfs(x):
        for z in zopts[x]:
            w = matchZ[z]
            if w == 0 or (dist[w] == dist[x] + 1 and dfs(w)):
                matchX[x] = z; matchZ[z] = x
                return True
        dist[x] = INF
        return False

    matching = 0
    while bfs():
        for x in range(1, k + 1):
            if matchX[x] == 0 and dfs(x):
                matching += 1

    if matching != k:
        sys.stdout.write("NO\n")
        return

    out = ["YES"]
    out.extend(f"{x} {Y[x]} {matchX[x]}" for x in range(1, k + 1))
    sys.stdout.write("\n".join(out) + "\n")


main()
