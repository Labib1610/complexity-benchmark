def solve():
    import sys
    from collections import defaultdict

    # Read input
    n, m = map(int, sys.stdin.readline().split())
    conflicts = []
    graph = defaultdict(set)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        conflicts.append((u, v))
        graph[u].add(v)
        graph[v].add(u)

    # Special case: no modules
    if n == 0:
        print("YES")
        return

    # Try all possible assignments in lexicographical order
    # We'll use backtracking with pruning
    assignment = [0] * (n + 1)  # assignment[i] = band for module i (1-indexed)

    def is_valid(module, band):
        # Check if assigning 'band' to 'module' conflicts with neighbors
        for neighbor in graph[module]:
            if assignment[neighbor] == band:
                return False
        return True

    def backtrack(module):
        if module > n:
            return True  # All modules assigned

        # Try bands 1, 2, 3 in order for lex smallest
        for band in [1, 2, 3]:
            if is_valid(module, band):
                assignment[module] = band
                if backtrack(module + 1):
                    return True
                # No need to undo assignment since we return immediately when found

        return False  # No valid band found for this module

    # Start backtracking from module 1
    if backtrack(1):
        print("YES")
        print(' '.join(map(str, assignment[1:])))
    else:
        print("NO")

solve()