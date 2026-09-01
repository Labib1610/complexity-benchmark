import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[0], data[1]
    adj_mask = [0] * n

    p = 2
    for _ in range(m):
        u = data[p] - 1
        v = data[p + 1] - 1
        p += 2
        if u == v:
            print("NO")
            return
        adj_mask[u] |= 1 << v
        adj_mask[v] |= 1 << u

    adj = [[] for _ in range(n)]
    degree = [0] * n
    for v in range(n):
        mask = adj_mask[v]
        while mask:
            bit = mask & -mask
            u = bit.bit_length() - 1
            adj[v].append(u)
            mask -= bit
        degree[v] = len(adj[v])

    failed = set()
    CACHE_LIMIT = 500000

    def solve(prefix):
        color = [-1] * n
        counts = [[0, 0, 0] for _ in range(n)]
        sat = [0] * n
        used = [0, 0, 0]
        state = 0

        for v, c in enumerate(prefix):
            if counts[v][c]:
                return None

            color[v] = c
            used[c] += 1
            state |= (c + 1) << (2 * v)

            bit = 1 << c
            for u in adj[v]:
                if color[u] == -1:
                    if counts[u][c] == 0:
                        sat[u] |= bit
                    counts[u][c] += 1

        for v in range(len(prefix), n):
            if sat[v] == 7:
                return None

        def dfs(remaining, current_state):
            if remaining == 0:
                return color.copy()

            if current_state in failed:
                return None

            chosen = -1
            best_sat = -1
            best_degree = -1

            for v in range(n):
                if color[v] == -1:
                    sm = sat[v]
                    if sm == 7:
                        if len(failed) < CACHE_LIMIT:
                            failed.add(current_state)
                        return None
                    s = sm.bit_count()
                    if s > best_sat or (s == best_sat and degree[v] > best_degree):
                        best_sat = s
                        best_degree = degree[v]
                        chosen = v

            available = 7 ^ sat[chosen]
            tried_unused = False

            for c in range(3):
                bit = 1 << c
                if not (available & bit):
                    continue

                if used[c] == 0:
                    if tried_unused:
                        continue
                    tried_unused = True

                color[chosen] = c
                used[c] += 1
                changed = []
                conflict = False

                for u in adj[chosen]:
                    if color[u] == -1:
                        old = counts[u][c]
                        counts[u][c] = old + 1
                        if old == 0:
                            sat[u] |= bit
                        changed.append(u)
                        if sat[u] == 7:
                            conflict = True

                if not conflict:
                    result = dfs(
                        remaining - 1,
                        current_state | ((c + 1) << (2 * chosen))
                    )
                    if result is not None:
                        return result

                for u in changed:
                    counts[u][c] -= 1
                    if counts[u][c] == 0:
                        sat[u] &= ~bit

                used[c] -= 1
                color[chosen] = -1

            if len(failed) < CACHE_LIMIT:
                failed.add(current_state)
            return None

        return dfs(n - len(prefix), state)

    # By permuting color names, any valid coloring can have vertex 1 colored 1.
    witness = solve([0])
    if witness is None:
        print("NO")
        return

    prefix = [0]

    for i in range(1, n):
        current = witness[i]
        selected = current

        for c in range(current):
            conflict = False
            for u in adj[i]:
                if u < i and prefix[u] == c:
                    conflict = True
                    break
            if conflict:
                continue

            candidate = solve(prefix + [c])
            if candidate is not None:
                witness = candidate
                selected = c
                break

        prefix.append(selected)

    print("YES")
    print(*[c + 1 for c in prefix])

if __name__ == "__main__":
    main()