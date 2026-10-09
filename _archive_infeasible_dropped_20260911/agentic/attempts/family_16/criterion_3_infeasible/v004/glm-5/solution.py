import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    T = int(next(it))
    
    total_m1 = 0
    total_m2 = 0
    
    for i in range(1, j + 1):
        p1 = int(next(it))
        p2 = int(next(it))
        
        if p1 + p2 > T:
            print(f"JOB {i}")
            return
        
        total_m1 += p1
        total_m2 += p2
    
    if total_m1 > T:
        print("LOAD 1")
    elif total_m2 > T:
        print("LOAD 2")

if __name__ == "__main__":
    solve()