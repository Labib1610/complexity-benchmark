import sys

def solve():
    # Read n and m
    try:
        line1 = sys.stdin.readline().split()
        if not line1:
            return
        n, m = map(int, line1)
    except ValueError:
        return

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)

    # assignments[i] will store the window for staff i (1 to n)
    assignments = [0] * (n + 1)

    def is_valid(node, color):
        for neighbor in adj[node]:
            if assignments[neighbor] == color:
                return False
        return True

    def backtrack(node):
        if node > n:
            return True
        
        # Try colors in increasing order to ensure lexicographically smallest result
        for color in [1, 2, 3]:
            if is_valid(node, color):
                assignments[node] = color
                if backtrack(node + 1):
                    return True
                assignments[node] = 0
        return False

    # The constraints (n <= 40) are small enough for backtracking with 
    # pruning/ordering in many cases, though 3-coloring is NP-complete.
    # Given the lexicographical requirement, we must try colors 1, 2, 3 in order.
    if backtrack(1):
        print("YES")
        print(*(assignments[1:]))
    else:
        print("NO")

if __name__ == "__main__":
    # Increase recursion depth for deep backtracking trees
    sys.setrecursionlimit(2000)
    solve()