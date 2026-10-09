from itertools import product

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n, m = int(data[0]), int(data[1])
    edges = []
    index = 2
    for _ in range(m):
        u = int(data[index]) - 1
        v = int(data[index+1]) - 1
        edges.append((u, v))
        index += 2
    
    # For each assignment, check if it's valid
    # We want the lexicographically smallest assignment that minimizes S
    # Since S = sum(s_i * 4^(n-i)), this is minimized by lexicographic order with priority on earlier elements
    
    # So we generate in lexicographic order of the assignments (1,1,...,1) to (3,3,...,3)
    # which is exactly what product does with repeat=n
    
    for assignment in product([1, 2, 3], repeat=n):
        valid = True
        for u, v in edges:
            su = assignment[u]
            sv = assignment[v]
            # Check if the equation t^2 - (su+sv)t + susv = 0 has distinct real roots
            # This happens when discriminant D = (su+sv)^2 - 4*susv > 0
            # D = (su)^2 + 2*susv + (sv)^2 - 4*susv = (su)^2 - 2*susv + (sv)^2 = (su - sv)^2
            # So D = (su - sv)^2 >= 0 always, and D = 0 iff su = sv
            # We need D > 0, i.e., su != sv
            if su == sv:
                valid = False
                break
        if valid:
            print("YES")
            print(' '.join(map(str, assignment)))
            return
    
    print("NO")

solve()