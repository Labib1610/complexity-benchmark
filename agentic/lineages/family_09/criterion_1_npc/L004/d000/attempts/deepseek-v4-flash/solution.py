import sys

def main():
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    adj = [0] * n
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)

    # Backtracking to find independent set of size k
    # We'll try to pick vertices in increasing order
    chosen = []
    def dfs(start, chosen_mask, count):
        if count == k:
            return True
        # Try to pick next vertex
        for v in range(start, n):
            if (chosen_mask & adj[v]) == 0:
                chosen.append(v)
                if dfs(v + 1, chosen_mask | (1 << v), count + 1):
                    return True
                chosen.pop()
        return False

    if dfs(0, 0, 0):
        print("YES")
        print(" ".join(str(x + 1) for x in chosen))
    else:
        print("NO")

if __name__ == "__main__":
    main()