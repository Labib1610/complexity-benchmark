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
    is_possible = True
    
    for i in range(1, n + 1):
        if color[i] == 0:
            stack = [i]
            color[i] = 1
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        stack.append(v)
                    elif color[v] == color[u]:
                        is_possible = False
                        break
                if not is_possible:
                    break
        if not is_possible:
            break
    
    if not is_possible:
        sys.stdout.write("NO\n")
        return
    
    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(str(color[i]) for i in range(1, n + 1)) + "\n")

if __name__ == "__main__":
    solve()