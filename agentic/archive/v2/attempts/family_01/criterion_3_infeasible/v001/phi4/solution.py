def find_mutually_incompatible_group():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    # Read the pairs of incompatible individuals
    edges = set()
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        if u > v:
            u, v = v, u
        edges.add((u, v))
        index += 2
    
    # Check all combinations of three individuals to find the lexicographically smallest incompatible group
    for a in range(1, n - 1):
        for b in range(a + 1, n):
            if (a, b) not in edges:
                continue
            for c in range(b + 1, n + 1):
                if (a, c) in edges and (b, c) in edges:
                    print(a, b, c)
                    return

if __name__ == "__main__":
    find_mutually_incompatible_group()