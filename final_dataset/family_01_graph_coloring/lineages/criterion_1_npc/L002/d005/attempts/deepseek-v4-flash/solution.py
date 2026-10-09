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
    
    # Sort vertices by degree for better pruning
    order = sorted(range(n), key=lambda x: len(adj[x]), reverse=True)
    
    def backtrack(idx):
        if idx == n:
            return True
        v = order[idx]
        used = [False] * 4
        for nei in adj[v]:
            if color[nei] != -1:
                used[color[nei]] = True
        for c in range(1, 4):
            if not used[c]:
                color[v] = c
                if backtrack(idx + 1):
                    return True
                color[v] = -1
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(str(color[i]) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()