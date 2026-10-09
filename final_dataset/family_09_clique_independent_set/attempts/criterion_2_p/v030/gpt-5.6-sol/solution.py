import sys
from collections import deque

def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))

    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)

    del data, it

    color = [-1] * n
    left = []
    right = []

    for start in range(n):
        if color[start] != -1:
            continue
        color[start] = 0
        q = deque([start])
        while q:
            u = q.popleft()
            if color[u] == 0:
                left.append(u)
            else:
                right.append(u)
            nc = color[u] ^ 1
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = nc
                    q.append(v)

    if len(left) >= k:
        ans = left[:k]
        sys.stdout.write("YES\n" + " ".join(str(x + 1) for x in ans))
        return

    if len(right) >= k:
        ans = right[:k]
        sys.stdout.write("YES\n" + " ".join(str(x + 1) for x in ans))
        return

    mate = [-1] * n
    matching = 0
    impossible_threshold = n - k

    while True:
        dist = [-1] * n
        q = deque()

        for u in left:
            if mate[u] == -1:
                dist[u] = 0
                q.append(u)

        shortest = n + 1

        while q:
            u = q.popleft()
            if dist[u] + 1 > shortest:
                continue
            next_dist = dist[u] + 1
            for v in adj[u]:
                w = mate[v]
                if w == -1:
                    if next_dist < shortest:
                        shortest = next_dist
                elif next_dist < shortest and dist[w] == -1:
                    dist[w] = next_dist
                    q.append(w)

        if shortest == n + 1:
            break

        ptr = [0] * n
        augmented_this_phase = 0

        for root in left:
            if mate[root] != -1 or dist[root] != 0:
                continue

            stack_u = [root]
            stack_v = []
            success = False

            while stack_u:
                u = stack_u[-1]
                found_next = False
                neighbors = adj[u]

                while ptr[u] < len(neighbors):
                    v = neighbors[ptr[u]]
                    ptr[u] += 1
                    w = mate[v]

                    if w == -1:
                        if dist[u] + 1 != shortest:
                            continue

                        mate[u] = v
                        mate[v] = u

                        for i in range(len(stack_v) - 1, -1, -1):
                            pu = stack_u[i]
                            pv = stack_v[i]
                            mate[pu] = pv
                            mate[pv] = pu

                        success = True
                        break

                    if dist[w] == dist[u] + 1:
                        stack_v.append(v)
                        stack_u.append(w)
                        found_next = True
                        break

                if success:
                    break

                if not found_next:
                    dist[u] = -1
                    stack_u.pop()
                    if stack_u:
                        stack_v.pop()

            if success:
                matching += 1
                augmented_this_phase += 1
                if matching > impossible_threshold:
                    sys.stdout.write("NO")
                    return

        if augmented_this_phase == 0:
            break

    if n - matching < k:
        sys.stdout.write("NO")
        return

    reachable_left = bytearray(n)
    reachable_right = bytearray(n)
    q = deque()

    for u in left:
        if mate[u] == -1:
            reachable_left[u] = 1
            q.append(u)

    while q:
        u = q.popleft()
        matched_v = mate[u]
        for v in adj[u]:
            if v == matched_v or reachable_right[v]:
                continue
            reachable_right[v] = 1
            w = mate[v]
            if w != -1 and not reachable_left[w]:
                reachable_left[w] = 1
                q.append(w)

    ans = []
    for u in left:
        if reachable_left[u]:
            ans.append(u)
            if len(ans) == k:
                break

    if len(ans) < k:
        for v in right:
            if not reachable_right[v]:
                ans.append(v)
                if len(ans) == k:
                    break

    sys.stdout.write("YES\n" + " ".join(str(x + 1) for x in ans))

if __name__ == "__main__":
    main()