import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[0], data[1]
    adj = [[] for _ in range(n + 1)]

    idx = 2
    for _ in range(m):
        u = data[idx]
        v = data[idx + 1]
        idx += 2
        adj[u].append(v)
        adj[v].append(u)

    color = [0] * (n + 1)

    for start in range(1, n + 1):
        if color[start] == 0:
            color[start] = 1
            stack = [start]

            while stack:
                u = stack.pop()
                need = 3 - color[u]

                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = need
                        stack.append(v)
                    elif color[v] != need:
                        print("NO")
                        return

    print("YES")
    print(" ".join(map(str, color[1:])))

if __name__ == "__main__":
    main()