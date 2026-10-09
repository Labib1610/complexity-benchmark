import sys
from collections import deque

def main():
    input_buffer = sys.stdin.buffer
    first = input_buffer.readline().split()
    if not first:
        return

    k, t = map(int, first)
    if t < k:
        print("NO")
        return

    adjacency = [[] for _ in range(k + 1)]
    film = [0] * (k + 1)

    for _ in range(t):
        d, f, s = map(int, input_buffer.readline().split())
        film[d] = f
        adjacency[d].append(s)

    if any(not adjacency[d] for d in range(1, k + 1)):
        print("NO")
        return

    pair_director = [0] * (k + 1)
    pair_room = [0] * (k + 1)
    distance = [0] * (k + 1)
    inf = k + 1

    sys.setrecursionlimit(k + 100)

    def bfs():
        queue = deque()
        shortest = inf

        for d in range(1, k + 1):
            if pair_director[d] == 0:
                distance[d] = 0
                queue.append(d)
            else:
                distance[d] = inf

        while queue:
            d = queue.popleft()
            if distance[d] >= shortest:
                continue

            next_distance = distance[d] + 1
            for room in adjacency[d]:
                other = pair_room[room]
                if other == 0:
                    shortest = next_distance
                elif distance[other] == inf:
                    distance[other] = next_distance
                    queue.append(other)

        return shortest

    def dfs(d, shortest):
        next_distance = distance[d] + 1

        for room in adjacency[d]:
            other = pair_room[room]
            if other == 0:
                if next_distance != shortest:
                    continue
            elif distance[other] != next_distance or not dfs(other, shortest):
                continue

            pair_director[d] = room
            pair_room[room] = d
            return True

        distance[d] = inf
        return False

    matching = 0

    while True:
        shortest = bfs()
        if shortest == inf:
            break

        for d in range(1, k + 1):
            if pair_director[d] == 0 and dfs(d, shortest):
                matching += 1

    if matching != k:
        print("NO")
        return

    output = ["YES"]
    output.extend(
        f"{d} {film[d]} {pair_director[d]}"
        for d in range(1, k + 1)
    )
    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()