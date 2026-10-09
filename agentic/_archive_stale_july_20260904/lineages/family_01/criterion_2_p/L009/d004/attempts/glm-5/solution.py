import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx]); v = int(input_data[idx + 1])
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * (n + 1)
    possible = True
    
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
                        possible = False
                        break
                if not possible:
                    break
        if not possible:
            break
    
    if not possible:
        sys.stdout.write("NO\n")
        return
    
    # Lexicographically smallest: prefer 1 whenever possible.
    # color 1 -> 1, color 2 -> 2
    ans = [str(color[i]) for i in range(1, n + 1)]
    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(ans) + "\n")

solve()