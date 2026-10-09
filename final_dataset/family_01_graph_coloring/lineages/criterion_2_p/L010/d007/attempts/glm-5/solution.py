import sys
from collections import deque

def solve():
    input = sys.stdin.read().split()
    if not input:
        return
    it = iter(input)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * (n + 1)
    possible = True
    
    for i in range(1, n + 1):
        if color[i] == 0:
            # BFS to color the component
            queue = deque([i])
            color[i] = 1
            comp_nodes = []
            while queue:
                u = queue.popleft()
                comp_nodes.append(u)
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        possible = False
                        break
                if not possible:
                    break
            if not possible:
                break
            
            # Check if flipping gives smaller E
            cnt1 = 0
            cnt2 = 0
            for node in comp_nodes:
                if color[node] == 1:
                    cnt1 += 1
                else:
                    cnt2 += 1
            
            if cnt2 < cnt1:
                for node in comp_nodes:
                    color[node] = 3 - color[node]
    
    if not possible:
        print("NO")
    else:
        print("YES")
        print(' '.join(map(str, color[1:])))

if __name__ == "__main__":
    solve()