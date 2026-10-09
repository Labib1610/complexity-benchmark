import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    q = int(next(it))
    t = int(next(it))
    
    n = 3 * q
    adj = [set() for _ in range(n + 1)]
    triples = []
    
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        triples.append((a, b, c))
        adj[a].add(b)
        adj[a].add(c)
        adj[b].add(a)
        adj[b].add(c)
        adj[c].add(a)
        adj[c].add(b)
    
    used = [False] * (n + 1)
    result = []
    
    # Process vertices with degree < 2 first (they must be in a specific triple)
    # We iterate until we've found q triples or can't proceed
    changed = True
    while changed and len(result) < q:
        changed = False
        for v in range(1, n + 1):
            if used[v]:
                continue
            # Count available neighbors
            avail_neighbors = [u for u in adj[v] if not used[u]]
            if len(avail_neighbors) < 2:
                # v must be in a triple with two specific neighbors
                # Find the triple containing v
                found = False
                for a, b, c in triples:
                    if a == v:
                        if not used[b] and not used[c]:
                            result.append((a, b, c))
                            used[a] = used[b] = used[c] = True
                            changed = True
                            found = True
                            break
                    elif b == v:
                        if not used[a] and not used[c]:
                            result.append((a, b, c))
                            used[a] = used[b] = used[c] = True
                            changed = True
                            found = True
                            break
                    elif c == v:
                        if not used[a] and not used[b]:
                            result.append((a, b, c))
                            used[a] = used[b] = used[c] = True
                            changed = True
                            found = True
                            break
                if found:
                    break
    
    # If we still need more triples, use greedy matching
    while len(result) < q:
        found = False
        for a, b, c in triples:
            if not used[a] and not used[b] and not used[c]:
                result.append((a, b, c))
                used[a] = used[b] = used[c] = True
                found = True
                break
        if not found:
            print("NO")
            return
    
    print("YES")
    for triple in result:
        print(triple[0], triple[1], triple[2])

solve()