import sys
from collections import deque

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0]); m = int(data[1])
    # build adjacency list using arrays for speed
    # Use CSR-like structure or list of lists
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(data[idx]); v = int(data[idx+1]); idx += 2
        adj[u].append(v)
        adj[v].append(u)
    color = [0] * (n + 1)  # 0 = uncolored, 1 or 2
    for s in range(1, n + 1):
        if color[s] == 0:
            color[s] = 1
            q = deque([s])
            while q:
                u = q.popleft()
                cu = color[u]
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - cu
                        q.append(v)
                    elif color[v] == cu:
                        print("NO")
                        return
    out = []
    out.append("YES")
    out.append(' '.join(map(str, color[1:])))
    sys.stdout.write('\n'.join(out) + '\n')

main()