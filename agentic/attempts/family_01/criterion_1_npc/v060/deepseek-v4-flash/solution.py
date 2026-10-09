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
    
    def is_safe(v, c):
        for u in adj[v]:
            if color[u] == c:
                return False
        return True
    
    def backtrack(v):
        if v == n:
            return True
        for c in range(3):
            if is_safe(v, c):
                color[v] = c
                if backtrack(v + 1):
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