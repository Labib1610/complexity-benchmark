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

        if u == v:
            print("NO")
            return

        adj[u].append(v)
        adj[v].append(u)

    color = [0] * (n + 1)

    for start in range(1, n + 1):
        if color[start] != 0:
            continue

        color[start] = 1
        queue = [start]
        head = 0

        while head < len(queue):
            v = queue[head]
            head += 1

            for to in adj[v]:
                if color[to] == 0:
                    color[to] = 3 - color[v]
                    queue.append(to)
                elif color[to] == color[v]:
                    print("NO")
                    return

    print("YES")
    print(" ".join(map(str, color[1:])))

if __name__ == "__main__":
    main()