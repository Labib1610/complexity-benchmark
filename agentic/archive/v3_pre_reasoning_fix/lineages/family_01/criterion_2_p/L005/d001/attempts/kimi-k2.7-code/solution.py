import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u == v:
            print("NO")
            return
        adj[u].append(v)
        adj[v].append(u)

    color = [0] * (n + 1)
    for i in range(1, n + 1):
        if color[i] != 0:
            continue
        color[i] = 1
        stack = [i]
        while stack:
            u = stack.pop()
            cu = color[u]
            cv = 3 - cu
            for w in adj[u]:
                if color[w] == 0:
                    color[w] = cv
                    stack.append(w)
                elif color[w] == cu:
                    print("NO")
                    return

    out = ['YES', ' '.join(map(str, color[1:]))]
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()