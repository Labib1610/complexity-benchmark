import sys
sys.setrecursionlimit(300000)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
    
    color = [-1] * n
    
    def bfs(start):
        from collections import deque
        q = deque([start])
        color[start] = 0
        while q:
            u = q.popleft()
            for v in g[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
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
    print(' '.join(str(c + 1) for c in color))

if __name__ == "__main__":
    solve()