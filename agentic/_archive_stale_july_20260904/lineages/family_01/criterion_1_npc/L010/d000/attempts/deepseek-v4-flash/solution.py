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
    
    color = [0] * n  # 0 = unassigned, 1,2,3 = colors
    
    def is_safe(v, c):
        for u in adj[v]:
            if color[u] == c:
                return False
        return True
    
    def backtrack(idx):
        if idx == n:
            return True
        for c in range(1, 4):
            if is_safe(idx, c):
                color[idx] = c
                if backtrack(idx + 1):
                    return True
                color[idx] = 0
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(str(c) for c in color))
    else:
        print("NO")

if __name__ == "__main__":
    solve()