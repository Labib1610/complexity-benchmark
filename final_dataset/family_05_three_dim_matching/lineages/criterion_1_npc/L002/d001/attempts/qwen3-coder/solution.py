from itertools import permutations

def solve():
    k, t = map(int, input().split())
    pathways = []
    for _ in range(t):
        u, v, w = map(int, input().split())
        pathways.append((u, v, w))
    
    # Try all permutations of k pathways
    for perm in permutations(range(t), k):
        selected = [pathways[i] for i in perm]
        
        # Check if all inputs, outputs, and frequencies are unique
        inputs = [p[0] for p in selected]
        outputs = [p[1] for p in selected]
        frequencies = [p[2] for p in selected]
        
        if (len(set(inputs)) == k and 
            len(set(outputs)) == k and 
            len(set(frequencies)) == k):
            print("YES")
            for u, v, w in selected:
                print(u, v, w)
            return
    
    print("NO")

solve()