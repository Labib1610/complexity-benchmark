import sys

def main():
    input_buffer = sys.stdin.buffer
    first = input_buffer.readline().split()
    if not first:
        return

    k, t = map(int, first)
    adjacency = [[] for _ in range(k + 1)]
    jet = [0] * (k + 1)

    pair_captain = [0] * (k + 1)
    pair_destination = [0] * (k + 1)
    matched = 0

    for _ in range(t):
        c, j, d = map(int, input_buffer.readline().split())
        adjacency[c].append(d)
        jet[c] = j

        if pair_captain[c] == 0 and pair_destination[d] == 0:
            pair_captain[c] = d
            pair_destination[d] = c
            matched += 1

    if matched < k:
        sys.setrecursionlimit(5000)
        distance = [-1] * (k + 1)

        while True:
            queue = []
            for c in range(1, k + 1):
                if pair_captain[c] == 0:
                    distance[c] = 0
                    queue.append(c)
                else:
                    distance[c] = -1

            shortest = k + 1
            head = 0

            while head < len(queue):
                c = queue[head]
                head += 1
                next_distance = distance[c] + 1

                if next_distance > shortest:
                    continue

                for d in adjacency[c]:
                    other = pair_destination[d]
                    if other == 0:
                        shortest = next_distance
                    elif next_distance < shortest and distance[other] == -1:
                        distance[other] = next_distance
                        queue.append(other)

            if shortest == k + 1:
                break

            edge_index = [0] * (k + 1)

            def dfs(c):
                next_distance = distance[c] + 1
                edges = adjacency[c]

                while edge_index[c] < len(edges):
                    d = edges[edge_index[c]]
                    edge_index[c] += 1
                    other = pair_destination[d]

                    if other == 0:
                        if next_distance == shortest:
                            pair_captain[c] = d
                            pair_destination[d] = c
                            return True
                    elif (next_distance < shortest and
                          distance[other] == next_distance and dfs(other)):
                        pair_captain[c] = d
                        pair_destination[d] = c
                        return True

                distance[c] = -1
                return False

            augmented = 0
            for c in range(1, k + 1):
                if pair_captain[c] == 0 and dfs(c):
                    augmented += 1

            if augmented == 0:
                break

            matched += augmented
            if matched == k:
                break

    if matched != k:
        sys.stdout.write("NO\n")
        return

    output = ["YES"]
    output.extend(
        f"{c} {jet[c]} {pair_captain[c]}"
        for c in range(1, k + 1)
    )
    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()