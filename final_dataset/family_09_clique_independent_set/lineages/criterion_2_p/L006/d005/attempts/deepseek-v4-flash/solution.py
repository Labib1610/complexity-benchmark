import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    n, m, k = map(int, input_data[:3])
    adj = [[] for _ in range(n)]
    idx = 3
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx+1]) - 1
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
    
    color = [-1] * n
    sides = [[], []]
    
    for start in range(n):
        if color[start] == -1:
            color[start] = 0
            sides[0].append(start)
            q = deque([start])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        sides[color[v]].append(v)
                        q.append(v)
                    elif color[v] == color[u]:
                        # Should not happen due to problem guarantee
                        pass
    
    # choose larger side
    if len(sides[0]) >= len(sides[1]):
        big_side = sides[0]
    else:
        big_side = sides[1]
    
    if len(big_side) < k:
        print("NO")
        return
    
    selected = big_side[:k]
    print("YES")
    print(" ".join(str(x+1) for x in selected))

if __name__ == "__main__":
    solve()