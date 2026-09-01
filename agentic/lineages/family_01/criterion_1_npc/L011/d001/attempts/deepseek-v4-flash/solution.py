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
    
    def is_valid(node, c):
        for nb in adj[node]:
            if colors[nb] == c:
                return False
        return True
    
    def backtrack(idx):
        if idx == n:
            return True
        for c in range(1, 4):
            if is_valid(idx, c):
                colors[idx] = c
                if backtrack(idx + 1):
                    return True
                colors[idx] = 0
        return False
    
    colors = [0] * n
    if backtrack(0):
        print("YES")
        print(" ".join(map(str, colors)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()