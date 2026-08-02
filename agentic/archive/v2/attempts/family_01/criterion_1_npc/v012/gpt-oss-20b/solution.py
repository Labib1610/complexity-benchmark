import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    # adjacency list, 0‑based indices
    adj = [[] for _ in range(n)]
    for _ in range(m):
        a = int(next(it)) - 1
        b = int(next(it)) - 1
        adj[a].append(b)
        adj[b].append(a)

    avail = [0b111] * n          # all three rooms allowed
    colour = [-1] * n            # -1 = uncoloured

    sys.setrecursionlimit(max(10000, n * 5))

    def dfs(i: int) -> bool:
        """return True when a complete colouring is found."""
        if i == n:
            return True

        # try rooms 1, 2, 3  (indices 0, 1, 2)
        for c in range(3):
            if (avail[i] >> c) & 1:          # this room still possible
                colour[i] = c
                changes = []

                mask = 1 << c
                for u in adj[i]:
                    if colour[u] == -1:       # neighbour still uncoloured
                        old = avail[u]
                        new = old & (~mask)
                        if new != old:
                            avail[u] = new
                            changes.append((u, old))

                if dfs(i + 1):
                    return True

                # backtrack
                for u, old in changes:
                    avail[u] = old
                colour[i] = -1
        return False

    if dfs(0):
        print("YES")
        # convert 0‑based colour to 1‑based rooms
        print(" ".join(str(c + 1) for c in colour))
    else:
        print("NO")


if __name__ == "__main__":
    solve()