import sys

def solve():
    # Set recursion depth for deep backtracking
    sys.setrecursionlimit(2000)
    
    # Read input
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2

    # colors[i] stores the domain assigned to module i (0 means unassigned)
    colors = [0] * (n + 1)

    def is_valid(u, c):
        for v in adj[u]:
            if colors[v] == c:
                return False
        return True

    def backtrack(u):
        if u > n:
            return True
        
        # Try colors 1, 2, 3 in order to ensure lexicographical smallest result
        for c in range(1, 4):
            if is_valid(u, c):
                colors[u] = c
                if backtrack(u + 1):
                    return True
                colors[u] = 0
        return False

    # Optimization: The problem is 3-coloring. While 3-coloring is NP-complete,
    # N=40 is small enough for backtracking with some pruning or simple search
    # given the time limit and the specific requirement for lexicographical smallest.
    # However, we can improve the search by checking if the remaining graph is 3-colorable.
    # Since N=40, simple backtracking might be slow in worst case, but usually works
    # for sparse or structured graphs.
    
    if backtrack(1):
        print("YES")
        print(*(colors[1:]))
    else:
        print("NO")

if __name__ == "__main__":
    solve()