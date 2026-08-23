import sys

def main():
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

    for s in range(n):
        if color[s] != -1:
            continue

        color[s] = 0
        q = [s]
        head = 0

        while head < len(q):
            u = q[head]
            head += 1
            cu = color[u]

            for v in adj[u]:
                if color[v] == -1:
                    color[v] = 1 - cu
                    q.append(v)
                elif color[v] == cu:
                    sys.stdout.write("NO\n")
                    return

    ans = " ".join(str(1 + c) for c in color)
    sys.stdout.write("YES\n" + ans + "\n")


if __name__ == "__main__":
    main()