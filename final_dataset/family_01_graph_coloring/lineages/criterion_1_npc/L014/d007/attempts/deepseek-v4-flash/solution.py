import sys

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, w = map(int, input().split())
        u -= 1
        w -= 1
        adj[u].append(w)
        adj[w].append(u)

    # Order nodes by degree descending for better pruning
    order = sorted(range(n), key=lambda x: len(adj[x]), reverse=True)
    pos = [0] * n
    for i, v in enumerate(order):
        pos[v] = i

    color = [0] * n
    assigned = [False] * n

    def backtrack(idx):
        if idx == n:
            return True
        v = order[idx]
        used = set()
        for nb in adj[v]:
            if assigned[nb]:
                used.add(color[nb])
        for c in (1, 2, 3):
            if c not in used:
                color[v] = c
                assigned[v] = True
                if backtrack(idx + 1):
                    return True
                assigned[v] = False
                color[v] = 0
        return False

    if backtrack(0):
        print("YES")
        print(" ".join(str(color[i]) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()