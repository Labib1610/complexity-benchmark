import sys
sys.setrecursionlimit(1 << 25)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        c1 = int(next(it))
        c2 = int(next(it))
        u = abs(c1)
        v = abs(c2)
        b1 = 1 if c1 > 0 else 0
        b2 = 1 if c2 > 0 else 0
        adj[u].append((v, b1, b2))
        adj[v].append((u, b2, b1))
    
    color = [-1] * (n + 1)
    possible = True
    
    for i in range(1, n + 1):
        if color[i] == -1:
            stack = [(i, 0)]
            color[i] = 0
            while stack and possible:
                u, c = stack.pop()
                for v, b_u, b_v in adj[u]:
                    req_u = b_u
                    req_v = b_v
                    if c == 0:
                        need_v = req_v
                    else:
                        need_v = 1 - req_v
                    if color[v] == -1:
                        color[v] = need_v
                        stack.append((v, need_v))
                    elif color[v] != need_v:
                        possible = False
                        break
                if not possible:
                    break
        if not possible:
            break
    
    if not possible:
        print("NO")
    else:
        print("YES")
        print(' '.join(str(color[i]) for i in range(1, n + 1)))

solve()