import sys
from array import array

sys.setrecursionlimit(10000)

def main():
    inp = sys.stdin.buffer
    first = inp.readline().split()
    if not first:
        return

    k, t = map(int, first)
    adj = [array('H') for _ in range(k)]
    machine = [-1] * k

    for _ in range(t):
        x, y, z = map(int, inp.readline().split())
        x -= 1
        if machine[x] == -1:
            machine[x] = y
        adj[x].append(z - 1)

    pair_u = [-1] * k
    pair_v = [-1] * k
    matched = 0

    # Initial greedy matching.
    for u in range(k):
        for v in adj[u]:
            if pair_v[v] == -1:
                pair_u[u] = v
                pair_v[v] = u
                matched += 1
                break

    dist = [-1] * k

    while matched < k:
        queue = [0] * k
        head = 0
        tail = 0

        for u in range(k):
            if pair_u[u] == -1:
                dist[u] = 0
                queue[tail] = u
                tail += 1
            else:
                dist[u] = -1

        shortest = k + 1

        while head < tail:
            u = queue[head]
            head += 1
            nd = dist[u] + 1

            if nd > shortest:
                continue

            for v in adj[u]:
                next_u = pair_v[v]
                if next_u == -1:
                    if nd < shortest:
                        shortest = nd
                elif nd < shortest and dist[next_u] == -1:
                    dist[next_u] = nd
                    queue[tail] = next_u
                    tail += 1

        if shortest == k + 1:
            break

        ptr = [0] * k

        def dfs(u):
            edges = adj[u]
            while ptr[u] < len(edges):
                v = edges[ptr[u]]
                ptr[u] += 1
                next_u = pair_v[v]

                if next_u == -1:
                    if dist[u] + 1 == shortest:
                        pair_u[u] = v
                        pair_v[v] = u
                        return True
                elif dist[next_u] == dist[u] + 1 and dfs(next_u):
                    pair_u[u] = v
                    pair_v[v] = u
                    return True

            dist[u] = -1
            return False

        added = 0
        for u in range(k):
            if pair_u[u] == -1 and dfs(u):
                added += 1

        if added == 0:
            break
        matched += added

    if matched != k:
        sys.stdout.write("NO\n")
        return

    out = ["YES"]
    for u in range(k):
        out.append(f"{u + 1} {machine[u]} {pair_u[u] + 1}")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()