from itertools import permutations

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    k = int(data[0])
    t = int(data[1])
    
    triples = []
    idx = 2
    for _ in range(t):
        e = int(data[idx])
        s = int(data[idx+1])
        p = int(data[idx+2])
        triples.append((e, s, p))
        idx += 3
    
    # Try all permutations of triples
    from itertools import permutations as perm
    
    for selected in perm(triples, k):
        enzymes = [x[0] for x in selected]
        substrates = [x[1] for x in selected]
        profiles = [x[2] for x in selected]
        
        if len(set(enzymes)) == k and len(set(substrates)) == k and len(set(profiles)) == k:
            print("YES")
            for e, s, p in selected:
                print(e, s, p)
            return
            
    print("NO")

solve()