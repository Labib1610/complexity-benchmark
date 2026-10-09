import sys
from sys import setrecursionlimit

def solve():
    input_data = sys.stdin.buffer.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx]); v = int(input_data[idx+1])
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
    
    color = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if color[i] == 0:
            # BFS to check bipartiteness and assign colors
            queue = [i]
            color[i] = 1
            head = 0
            while head < len(queue):
                u = queue[head]
                head += 1
                cu = color[u]
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - cu
                        queue.append(v)
                    elif color[v] == cu:
                        sys.stdout.write("NO\n")
                        return
    
    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(str(color[i]) for i in range(1, n + 1)) + "\n")

if __name__ == "__main__":
    solve()