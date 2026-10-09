import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [set() for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].add(v)
        adj[v].add(u)
    
    # Order vertices by degree descending for better pruning
    order = sorted(range(n), key=lambda x: -len(adj[x]))
    pos_of = [0] * n
    for i, v in enumerate(order):
        pos_of[v] = i
    
    color = [0] * n
    colored = [False] * n
    
    def dfs(idx):
        if idx == n:
            return True
        v = order[idx]
        used = set()
        for u in adj[v]:
            if colored[u]:
                used.add(color[u])
        for c in (1, 2, 3):
            if c not in used:
                color[v] = c
                colored[v] = True
                if dfs(idx + 1):
                    return True
                colored[v] = False
                color[v] = 0
        return False
    
    if dfs(0):
        ans = [0] * n
        for i in range(n):
            ans[i] = color[i]
        print("YES")
        print(" ".join(str(ans[i]) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()