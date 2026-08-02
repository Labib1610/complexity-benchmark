def can_assign_shifts(n, conflicts):
    from collections import defaultdict, deque

    graph = defaultdict(list)
    for u, v in conflicts:
        graph[u].append(v)
        graph[v].append(u)

    shifts = [0] * (n + 1)  # shifts[i] will be 1, 2, or 3 for worker i
    for worker in range(1, n + 1):
        if shifts[worker] == 0:  # unassigned worker
            queue = deque([worker])
            shifts[worker] = 1  # start with shift 1

            while queue:
                current = queue.popleft()
                current_shift = shifts[current]

                for neighbor in graph[current]:
                    if shifts[neighbor] == 0:  # not assigned
                        # Assign a shift different from current_shift
                        for new_shift in range(1, 4):
                            if new_shift != current_shift:
                                shifts[neighbor] = new_shift
                                queue.append(neighbor)
                                break
                    elif shifts[neighbor] == current_shift:  # conflict
                        return "NO", []

    return "YES", shifts[1:]

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    n, m = map(int, data[0].split())
    conflicts = [tuple(map(int, line.split())) for line in data[1:m + 1]]

    result, shifts = can_assign_shifts(n, conflicts)
    print(result)
    if result == "YES":
        print(" ".join(map(str, shifts)))

if __name__ == "__main__":
    main()