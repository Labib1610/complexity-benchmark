def solve():
    n, m = map(int, input().split())
    collisions = set()
    for _ in range(m):
        u, v = map(int, input().split())
        collisions.add(tuple(sorted((u, v))))
    
    best_triplet = None
    
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            for c in range(b + 1, n + 1):
                if (a, b) in collisions and (a, c) in collisions and (b, c) in collisions:
                    if best_triplet is None:
                        best_triplet = (a, b, c)
                    else:
                        if a < best_triplet[0]:
                            best_triplet = (a, b, c)
                        elif a == best_triplet[0] and b < best_triplet[1]:
                            best_triplet = (a, b, c)
                        elif a == best_triplet[0] and b == best_triplet[1] and c < best_triplet[2]:
                            best_triplet = (a, b, c)
    
    print(best_triplet[0], best_triplet[1], best_triplet[2])

solve()