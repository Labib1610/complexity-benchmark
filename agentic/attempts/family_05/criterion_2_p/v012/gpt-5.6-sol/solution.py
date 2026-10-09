import sys
from collections import deque

def main():
    input_data = sys.stdin.buffer
    first = input_data.readline().split()
    if not first:
        return

    k, t = map(int, first)
    adjacency = [[] for _ in range(k + 1)]
    vehicle = [0] * (k + 1)

    for _ in range(t):
        x, y, z = map(int, input_data.readline().split())
        vehicle[x] = y
        adjacency[x].append(z)

    if any(not adjacency[x] for x in range(1, k + 1)):
        print("NO")
        return

    match_agent = [0] * (k + 1)
    match_sector = [0] * (k + 1)
    dist = [0] * (k + 1)
    current = [0] * (k + 1)
    inf = k + 1

    sys.setrecursionlimit(5000)

    def bfs():
        queue = deque()
        for agent in range(1, k + 1):
            if match_agent[agent] == 0:
                dist[agent] = 0
                queue.append(agent)
            else:
                dist[agent] = inf

        dist[0] = inf

        while queue:
            agent = queue.popleft()
            if dist[agent] >= dist[0]:
                continue

            next_distance = dist[agent] + 1
            for sector in adjacency[agent]:
                other_agent = match_sector[sector]
                if other_agent == 0:
                    dist[0] = next_distance
                elif dist[other_agent] == inf:
                    dist[other_agent] = next_distance
                    queue.append(other_agent)

        return dist[0] != inf

    def dfs(agent):
        edges = adjacency[agent]
        while current[agent] < len(edges):
            sector = edges[current[agent]]
            current[agent] += 1
            other_agent = match_sector[sector]

            if dist[other_agent] == dist[agent] + 1:
                if other_agent == 0 or dfs(other_agent):
                    match_agent[agent] = sector
                    match_sector[sector] = agent
                    return True

        dist[agent] = inf
        return False

    matched = 0
    while bfs():
        current = [0] * (k + 1)
        for agent in range(1, k + 1):
            if match_agent[agent] == 0 and dfs(agent):
                matched += 1

    if matched != k:
        print("NO")
        return

    output = ["YES"]
    for agent in range(1, k + 1):
        output.append(f"{agent} {vehicle[agent]} {match_agent[agent]}")
    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()