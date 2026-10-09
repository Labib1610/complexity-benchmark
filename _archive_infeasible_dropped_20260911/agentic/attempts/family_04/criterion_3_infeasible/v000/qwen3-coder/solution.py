import math
from functools import reduce

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def main():
    n = int(input())
    costs = list(map(int, input().split()))
    T = int(input())
    
    total_sum = sum(costs)
    
    # Check if SUM condition applies
    if T > total_sum:
        print("SUM")
        return
    
    # Find GCD of all costs
    overall_gcd = reduce(gcd, costs)
    
    # Check if there's a divisor >= 2 that divides all costs but not T
    if overall_gcd > 1:
        # Check if overall_gcd itself doesn't divide T
        if T % overall_gcd != 0:
            print(f"MOD {overall_gcd}")
            return
            
        # Otherwise, find a factor of overall_gcd that doesn't divide T
        # We'll check prime factors of overall_gcd
        temp_gcd = overall_gcd
        d = 2
        while d * d <= temp_gcd:
            if temp_gcd % d == 0:
                # d is a prime factor
                if T % d != 0:
                    print(f"MOD {d}")
                    return
                # Remove all instances of d from temp_gcd
                while temp_gcd % d == 0:
                    temp_gcd //= d
            d += 1
        
        # If temp_gcd is still > 1, then it's a prime factor
        if temp_gcd > 1 and T % temp_gcd != 0:
            print(f"MOD {temp_gcd}")
            return
    
    # This shouldn't happen according to problem guarantee
    # But we must output something
    print("SUM")

if __name__ == "__main__":
    main()