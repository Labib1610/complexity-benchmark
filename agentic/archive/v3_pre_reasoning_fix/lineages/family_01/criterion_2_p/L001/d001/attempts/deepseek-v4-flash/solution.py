import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    n = int(data[0])
    m = int(data[1])

    adj = [[] for _ in range(n + 1)]

    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        adj[u].append(v)
        adj[v].append(u)

    del data

    color = [0] * (n + 1)
    ok = True

    for start in range(1, n + 1):
        if color[start] != 0:
            continue

        color[start] = 1
        q = [start]
        head = 0

        while head < len(q):
            u = q[head]
            head += 1
            cu = color[u]

            for v in adj[u]:
                if color[v] == 0:
                    color[v] = 3 - cu
                    q.append(v)
                elif color[v] == cu:
                    ok = False
                    break

            if not ok:
                break

        if not ok:
            break

    out = sys.stdout.write

    if not ok:
        out("NO\n")
    else:
        out("YES\n")
        out(" ".join(map(str, color[1:])))
        out("\n")


if __name__ == "__main__":
    main()