import sys
sys.setrecursionlimit(300000)

def solve():
    n, m = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    
    color = [-1] * n
    
    def bfs(start):
        from collections import deque
        q = deque([start])
        color[start] = 0
        while q:
            u = q.popleft()
            for v in graph[u]:
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
    
    # color 0 -> 1, color 1 -> 2
    result = [1 if c == 0 else 2 for c in color]
    print("YES")
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    solve()