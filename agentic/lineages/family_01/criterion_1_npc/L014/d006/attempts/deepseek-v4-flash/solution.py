import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    colors = [0] * n  # 0 = uncolored, 1,2,3 = speeds
    
    def backtrack(node):
        if node == n:
            return True
        # Try colors 1,2,3
        for c in (1,2,3):
            ok = True
            for nb in adj[node]:
                if colors[nb] == c:
                    ok = False
                    break
            if ok:
                colors[node] = c
                if backtrack(node + 1):
                    return True
                colors[node] = 0
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(str(colors[i]) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()