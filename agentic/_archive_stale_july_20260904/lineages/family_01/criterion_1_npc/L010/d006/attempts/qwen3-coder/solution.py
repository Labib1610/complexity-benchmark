from itertools import product

def cross_product(a, b):
    # a = (1, f_u, f_u^2), b = (1, f_v, f_v^2)
    # Cross product = (f_u*f_v^2 - f_u^2*f_v, f_u^2*1 - 1*f_v^2, 1*f_v - f_u*1)
    #               = (f_u*f_v*(f_v - f_u), f_u^2 - f_v^2, f_v - f_u)
    return (a[1]*b[2] - a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]*b[1] - a[1]*b[0])

def will_resonate(f_u, f_v):
    a = (1, f_u, f_u*f_u)
    b = (1, f_v, f_v*f_v)
    cp = cross_product(a, b)
    return cp == (0, 0, 0)

def is_valid_solution(n, edges, assignment):
    for u, v in edges:
        if will_resonate(assignment[u-1], assignment[v-1]):
            return False
    return True

def solve():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    
    # Try all possible assignments in lexicographical order
    for assignment in product([1, 2, 3], repeat=n):
        if is_valid_solution(n, edges, assignment):
            print("YES")
            print(" ".join(map(str, assignment)))
            return
    
    print("NO")

solve()