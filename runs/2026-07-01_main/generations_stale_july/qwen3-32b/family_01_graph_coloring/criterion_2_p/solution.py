import sys
from collections import deque

def main():
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr])
    ptr += 1
    m = int(input[ptr])
    ptr += 1

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(input[ptr])
        ptr += 1
        v = int(input[ptr])
        ptr += 1
        adj[u].append(v)
        adj[v].append(u)

    color = [0] * (n + 1)
    for u in range(1, n + 1):
        if color[u] == 0:
            queue = deque()
            queue.append(u)
            color[u] = 1
            while queue:
                current = queue.popleft()
                for neighbor in adj[current]:
                    if color[neighbor] == 0:
                        color[neighbor] = 3 - color[current]
                        queue.append(neighbor)
                    elif color[neighbor] != 3 - color[current]:
                        print("NO")
                        return
    print("YES")
    print(' '.join(map(str, color[1:n+1])))

if __name__ == "__main__":
    main()