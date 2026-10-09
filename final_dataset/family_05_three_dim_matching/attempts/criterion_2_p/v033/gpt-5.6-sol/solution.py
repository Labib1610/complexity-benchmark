import sys
from array import array
from collections import deque

sys.setrecursionlimit(10000)


def integers(data):
    i = 0
    n = len(data)
    while i < n:
        while i < n and data[i] <= 32:
            i += 1
        value = 0
        while i < n and data[i] > 32:
            value = value * 10 + data[i] - 48
            i += 1
        yield value


def main():
    data = sys.stdin.buffer.read()
    it = integers(data)

    try:
        k = next(it)
        t = next(it)
    except StopIteration:
        return

    adjacency = [array('H') for _ in range(k)]
    machine_of = [-1] * k
    specialist_of = [-1] * k
    valid = True

    for _ in range(t):
        x = next(it) - 1
        y = next(it) - 1
        z = next(it) - 1

        if machine_of[x] == -1:
            machine_of[x] = y
        elif machine_of[x] != y:
            valid = False

        if specialist_of[y] == -1:
            specialist_of[y] = x
        elif specialist_of[y] != x:
            valid = False

        adjacency[x].append(z)

    if not valid or any(y == -1 for y in machine_of) or any(x == -1 for x in specialist_of):
        print("NO")
        return

    pair_left = [-1] * k
    pair_right = [-1] * k
    distance = [-1] * k

    def bfs():
        queue = deque()
        found = False

        for u in range(k):
            if pair_left[u] == -1:
                distance[u] = 0
                queue.append(u)
            else:
                distance[u] = -1

        while queue:
            u = queue.popleft()
            next_distance = distance[u] + 1

            for v in adjacency[u]:
                matched = pair_right[v]
                if matched == -1:
                    found = True
                elif distance[matched] == -1:
                    distance[matched] = next_distance
                    queue.append(matched)

        return found

    def dfs(u):
        for v in adjacency[u]:
            matched = pair_right[v]
            if matched == -1 or (
                distance[matched] == distance[u] + 1 and dfs(matched)
            ):
                pair_left[u] = v
                pair_right[v] = u
                return True

        distance[u] = -1
        return False

    matching = 0
    while bfs():
        for u in range(k):
            if pair_left[u] == -1 and dfs(u):
                matching += 1

    if matching != k:
        print("NO")
        return

    output = ["YES"]
    for x in range(k):
        output.append(f"{x + 1} {machine_of[x] + 1} {pair_left[x] + 1}")

    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    main()