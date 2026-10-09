import sys
from sys import setrecursionlimit

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
    setrecursionlimit(300000)
    
    for start in range(1, n + 1):
        if color[start] == 0:
            stack = [(start, 1)]
            while stack:
                node, c = stack.pop()
                if color[node] != 0:
                    continue
                color[node] = c
                for nb in adj[node]:
                    if color[nb] == 0:
                        stack.append((nb, 3 - c))
    
    cnt1 = sum(1 for i in range(1, n + 1) if color[i] == 1)
    cnt2 = n - cnt1
    
    if cnt1 >= k:
        chosen = []
        for i in range(1, n + 1):
            if color[i] == 1:
                chosen.append(i)
                if len(chosen) == k:
                    break
        sys.stdout.write("YES\n")
        sys.stdout.write(" ".join(map(str, chosen)) + "\n")
    elif cnt2 >= k:
        chosen = []
        for i in range(1, n + 1):
            if color[i] == 2:
                chosen.append(i)
                if len(chosen) == k:
                    break
        sys.stdout.write("YES\n")
        sys.stdout.write(" ".join(map(str, chosen)) + "\n")
    else:
        sys.stdout.write("NO\n")

solve()