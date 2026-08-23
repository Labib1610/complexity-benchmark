import sys
from itertools import product

def read_input():
    n, m = map(int, sys.stdin.readline().split())
    incompatible = set()
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        if u > v:
            u, v = v, u
        incompatible.add((u, v))
    return n, m, incompatible

def is_valid(n, incompatible, assignment):
    # Check if the assignment is valid
    for i in range(n):
        for j in range(i+1, n):
            if assignment[i] == assignment[j]:
                u, v = i+1, j+1
                if u > v:
                    u, v = v, u
                if (u, v) in incompatible:
                    return False
    return True

def solve():
    n, m, incompatible = read_input()
    
    # Try all possible assignments in lexicographical order
    for assignment in product([1, 2, 3], repeat=n):
        if is_valid(n, incompatible, assignment):
            print("YES")
            print(' '.join(map(str, assignment)))
            return
    
    print("NO")

solve()