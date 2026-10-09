import sys
from collections import deque

def main():
    input_buffer = sys.stdin.buffer
    first = input_buffer.readline().split()
    if not first:
        return

    k, t = map(int, first)
    adjacency = [[] for _ in range(k + 1)]
    receptor = [0] * (k + 1)

    for _ in range(t):
        x, y, z = map(int, input_buffer.readline().split())
        adjacency[x].append(z)
        receptor[x] = y

    match_left = [0] * (k + 1)
    match_right = [0] * (k + 1)
    distance = [0] * (k + 1)
    infinity = k + 1

    sys.setrecursionlimit(10000)

    def bfs():
        queue = deque()
        for x in range(1, k + 1):
            if match_left[x] == 0:
                distance[x] = 0
                queue.append(x)
            else:
                distance[x] = infinity

        shortest = infinity

        while queue:
            x = queue.popleft()
            if distance[x] >= shortest:
                continue

            for z in adjacency[x]:
                next_x = match_right[z]
                if next_x == 0:
                    shortest = distance[x] + 1
                elif distance[next_x] == infinity:
                    distance[next_x] = distance[x] + 1
                    queue.append(next_x)

        return shortest

    matched = 0

    while matched < k:
        shortest = bfs()
        if shortest == infinity:
            break

        edge_index = [0] * (k + 1)

        def dfs(x):
            edges = adjacency[x]
            while edge_index[x] < len(edges):
                z = edges[edge_index[x]]
                edge_index[x] += 1
                next_x = match_right[z]

                if next_x == 0:
                    if distance[x] + 1 == shortest:
                        match_left[x] = z
                        match_right[z] = x
                        return True
                elif distance[next_x] == distance[x] + 1 and dfs(next_x):
                    match_left[x] = z
                    match_right[z] = x
                    return True

            distance[x] = infinity
            return False

        augmented = 0
        for x in range(1, k + 1):
            if match_left[x] == 0 and dfs(x):
                augmented += 1

        if augmented == 0:
            break
        matched += augmented

    if matched != k:
        sys.stdout.write("NO\n")
        return

    output = ["YES"]
    for x in range(1, k + 1):
        output.append(f"{x} {receptor[x]} {match_left[x]}")
    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()