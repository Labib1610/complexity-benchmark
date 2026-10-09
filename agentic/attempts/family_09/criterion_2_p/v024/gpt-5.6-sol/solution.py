import sys
from collections import deque

def main():
    input = sys.stdin.buffer.readline
    n, m, k = map(int, input().split())

    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * n

    for start in range(n):
        if color[start] != -1:
            continue

        color[start] = 0
        q = deque([start])
        component = []
        count0 = 0
        count1 = 0

        while q:
            u = q.popleft()
            component.append(u)
            if color[u] == 0:
                count0 += 1
            else:
                count1 += 1

            next_color = color[u] ^ 1
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = next_color
                    q.append(v)

        if count1 > count0:
            for u in component:
                color[u] ^= 1

    initial = [u for u in range(n) if color[u] == 0]
    if len(initial) >= k:
        answer = initial[:k]
        sys.stdout.write("YES\n")
        sys.stdout.write(" ".join(str(x + 1) for x in answer))
        sys.stdout.write("\n")
        return

    left = [u for u in range(n) if color[u] == 1]
    pair = [-1] * n
    dist = [-1] * n

    while True:
        q = deque()
        for u in left:
            if pair[u] == -1:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = -1

        shortest = n + 1

        while q:
            u = q.popleft()
            du = dist[u]
            if du > shortest:
                continue

            for v in adj[u]:
                w = pair[v]
                if w == -1:
                    if du < shortest:
                        shortest = du
                elif du < shortest and dist[w] == -1:
                    dist[w] = du + 1
                    q.append(w)

        if shortest == n + 1:
            break

        ptr = [0] * n
        augmented_any = False

        for root in left:
            if pair[root] != -1 or dist[root] != 0:
                continue

            stack = [root]
            path_right = []
            augmented = False

            while stack:
                u = stack[-1]
                found_step = False
                neighbors = adj[u]

                while ptr[u] < len(neighbors):
                    v = neighbors[ptr[u]]
                    ptr[u] += 1
                    w = pair[v]

                    if w == -1:
                        if dist[u] == shortest:
                            pair[u] = v
                            pair[v] = u

                            for i in range(len(path_right) - 1, -1, -1):
                                a = stack[i]
                                b = path_right[i]
                                pair[a] = b
                                pair[b] = a

                            augmented = True
                            augmented_any = True
                            break
                    elif dist[u] < shortest and dist[w] == dist[u] + 1:
                        stack.append(w)
                        path_right.append(v)
                        found_step = True
                        break

                if augmented:
                    break

                if found_step:
                    continue

                dist[u] = -1
                stack.pop()
                if path_right:
                    path_right.pop()

        if not augmented_any:
            break

    reachable_left = bytearray(n)
    reachable_right = bytearray(n)
    q = deque()

    for u in left:
        if pair[u] == -1:
            reachable_left[u] = 1
            q.append(u)

    while q:
        u = q.popleft()
        matched_v = pair[u]

        for v in adj[u]:
            if v == matched_v or reachable_right[v]:
                continue

            reachable_right[v] = 1
            w = pair[v]
            if w != -1 and not reachable_left[w]:
                reachable_left[w] = 1
                q.append(w)

    independent_set = []
    for u in range(n):
        if color[u] == 1:
            if reachable_left[u]:
                independent_set.append(u)
        else:
            if not reachable_right[u]:
                independent_set.append(u)

    if len(independent_set) < k:
        sys.stdout.write("NO\n")
    else:
        answer = independent_set[:k]
        sys.stdout.write("YES\n")
        sys.stdout.write(" ".join(str(x + 1) for x in answer))
        sys.stdout.write("\n")

if __name__ == "__main__":
    main()