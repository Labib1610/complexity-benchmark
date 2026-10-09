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
    
    color = [0] * n
    
    def is_safe(node, c):
        for nei in adj[node]:
            if color[nei] == c:
                return False
        return True
    
    def backtrack(idx):
        if idx == n:
            return True
        # Try colors 1, 2, 3
        for c in range(1, 4):
            if is_safe(idx, c):
                color[idx] = c
                if backtrack(idx + 1):
                    return True
                color[idx] = 0
        return False
    
    if backtrack(0):
        print("YES")
        print(" ".join(map(str, color)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()