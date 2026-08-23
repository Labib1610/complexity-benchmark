import sys

def main():
    input = sys.stdin.buffer.readline

    first = input().split()
    if not first:
        return

    n = int(first[0])
    m = int(first[1])

    adj = [[] for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)

    color = [0] * n

    for i in range(n):
        if color[i] == 0:
            color[i] = 1
            queue = [i]
            head = 0

            while head < len(queue):
                u = queue[head]
                head += 1

                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        sys.stdout.write("NO\n")
                        return

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, color)) + "\n")


if __name__ == "__main__":
    main()