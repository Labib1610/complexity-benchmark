import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    q = int(next(it))
    t = int(next(it))
    
    n = 3 * q
    triads = []
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        triads.append((a, b, c))
    
    # Build adjacency list for each person
    adj = [[] for _ in range(n + 1)]
    for idx, (a, b, c) in enumerate(triads):
        adj[a].append(idx)
        adj[b].append(idx)
        adj[c].append(idx)
    
    used_triad = [False] * t
    used_person = [False] * (n + 1)
    result = []
    
    # Process persons in order
    for person in range(1, n + 1):
        if used_person[person]:
            continue
        # Find an unused triad containing this person
        found = False
        for ti in adj[person]:
            if used_triad[ti]:
                continue
            a, b, c = triads[ti]
            if used_person[a] or used_person[b] or used_person[c]:
                continue
            # Use this triad
            used_triad[ti] = True
            used_person[a] = True
            used_person[b] = True
            used_person[c] = True
            result.append((a, b, c))
            found = True
            break
        if not found:
            print("NO")
            return
    
    print("YES")
    for a, b, c in result:
        print(a, b, c)

if __name__ == "__main__":
    solve()