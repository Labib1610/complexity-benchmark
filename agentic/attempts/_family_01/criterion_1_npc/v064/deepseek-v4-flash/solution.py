import sys

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * n

    # Sort vertices by degree (largest first) for better pruning
    order = sorted(range(n), key=lambda x: len(adj[x]), reverse=True)

    def backtrack(idx):
        if idx == n:
            return True
        v = order[idx]
        used = set()
        for nb in adj[v]:
            if color[nb] != -1:
                used.add(color[nb])
        for c in range(3):
            if c not in used:
                color[v] = c
                if backtrack(idx + 1):
                    return True
                color[v] = -1
        return False

    if backtrack(0):
        print("YES")
        print(" ".join(str(c + 1) for c in color))
    else:
        print("NO")

if __name__ == "__main__":
    solve()