import sys
import sys
from collections import defaultdict, deque

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    
    color = [-1] * n
    for start in range(n):
        if color[start] != -1:
            continue
        color[start] = 0
        q = [start]
        while q:
            u = q.pop()
            for v in graph[u]:
                if color[v] == -1:
                    color[v] = 1 - color[u]
                    q.append(v)
                elif color[v] == color[u]:
                    print("NO")
                    return
    print("YES")

if __name__ == "__main__":
    solve()