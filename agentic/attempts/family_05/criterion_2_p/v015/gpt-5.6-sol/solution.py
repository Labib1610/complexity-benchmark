import sys

def main():
    input_buffer = sys.stdin.buffer
    first = input_buffer.readline().split()
    if not first:
        return

    k, t = map(int, first)

    graph = [[] for _ in range(k + 1)]
    truck = [0] * (k + 1)
    pair_driver = [0] * (k + 1)
    pair_route = [0] * (k + 1)

    for _ in range(t):
        x, y, z = map(int, input_buffer.readline().split())
        graph[x].append(z)
        truck[x] = y

        # Build an initial greedy matching.
        if pair_driver[x] == 0 and pair_route[z] == 0:
            pair_driver[x] = z
            pair_route[z] = x

    distance = [0] * (k + 1)
    inf = k + 1

    def bfs():
        queue = []
        for driver in range(1, k + 1):
            if pair_driver[driver] == 0:
                distance[driver] = 0
                queue.append(driver)
            else:
                distance[driver] = inf

        distance[0] = inf
        head = 0

        while head < len(queue):
            driver = queue[head]
            head += 1

            if distance[driver] < distance[0]:
                next_distance = distance[driver] + 1
                for route in graph[driver]:
                    next_driver = pair_route[route]
                    if distance[next_driver] == inf:
                        distance[next_driver] = next_distance
                        queue.append(next_driver)

        return distance[0] != inf

    sys.setrecursionlimit(5000)

    def dfs(driver):
        if driver == 0:
            return True

        next_distance = distance[driver] + 1
        for route in graph[driver]:
            next_driver = pair_route[route]
            if distance[next_driver] == next_distance and dfs(next_driver):
                pair_driver[driver] = route
                pair_route[route] = driver
                return True

        distance[driver] = inf
        return False

    while bfs():
        for driver in range(1, k + 1):
            if pair_driver[driver] == 0:
                dfs(driver)

    if any(pair_driver[driver] == 0 for driver in range(1, k + 1)):
        sys.stdout.write("NO\n")
        return

    output = ["YES"]
    output.extend(
        f"{driver} {truck[driver]} {pair_driver[driver]}"
        for driver in range(1, k + 1)
    )
    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()