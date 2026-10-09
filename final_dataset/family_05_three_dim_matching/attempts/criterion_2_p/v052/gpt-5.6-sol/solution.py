import sys
from collections import deque

sys.setrecursionlimit(10000)

def main():
    data = sys.stdin.buffer
    first = data.readline().split()
    if not first:
        return

    k, t = map(int, first)

    adj = [[] for _ in range(k + 1)]
    cruiser_of = [0] * (k + 1)
    captain_of = [0] * (k + 1)

    match_captain = [0] * (k + 1)
    match_sector = [0] * (k + 1)
    matched = 0
    valid = True

    for _ in range(t):
        c, v, s = map(int, data.readline().split())
        adj[c].append(s)

        if cruiser_of[c] == 0:
            cruiser_of[c] = v
        elif cruiser_of[c] != v:
            valid = False

        if captain_of[v] == 0:
            captain_of[v] = c
        elif captain_of[v] != c:
            valid = False

        if match_captain[c] == 0 and match_sector[s] == 0:
            match_captain[c] = s
            match_sector[s] = c
            matched += 1

    if not valid or any(cruiser_of[c] == 0 for c in range(1, k + 1)):
        print("NO")
        return

    dist = [0] * (k + 1)
    inf = k + 1

    def bfs():
        q = deque()
        for c in range(1, k + 1):
            if match_captain[c] == 0:
                dist[c] = 0
                q.append(c)
            else:
                dist[c] = inf

        shortest = inf
        while q:
            c = q.popleft()
            if dist[c] >= shortest:
                continue

            next_dist = dist[c] + 1
            for s in adj[c]:
                other = match_sector[s]
                if other == 0:
                    shortest = next_dist
                elif dist[other] == inf:
                    dist[other] = next_dist
                    q.append(other)

        return shortest

    def dfs(c, shortest):
        next_dist = dist[c] + 1
        for s in adj[c]:
            other = match_sector[s]
            if other == 0:
                if next_dist == shortest:
                    match_captain[c] = s
                    match_sector[s] = c
                    return True
            elif dist[other] == next_dist and dfs(other, shortest):
                match_captain[c] = s
                match_sector[s] = c
                return True

        dist[c] = inf
        return False

    while matched < k:
        shortest = bfs()
        if shortest == inf:
            break

        for c in range(1, k + 1):
            if match_captain[c] == 0 and dfs(c, shortest):
                matched += 1

    if matched != k:
        print("NO")
        return

    output = ["YES"]
    output.extend(
        f"{c} {cruiser_of[c]} {match_captain[c]}"
        for c in range(1, k + 1)
    )
    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()