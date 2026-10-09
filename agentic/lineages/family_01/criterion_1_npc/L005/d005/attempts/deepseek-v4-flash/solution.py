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
    
    color = [0] * n  # 0 = unassigned, 1,2,3
    
    def is_valid(u, c):
        for v in adj[u]:
            if color[v] == 0:
                continue
            if c == color[v]:
                return False
            if (c == 2 and color[v] == 3) or (c == 3 and color[v] == 2):
                return False
        return True
    
    def dfs(idx):
        if idx == n:
            return True
        # try colors 1,2,3
        for c in (1,2,3):
            if is_valid(idx, c):
                color[idx] = c
                if dfs(idx+1):
                    return True
                color[idx] = 0
        return False
    
    if dfs(0):
        print("YES")
        print(" ".join(map(str, color)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()