import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    T = int(next(it))
    
    p1_list = []
    p2_list = []
    
    for _ in range(j):
        p1 = int(next(it))
        p2 = int(next(it))
        p1_list.append(p1)
        p2_list.append(p2)
    
    # Check JOB condition: for each row, p1 + p2 <= T
    for i in range(j):
        if p1_list[i] + p2_list[i] > T:
            print(f"JOB {i + 1}")
            return
    
    # Check LOAD condition: sum of p values for a set must be <= T
    total1 = sum(p1_list)
    if total1 > T:
        print("LOAD 1")
        return
    
    total2 = sum(p2_list)
    if total2 > T:
        print("LOAD 2")
        return

if __name__ == "__main__":
    solve()