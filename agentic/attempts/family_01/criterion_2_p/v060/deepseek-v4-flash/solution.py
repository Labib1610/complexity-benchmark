import sys
sys.setrecursionlimit(300000)

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
    
    def bfs(start):
        from collections import deque
        q = deque([start])
        color[start] = 1
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 3 - color[u]
                    q.append(v)
                elif color[v] == color[u]:
                    return False
        return True
    
    for i in range(n):
        if color[i] == -1:
            if not bfs(i):
                print("NO")
                return
    
    print("YES")
    print(" ".join(str(color[i]) for i in range(n)))

if __name__ == "__main__":
    solve()