import math
from itertools import product

def gcd_factorials(a, b):
    # gcd(a!, b!) = min(a,b)!
    return math.factorial(min(a, b))

def satisfies_condition(cu, cv):
    gcd_fact = gcd_factorials(cu, cv)
    max_val = max(cu, cv)
    return gcd_fact < max_val

def check_sequence(seq, conditions):
    for u, v in conditions:
        if not satisfies_condition(seq[u-1], seq[v-1]):
            return False
    return True

def main():
    n, m = map(int, input().split())
    conditions = []
    for _ in range(m):
        u, v = map(int, input().split())
        conditions.append((u, v))
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Try all possible sequences
    for seq in product([1, 2, 3], repeat=n):
        if check_sequence(seq, conditions):
            print("YES")
            print(" ".join(map(str, seq)))
            return
    
    print("NO")

if __name__ == "__main__":
    main()