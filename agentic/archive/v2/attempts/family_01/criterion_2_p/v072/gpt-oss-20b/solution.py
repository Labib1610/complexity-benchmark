import sys
from collections import deque

def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    try:
        n = int(next(it))
        m = int(next(it))
    except StopIteration:
        return

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * (n + 1)          # relative color (0/1) during BFS
    ans = [0] * (n + 1)             # final assignment (1/2)

    for start in range(1, n + 1):
        if color[start] != -1:
            continue

        q = deque([start])
        color[start] = 0
        component = [start]

        while q:
            u = q.popleft()
            cu = color[u]
            for v in adj[u]:
                cv = color[v]
                if cv == -1:
                    color[v] = cu ^ 1
                    q.append(v)
                    component.append(v)
                elif cv == cu:
                    sys.stdout.write("NO")
                    return

        # Choose orientation to make the smallest index in this component color 1
        min_node = min(component)
        rel_min = color[min_node]
        for v in component:
            ans[v] = 1 + (color[v] ^ rel_min)

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(str(ans[i]) for i in range(1, n + 1)))

if __name__ == "__main__":
    main()