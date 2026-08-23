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

    color = [-1] * (n + 1)

    for start in range(1, n + 1):
        if color[start] != -1:
            continue

        color[start] = 0
        stack = [start]

        while stack:
            u = stack.pop()
            cu = color[u]

            for v in adj[u]:
                if color[v] == -1:
                    color[v] = cu ^ 1
                    stack.append(v)
                elif color[v] == cu:
                    sys.stdout.write("NO\n")
                    return

    ans = [str(color[i] + 1) for i in range(1, n + 1)]
    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(ans) + "\n")

if __name__ == "__main__":
    main()