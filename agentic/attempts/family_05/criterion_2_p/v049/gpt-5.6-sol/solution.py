import sys
from collections import deque

def main():
    input_stream = sys.stdin.buffer
    first = input_stream.readline().split()
    if not first:
        return

    k, t = map(int, first)

    if t < k:
        sys.stdout.write("NO\n")
        return

    adjacency = [[] for _ in range(k)]
    rig_for_operator = [-1] * k

    for _ in range(t):
        x, y, z = map(int, input_stream.readline().split())
        x -= 1
        y -= 1
        z -= 1
        adjacency[x].append(z)
        rig_for_operator[x] = y

    if any(y == -1 for y in rig_for_operator):
        sys.stdout.write("NO\n")
        return

    pair_operator = [-1] * k
    pair_zone = [-1] * k
    distance = [0] * k
    pointer = [0] * k
    infinity = k + 1

    sys.setrecursionlimit(10000)

    def bfs():
        queue = deque()
        for operator in range(k):
            if pair_operator[operator] == -1:
                distance[operator] = 0
                queue.append(operator)
            else:
                distance[operator] = infinity

        shortest = infinity

        while queue:
            operator = queue.popleft()
            current_distance = distance[operator]

            if current_distance >= shortest:
                continue

            for zone in adjacency[operator]:
                matched_operator = pair_zone[zone]
                if matched_operator == -1:
                    shortest = current_distance + 1
                elif distance[matched_operator] == infinity:
                    distance[matched_operator] = current_distance + 1
                    queue.append(matched_operator)

        return shortest

    def dfs(operator, shortest):
        edges = adjacency[operator]
        while pointer[operator] < len(edges):
            zone = edges[pointer[operator]]
            pointer[operator] += 1
            matched_operator = pair_zone[zone]

            if matched_operator == -1:
                if distance[operator] + 1 == shortest:
                    pair_operator[operator] = zone
                    pair_zone[zone] = operator
                    return True
            elif (
                distance[matched_operator] == distance[operator] + 1
                and dfs(matched_operator, shortest)
            ):
                pair_operator[operator] = zone
                pair_zone[zone] = operator
                return True

        distance[operator] = infinity
        return False

    matching_size = 0

    while matching_size < k:
        shortest = bfs()
        if shortest == infinity:
            break

        pointer[:] = [0] * k
        augmented = 0

        for operator in range(k):
            if pair_operator[operator] == -1 and dfs(operator, shortest):
                augmented += 1

        if augmented == 0:
            break
        matching_size += augmented

    if matching_size != k:
        sys.stdout.write("NO\n")
        return

    output = ["YES"]
    for operator in range(k):
        output.append(
            f"{operator + 1} {rig_for_operator[operator] + 1} "
            f"{pair_operator[operator] + 1}"
        )

    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()