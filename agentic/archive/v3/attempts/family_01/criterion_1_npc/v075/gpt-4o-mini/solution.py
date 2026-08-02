def can_assign_tags(n, m, conflicts):
    from itertools import product
    
    # Create a graph representation of the conflicts
    graph = [[] for _ in range(n)]
    for u, v in conflicts:
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    # Try all possible assignments for 3 tags using the product
    for assignment in product(range(1, 4), repeat=n):
        valid = True
        for u in range(n):
            for v in graph[u]:
                if assignment[u] == assignment[v]:  # Conflict found
                    valid = False
                    break
            if not valid:
                break
        if valid:
            return (True, assignment)

    return (False,)

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    n, m = map(int, data[0].split())
    conflicts = [tuple(map(int, line.split())) for line in data[1:m + 1]]
    
    result = can_assign_tags(n, m, conflicts)
    if result[0]:
        print("YES")
        print(" ".join(map(str, result[1])))
    else:
        print("NO")

if __name__ == "__main__":
    main()