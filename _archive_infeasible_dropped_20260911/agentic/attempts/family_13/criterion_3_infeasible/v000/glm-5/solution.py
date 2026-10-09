import sys
import math

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    d = list(map(int, data[1:1+n]))
    
    total = sum(d)
    
    # Check ODD first
    if total % 2 == 1:
        print("ODD")
        return
    
    # Check MAX
    half = total // 2
    if max(d) > half:
        print("MAX")
        return
    
    # Check MOD: find GCD of all durations
    g = 0
    for x in d:
        g = math.gcd(g, x)
    
    if g >= 2 and (half % g != 0):
        print(f"MOD {g}")
        return
    
    # This case shouldn't happen per problem statement
    # but we need to handle it somehow
    print("ODD")

if __name__ == "__main__":
    solve()