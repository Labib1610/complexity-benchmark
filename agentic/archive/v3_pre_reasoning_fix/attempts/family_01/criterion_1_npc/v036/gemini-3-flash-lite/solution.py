import sys

def solve():
    try:
        line1 = sys.stdin.readline().split()
        if not line1:
            return
        n, m = map(int, line1)
    except ValueError:
        return

    adj = [0] * (n + 1)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u] |= (1 << (v - 1))
        adj[v] |= (1 << (u - 1))

    assignment = [0] * n

    def is_valid(idx, color, current_assignment):
        mask = 0
        for i in range(idx):
            if current_assignment[i] == color:
                mask |= (1 << i)
        
        # Check if any experiment j < idx conflicts with the current one
        # where current_assignment[j] == color
        for j in range(idx):
            if current_assignment[j] == color:
                if (adj[idx + 1] >> j) & 1:
                    return False
        return True

    def backtrack(idx):
        if idx == n:
            return True
        
        for color in [1, 2, 3]:
            if is_valid(idx, color, assignment):
                assignment[idx] = color
                if backtrack(idx + 1):
                    return True
                assignment[idx] = 0
        return False

    if backtrack(0):
        print("YES")
        print(*(assignment))
    else:
        print("NO")

if __name__ == '__main__':
    solve()