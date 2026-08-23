import sys
from collections import deque

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * n
    possible = True

    for i in range(n):
        if color[i] != -1:
            continue
        comp = []
        stack = [i]
        color[i] = 0
        while stack:
            u = stack.pop()
            comp.append(u)
            for w in adj[u]:
                if color[w] == -1:
                    color[w] = color[u] ^ 1
                    stack.append(w)
                elif color[w] == color[u]:
                    possible = False
                    break
            if not possible:
                break
        if not possible:
            break

        # Make the smallest-index vertex in this component have value 1.
        minv = min(comp)
        if color[minv] == 1:
            for u in comp:
                color[u] ^= 1

    if not possible:
        sys.stdout.write("NO")
    else:
        out = ["YES", " ".join(str(c + 1) for c in color)]
        sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()