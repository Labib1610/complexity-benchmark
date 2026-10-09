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
    
    def is_safe(node, c):
        for nb in adj[node]:
            if color[nb] == c:
                return False
        return True
    
    def backtrack(node):
        if node == n:
            return True
        # Try colors 0,1,2
        for c in range(3):
            if is_safe(node, c):
                color[node] = c
                if backtrack(node + 1):
                    return True
                color[node] = -1
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(str(c + 1) for c in color))
    else:
        print("NO")

if __name__ == "__main__":
    solve()