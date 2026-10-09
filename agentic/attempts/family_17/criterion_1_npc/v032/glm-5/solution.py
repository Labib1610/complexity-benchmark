import sys
input = sys.stdin.readline

def solve():
    q, t = map(int, input().split())
    n = 3 * q
    
    # Read triples
    triples = []
    for _ in range(t):
        a, b, c = map(int, input().split())
        triples.append((a, b, c))
    
    # Build adjacency list for edges (a, b) -> c
    adj = {}
    for a, b, c in triples:
        adj[(a, b)] = c
        adj[(a, c)] = b
        adj[(b, c)] = a
    
    # Greedy matching
    match = [0] * (n + 1)
    
    for a in range(1, n + 1):
        if match[a] != 0:
            continue
        
        # Try to find a triple starting with a
        found = False
        for b in range(a + 1, n + 1):
            if match[b] != 0:
                continue
            c = adj.get((a, b))
            if c is not None and c > b and match[c] == 0:
                match[a] = b
                match[b] = a
                match[c] = -1  # Mark c as used (third element)
                found = True
                break
        
        if found:
            continue
        
        # Try to find a triple where a is the second element
        for b in range(1, a):
            if match[b] != 0:
                continue
            c = adj.get((b, a))
            if c is not None and c > a and match[c] == 0:
                match[b] = a
                match[a] = b
                match[c] = -1
                found = True
                break
    
    # Check if all vertices are matched
    for i in range(1, n + 1):
        if match[i] == 0:
            print("NO")
            return
    
    print("YES")
    
    # Output the triples
    used = [False] * (n + 1)
    for a in range(1, n + 1):
        if used[a]:
            continue
        b = match[a]
        if b == -1:
            continue  # This is a third element, skip
        c = adj.get((min(a, b), max(a, b)))
        print(a, b, c)
        used[a] = True
        used[b] = True
        used[c] = True

solve()