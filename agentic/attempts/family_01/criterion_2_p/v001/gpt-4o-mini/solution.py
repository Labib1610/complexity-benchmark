def main():
    import sys
    from collections import defaultdict, deque

    input = sys.stdin.read
    data = input().splitlines()
    
    n, m = map(int, data[0].split())
    adjacency_list = defaultdict(list)

    for i in range(1, m + 1):
        u, v = map(int, data[i].split())
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)

    team_assignment = [0] * (n + 1)  # 0 means unassigned, 1 and 2 will be the teams

    def bfs(start):
        queue = deque([start])
        team_assignment[start] = 1  # Start with team 1
        while queue:
            current = queue.popleft()
            current_team = team_assignment[current]
            next_team = 2 if current_team == 1 else 1

            for neighbor in adjacency_list[current]:
                if team_assignment[neighbor] == 0:  # not assigned yet
                    team_assignment[neighbor] = next_team
                    queue.append(neighbor)
                elif team_assignment[neighbor] == current_team:  # conflict
                    return False
        return True

    for member in range(1, n + 1):
        if team_assignment[member] == 0:  # unvisited member
            if not bfs(member):
                print("NO")
                return

    print("YES")
    print(" ".join(map(str, team_assignment[1:])))

if __name__ == "__main__":
    main()