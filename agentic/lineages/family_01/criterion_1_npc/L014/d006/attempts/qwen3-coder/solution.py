def check_resonance(x, y):
    # Calculate x^3 + y^3 + x*y
    val = x**3 + y**3 + x*y
    # Check if it ends in digit 1
    return val % 10 == 1

def is_valid_assignment(n, edges, assignment):
    for u, v in edges:
        if check_resonance(assignment[u-1], assignment[v-1]):
            return False
    return True

def solve():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    
    # If no edges, any assignment works
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Try all possible assignments
    for i in range(3**n):
        assignment = []
        temp = i
        for _ in range(n):
            assignment.append((temp % 3) + 1)
            temp //= 3
        
        if is_valid_assignment(n, edges, assignment):
            print("YES")
            print(" ".join(map(str, assignment)))
            return
    
    print("NO")

solve()