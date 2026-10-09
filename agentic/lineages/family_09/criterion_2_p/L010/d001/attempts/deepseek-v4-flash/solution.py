import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    
    color = [-1] * n
    part1 = []
    part2 = []
    
    for i in range(n):
        if color[i] == -1:
            color[i] = 0
            q = deque([i])
            part1.append(i)
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        if color[v] == 0:
                            part1.append(v)
                        else:
                            part2.append(v)
                        q.append(v)
                    elif color[v] == color[u]:
                        # Should not happen due to problem guarantee
                        pass
    
    a = len(part1)
    b = len(part2)
    
    # Try to pick x from part1 and k-x from part2
    for x in range(max(0, k - b), min(a, k) + 1):
        y = k - x
        if 0 <= x <= a and 0 <= y <= b:
            res = part1[:x] + part2[:y]
            print("YES")
            print(" ".join(str(v+1) for v in res))
            return
    
    print("NO")

if __name__ == "__main__":
    solve()