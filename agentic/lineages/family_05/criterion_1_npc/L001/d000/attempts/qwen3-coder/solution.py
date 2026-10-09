from itertools import permutations

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    k = int(data[0])
    t = int(data[1])
    
    triples = []
    index = 2
    for _ in range(t):
        x = int(data[index])
        y = int(data[index+1])
        z = int(data[index+2])
        triples.append((x, y, z))
        index += 3
    
    # Try all permutations of the triples
    for perm in permutations(triples):
        if len(perm) < k:
            continue
            
        # Take first k elements
        selected = perm[:k]
        
        # Check if all x, y, z are unique
        x_set = set()
        y_set = set()
        z_set = set()
        
        valid = True
        for x, y, z in selected:
            if x in x_set or y in y_set or z in z_set:
                valid = False
                break
            x_set.add(x)
            y_set.add(y)
            z_set.add(z)
        
        if valid and len(x_set) == k and len(y_set) == k and len(z_set) == k:
            print("YES")
            for x, y, z in selected:
                print(x, y, z)
            return
    
    print("NO")

solve()