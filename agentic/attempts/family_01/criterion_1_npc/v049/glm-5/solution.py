import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        adj[u].append(v)
        adj[v].append(u)

    # We use backtracking with pruning.
    # assignment[i] will be 1, 2, or 3. 0 means unassigned.
    assignment = [0] * n

    def is_safe(u, color):
        for v in adj[u]:
            if assignment[v] == color:
                return False
        return True

    def backtrack(u):
        if u == n:
            return True

        for color in range(1, 4):
            if is_safe(u, color):
                assignment[u] = color
                if backtrack(u + 1):
                    return True
                assignment[u] = 0
        
        return False

    if backtrack(0):
        sys.stdout.write("YES\n")
        sys.stdout.write(" ".join(map(str, assignment)) + "\n")
    else:
        sys.stdout.write("NO\n")

if __name__ == '__main__':
    solve()