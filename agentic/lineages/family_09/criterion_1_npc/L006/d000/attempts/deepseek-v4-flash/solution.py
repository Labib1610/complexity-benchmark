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

    # Try to find an independent set of size k
    chosen = []

    def backtrack(start, chosen_mask, count):
        if count == k:
            return True
        # Prune: not enough remaining vertices
        if n - start < k - count:
            return False
        for v in range(start, n):
            if (chosen_mask & adj[v]) == 0:
                chosen.append(v)
                if backtrack(v + 1, chosen_mask | (1 << v), count + 1):
                    return True
                chosen.pop()
        return False

    if backtrack(0, 0, 0):
        print("YES")
        print(" ".join(str(x + 1) for x in chosen))
    else:
        print("NO")

if __name__ == "__main__":
    solve()