import sys

def solve():
    input_data = sys.stdin.buffer.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * (n + 1)
    visited = [False] * (n + 1)
    components = []
    
    for i in range(1, n + 1):
        if not visited[i]:
            comp = []
            stack = [i]
            visited[i] = True
            color[i] = 0
            while stack:
                u = stack.pop()
                comp.append(u)
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        color[v] = color[u] ^ 1
                        stack.append(v)
            components.append(comp)
    
    max_safe = 0
    for comp in components:
        cnt0 = sum(1 for u in comp if color[u] == 0)
        cnt1 = len(comp) - cnt0
        max_safe += max(cnt0, cnt1)
    
    if k > max_safe:
        print("NO")
        return
    
    print("YES")
    rem = k
    out = []
    for comp in components:
        if rem == 0:
            break
        cnt0 = sum(1 for u in comp if color[u] == 0)
        cnt1 = len(comp) - cnt0
        if cnt0 >= cnt1:
            take = min(rem, cnt0)
            for u in comp:
                if color[u] == 0:
                    out.append(str(u))
                    rem -= 1
                    if rem == 0:
                        break
        else:
            take = min(rem, cnt1)
            for u in comp:
                if color[u] == 1:
                    out.append(str(u))
                    rem -= 1
                    if rem == 0:
                        break
    print(' '.join(out))

solve()