def main():
    import sys
    from collections import defaultdict, deque

    input = sys.stdin.read
    data = input().splitlines()

    n, m = map(int, data[0].split())
    
    incompatibilities = defaultdict(list)
    for i in range(1, m + 1):
        u, v = map(int, data[i].split())
        incompatibilities[u].append(v)
        incompatibilities[v].append(u)
    
    shifts = [0] * (n + 1)  # Shift assignment for staff 1 to n (1-indexed)

    def bfs(start):
        queue = deque([start])
        shifts[start] = 1  # Start assigning shift 1 to the starting staff member

        while queue:
            current = queue.popleft()
            current_shift = shifts[current]

            for neighbor in incompatibilities[current]:
                if shifts[neighbor] == 0:  # Not assigned yet
                    # Assign the next shift
                    shifts[neighbor] = 3 - current_shift - (1 if current_shift == 2 else 2)
                    queue.append(neighbor)
                elif shifts[neighbor] == current_shift:  # Conflict found
                    return False
        return True

    for staff in range(1, n + 1):
        if shifts[staff] == 0:  # Not assigned yet
            if not bfs(staff):
                print("NO")
                return

    print("YES")
    print(" ".join(map(str, shifts[1:])))

if __name__ == "__main__":
    main()