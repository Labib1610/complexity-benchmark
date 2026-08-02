import sys

def assign_windows(n, m, conflicts):
    # Graph representation of conflicts: adjacency list
    adj = {i: set() for i in range(1, n+1)}
    for u, v in conflicts:
        adj[u].add(v)
        adj[v].add(u)

    # Helper function to check if a given assignment is valid
    def is_valid_assignment(assignments):
        for i in range(1, n + 1):
            window = assignments[i]
            for j in adj[i]:
                if assignments[j] == window:
                    return False
        return True

    # Try to assign windows starting with the smallest lexicographical order
    def backtrack(assignments, next_staff=1):
        if next_staff > n:
            return is_valid_assignment(assignments)

        for window in range(1, 4):
            assignments[next_staff] = window
            if backtrack(assignments, next_staff + 1):
                return True
            # If this assignment doesn't lead to a solution, reset and try the next window
            del assignments[next_staff]

        return False

    assignments = {}
    if backtrack(assignments):
        result = ['YES'] + [assignments[i] for i in range(1, n+1)]
    else:
        result = ['NO']

    return result

def main():
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    m = int(data[idx + 1])
    idx += 2
    
    conflicts = []
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        conflicts.append((u, v))
        idx += 2

    result = assign_windows(n, m, conflicts)
    print("\n".join(map(str, result)))

if __name__ == "__main__":
    main()