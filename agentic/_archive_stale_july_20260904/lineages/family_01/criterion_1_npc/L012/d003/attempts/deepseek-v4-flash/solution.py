import sys
sys.setrecursionlimit(10000)

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
    
    color = [0] * n  # 0 means uncolored, 1,2,3 are colors
    
    def dfs(node):
        # Try colors 1,2,3
        for c in (1, 2, 3):
            ok = True
            for nb in adj[node]:
                if color[nb] == c:
                    ok = False
                    break
            if ok:
                color[node] = c
                # Find next uncolored node
                next_node = -1
                for i in range(n):
                    if color[i] == 0:
                        next_node = i
                        break
                if next_node == -1:
                    return True
                if dfs(next_node):
                    return True
                color[node] = 0
        return False
    
    # Start from node 0
    if not dfs(0):
        print("NO")
    else:
        print("YES")
        print(" ".join(str(c) for c in color))

if __name__ == "__main__":
    solve()