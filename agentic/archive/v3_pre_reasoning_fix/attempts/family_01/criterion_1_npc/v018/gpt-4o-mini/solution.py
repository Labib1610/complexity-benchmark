def can_schedule(n, m, incompatibilities):
    from itertools import combinations

    # Create an adjacency list for the incompatibility pairs
    incompatible = [[] for _ in range(n + 1)]
    for u, v in incompatibilities:
        incompatible[u].append(v)
        incompatible[v].append(u)

    # To store the schedule
    schedule = [0] * (n + 1)

    # Try to assign time windows
    def assign(worker):
        if worker > n:
            return True  # All workers assigned successfully

        for time_window in range(1, 4):  # Time windows 1, 2, 3
            # Check if we can assign this worker to the time window
            can_assign = True
            for incompatible_worker in incompatible[worker]:
                if schedule[incompatible_worker] == time_window:
                    can_assign = False
                    break

            if can_assign:
                schedule[worker] = time_window  # Assign this time window
                if assign(worker + 1):  # Recur for the next worker
                    return True
                schedule[worker] = 0  # Backtrack

        return False  # No valid assignment found

    if assign(1):
        print("YES")
        print(" ".join(map(str, schedule[1:])))
    else:
        print("NO")


# Read input
import sys
input = sys.stdin.read
data = input().splitlines()
n, m = map(int, data[0].split())
incompatibilities = [tuple(map(int, line.split())) for line in data[1:m + 1]]

can_schedule(n, m, incompatibilities)