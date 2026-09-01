import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].append(v)
        adj[v].append(u)

    # colors: 0 = uncolored, 1 = channel 1, 2 = channel 2
    colors = [0] * (n + 1)
    possible = True

    for i in range(1, n + 1):
        if colors[i] == 0:
            # Start BFS from node i
            queue = deque([i])
            colors[i] = 1
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if colors[v] == 0:
                        colors[v] = 3 - colors[u]
                        queue.append(v)
                    elif colors[v] == colors[u]:
                        possible = False
                        break
                if not possible:
                    break
        if not possible:
            break

    if not possible:
        sys.stdout.write("NO\n")
    else:
        sys.stdout.write("YES\n")
        # The BFS naturally assigns 1 to the first node of each component,
        # which results in the lexicographically smallest valid assignment.
        output = " ".join(map(str, colors[1:]))
        sys.stdout.write(output + "\n")

if __name__ == "__main__":
    solve()