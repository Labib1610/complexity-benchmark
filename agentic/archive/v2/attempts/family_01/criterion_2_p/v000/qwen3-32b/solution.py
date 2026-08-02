from collections import deque
import sys

def main():
    input = sys.stdin.read().split()
    idx = 0
    n = int(input[idx])
    idx += 1
    m = int(input[idx])
    idx += 1

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(input[idx])
        idx += 1
        v = int(input[idx])
        idx += 1
        adj[u].append(v)
        adj[v].append(u)

    color = [-1] * (n + 1)
    result = [0] * (n + 1)

    for start in range(1, n + 1):
        if color[start] == -1:
            queue = deque()
            queue.append(start)
            color[start] = 0
            component = []
            is_bipartite = True
            while queue:
                node = queue.popleft()
                component.append(node)
                for neighbor in adj[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = color[node] ^ 1
                        queue.append(neighbor)
                    else:
                        if color[neighbor] == color[node]:
                            is_bipartite = False
            if not is_bipartite:
                print("IMPOSSIBLE")
                return
            # Find min_node in component
            min_node = min(component)
            # Check color of min_node and adjust accordingly
            if color[min_node] == 1:
                for node in component:
                    result[node] = 2 - color[node]
            else:
                for node in component:
                    result[node] = 1 + color[node]
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()