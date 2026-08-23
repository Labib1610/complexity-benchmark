import sys

def solve():
    input_data = sys.stdin.buffer.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * (n + 1)
    
    for start in range(1, n + 1):
        if color[start] == 0:
            color[start] = 1
            stack = [start]
            while stack:
                u = stack.pop()
                cu = color[u]
                cv = 3 - cu
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = cv
                        stack.append(v)
                    elif color[v] != cv:
                        sys.stdout.write("NO\n")
                        return
    
    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(str(color[i]) for i in range(1, n + 1)) + "\n")

solve()