import sys

def solve():
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

    assignment = [0] * (n + 1)

    def is_valid(node, phase):
        for neighbor in adj[node]:
            if assignment[neighbor] == phase:
                return False
        return True

    def backtrack(node):
        if node > n:
            return True
        
        for phase in range(1, 4):
            if is_valid(node, phase):
                assignment[node] = phase
                if backtrack(node + 1):
                    return True
                assignment[node] = 0
        return False

    if backtrack(1):
        print("YES")
        print(*(assignment[1:]))
    else:
        print("NO")

if __name__ == '__main__':
    solve()