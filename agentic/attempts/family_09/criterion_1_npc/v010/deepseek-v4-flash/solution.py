import sys

def solve():
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    adj = [0] * n
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)

    # Try to find independent set of size k
    # Use backtracking with bitmasks
    def backtrack(start, chosen, mask):
        if len(chosen) == k:
            return chosen[:]
        if start >= n:
            return None
        # Prune: if remaining nodes + chosen < k, impossible
        if n - start + len(chosen) < k:
            return None
        # Option 1: skip node start
        res = backtrack(start + 1, chosen, mask)
        if res:
            return res
        # Option 2: take node start if not conflicting
        if not (mask & (1 << start)):
            chosen.append(start)
            res = backtrack(start + 1, chosen, mask | adj[start])
            if res:
                return res
            chosen.pop()
        return None

    result = backtrack(0, [], 0)
    if result is None:
        print("NO")
    else:
        print("YES")
        print(" ".join(str(x + 1) for x in result))

if __name__ == "__main__":
    solve()