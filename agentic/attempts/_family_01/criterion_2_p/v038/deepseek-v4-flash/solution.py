import sys
from collections import deque

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
    
    def bfs(start, start_color):
        q = deque([start])
        color[start] = start_color
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    q.append(v)
                elif color[v] == color[u]:
                    return False
        return True
    
    for i in range(n):
        if color[i] == -1:
            # try color 1
            temp = color[:]
            if bfs(i, 0):  # 0 means environment 1
                continue
            # revert and try color 2
            color = temp
            if not bfs(i, 1):  # 1 means environment 2
                print("NO")
                return
    
    print("YES")
    print(' '.join(str(c + 1) for c in color))

if __name__ == "__main__":
    solve()