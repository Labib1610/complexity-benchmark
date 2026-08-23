import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n, m = data[0], data[1]
    adj = [[] for _ in range(n)]

    idx = 2
    for _ in range(m):
        u = data[idx] - 1
        v = data[idx + 1] - 1
        idx += 2
        adj[u].append(v)
        adj[v].append(u)

    color = [0] * n

    for i in range(n):
        if color[i] == 0:
            color[i] = 1
            stack = [i]

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
    print(" ".join(map(str, color)))

if __name__ == "__main__":
    main()