import sys
from collections import deque

def main():
    input_buffer = sys.stdin.buffer
    first = input_buffer.readline().split()
    if not first:
        return

    k, t = map(int, first)

    adjacency = [[] for _ in range(k + 1)]
    station_for_drone = [0] * (k + 1)
    drone_for_station = [0] * (k + 1)

    pair_drone = [0] * (k + 1)
    pair_frequency = [0] * (k + 1)
    matching_size = 0
    valid = True

    for _ in range(t):
        d, c, f = map(int, input_buffer.readline().split())
        adjacency[d].append(f)

        if station_for_drone[d] == 0:
            station_for_drone[d] = c
        elif station_for_drone[d] != c:
            valid = False

        if drone_for_station[c] == 0:
            drone_for_station[c] = d
        elif drone_for_station[c] != d:
            valid = False

        if pair_drone[d] == 0 and pair_frequency[f] == 0:
            pair_drone[d] = f
            pair_frequency[f] = d
            matching_size += 1

    if not valid or any(station_for_drone[d] == 0 for d in range(1, k + 1)):
        print("NO")
        return

    INF = k + 1
    distance = [INF] * (k + 1)
    sys.setrecursionlimit(k + 100)

    while matching_size < k:
        queue = deque()
        shortest = INF

        for d in range(1, k + 1):
            if pair_drone[d] == 0:
                distance[d] = 0
                queue.append(d)
            else:
                distance[d] = INF

        while queue:
            d = queue.popleft()
            if distance[d] >= shortest:
                continue

            next_distance = distance[d] + 1
            for f in adjacency[d]:
                next_drone = pair_frequency[f]
                if next_drone == 0:
                    shortest = next_distance
                elif distance[next_drone] == INF:
                    distance[next_drone] = next_distance
                    queue.append(next_drone)

        if shortest == INF:
            break

        def dfs(d):
            next_distance = distance[d] + 1
            for f in adjacency[d]:
                next_drone = pair_frequency[f]
                if next_drone == 0:
                    if next_distance != shortest:
                        continue
                elif distance[next_drone] != next_distance or not dfs(next_drone):
                    continue

                pair_drone[d] = f
                pair_frequency[f] = d
                return True

            distance[d] = INF
            return False

        for d in range(1, k + 1):
            if pair_drone[d] == 0 and dfs(d):
                matching_size += 1

    if matching_size != k:
        print("NO")
        return

    output = ["YES"]
    output.extend(
        f"{d} {station_for_drone[d]} {pair_drone[d]}"
        for d in range(1, k + 1)
    )
    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()