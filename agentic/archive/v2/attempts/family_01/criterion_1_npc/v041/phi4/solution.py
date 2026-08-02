import sys

def main():
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    conflicts = []
    index = 2
    
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        conflicts.append((u - 1, v - 1))
        index += 2

    # Create adjacency list
    adj = [[] for _ in range(n)]
    for u, v in conflicts:
        adj[u].append(v)
        adj[v].append(u)

    def is_valid(assignment):
        for i in range(n):
            if assignment[i] == 0:
                continue
            shift = assignment[i]
            for neighbor in adj[i]:
                if assignment[neighbor] == shift:
                    return False
        return True

    from itertools import product

    # Try all possible assignments using shifts 1, 2, 3 (represented as 1, 2, 3)
    best_assignment = None
    found_valid = False

    for assignment in product([0, 1, 2, 3], repeat=n):
        if is_valid(assignment):
            found_valid = True
            # Convert to 1-based indexing and ignore zeros (unassigned)
            candidate = [x + 1 if x != 0 else 0 for x in assignment]
            if best_assignment is None or candidate < best_assignment:
                best_assignment = candidate

    if found_valid:
        print("YES")
        print(' '.join(map(str, best_assignment)))
    else:
        print("NO")

if __name__ == "__main__":
    main()