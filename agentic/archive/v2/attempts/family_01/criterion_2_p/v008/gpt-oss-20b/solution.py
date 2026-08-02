import sys
from collections import deque

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = next(it)
        v = next(it)
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * (n + 1)  # 0 -> shift 1, 1 -> shift 2

    for start in range(1, n + 1):
        if color[start] != -1:
            continue
        queue = deque([start])
        color[start] = 0
        while queue:
            u = queue.popleft()
            cu = color[u]
            for v in adj[u]:
                if color[v] == -1:
                    color[v] = cu ^ 1
                    queue.append(v)
                elif color[v] == cu:
                    sys.stdout.write("NO")
                    return

    # All components colored with earliest node as shift 1
    out = ['YES\n'] + [' '.join(str(c + 1) for c in color[1:])]
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    main()