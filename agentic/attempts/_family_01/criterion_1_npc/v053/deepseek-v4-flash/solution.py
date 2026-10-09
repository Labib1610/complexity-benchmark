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

    colors = [0] * n

    # Sort vertices by degree descending for better pruning
    order = sorted(range(n), key=lambda x: -len(adj[x]))

    def backtrack(idx):
        if idx == n:
            return True
        v = order[idx]
        used = set()
        for nei in adj[v]:
            if colors[nei] != 0:
                used.add(colors[nei])
        for c in range(1, 4):
            if c not in used:
                colors[v] = c
                if backtrack(idx + 1):
                    return True
                colors[v] = 0
        return False

    if backtrack(0):
        print("YES")
        print(" ".join(str(colors[i]) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()