import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))

    adj = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)

    # Try to find an independent set of size k
    # Use bitmask for visited/forbidden
    forbidden = 0
    chosen = []

    def dfs(start, forbidden_mask, depth):
        if depth == k:
            return True
        # Try to pick next vertex
        for v in range(start, n):
            if (forbidden_mask >> v) & 1:
                continue
            # choose v
            chosen.append(v + 1)
            new_forbidden = forbidden_mask | (1 << v) | adj[v]
            if dfs(v + 1, new_forbidden, depth + 1):
                return True
            chosen.pop()
        return False

    if dfs(0, 0, 0):
        print("YES")
        print(" ".join(map(str, chosen)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()