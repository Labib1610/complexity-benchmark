import sys

def find_smallest_conflict_triple():
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    conflicts = []
    index = 2
    for _ in range(m):
        u, v = int(data[index]), int(data[index + 1])
        if u > v:
            u, v = v, u
        conflicts.append((u, v))
        index += 2
    
    # Sort conflicts to make sure we get lexicographically smallest pairs first
    conflicts.sort()
    
    # We will use a set of sets for quick lookup
    conflict_set = {i: set() for i in range(1, n + 1)}
    
    for u, v in conflicts:
        conflict_set[u].add(v)
        conflict_set[v].add(u)
    
    # Find the smallest triple (a, b, c) such that a < b < c
    for i in range(n):
        for j in range(i + 1, n):
            if (i + 1) not in conflict_set or (j + 1) not in conflict_set[i + 1]:
                continue
            u = i + 1
            v = j + 1
            
            # Check all k > j such that there's a conflict (u, k), (v, k)
            for k in range(j + 1, n):
                w = k + 1
                if w in conflict_set[u] and w in conflict_set[v]:
                    print(u, v, w)
                    return

find_smallest_conflict_triple()