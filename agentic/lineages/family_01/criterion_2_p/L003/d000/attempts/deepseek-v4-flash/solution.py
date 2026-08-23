import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    color = [-1] * n
    
    for start in range(n):
        if color[start] != -1:
            continue
        color[start] = 0  # 0 will map to mode 1
        q = deque([start])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    q.append(v)
                elif color[v] == color[u]:
                    print("NO")
                    return
    
    print("YES")
    # Output mode: color 0 -> 1, color 1 -> 2
    print(" ".join(str(c + 1) for c in color))

if __name__ == "__main__":
    solve()