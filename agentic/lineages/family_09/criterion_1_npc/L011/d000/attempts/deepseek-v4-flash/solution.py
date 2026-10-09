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
    # Use backtracking with pruning
    chosen = []
    # We'll use a recursive function
    def backtrack(start, chosen_mask, chosen_list):
        if len(chosen_list) == k:
            return True
        # Try to add vertices from start to n-1
        for v in range(start, n):
            # Check if v is compatible with all chosen
            if (chosen_mask & adj[v]) == 0:
                chosen_list.append(v)
                if backtrack(v + 1, chosen_mask | (1 << v), chosen_list):
                    return True
                chosen_list.pop()
        return False

    if backtrack(0, 0, []):
        print("YES")
        print(" ".join(str(x + 1) for x in chosen))
    else:
        print("NO")

if __name__ == "__main__":
    solve()