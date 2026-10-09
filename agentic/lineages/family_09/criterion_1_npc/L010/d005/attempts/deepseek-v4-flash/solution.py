import sys

def solve():
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    adj = [0] * n
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
    
    # Backtracking to find independent set of size k
    chosen = []
    
    def dfs(start, count):
        if count == k:
            return True
        # Try to pick next vertex
        for v in range(start, n):
            # Check if v is adjacent to any chosen
            ok = True
            for u in chosen:
                if (adj[u] >> v) & 1:
                    ok = False
                    break
            if ok:
                chosen.append(v)
                if dfs(v + 1, count + 1):
                    return True
                chosen.pop()
        return False
    
    if dfs(0, 0):
        print("YES")
        print(" ".join(str(x + 1) for x in chosen))
    else:
        print("NO")

if __name__ == "__main__":
    solve()