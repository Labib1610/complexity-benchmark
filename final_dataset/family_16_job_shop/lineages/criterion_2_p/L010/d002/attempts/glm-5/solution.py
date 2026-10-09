import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    
    total_d1 = 0
    total_d2 = 0
    max_gap = 0
    
    for _ in range(j):
        d1 = int(next(it))
        d2 = int(next(it))
        total_d1 += d1
        total_d2 += d2
        if d1 > d2:
            max_gap = max(max_gap, d1 - d2)
    
    result = total_d1 + total_d2 + max_gap
    print(result)

if __name__ == "__main__":
    solve()