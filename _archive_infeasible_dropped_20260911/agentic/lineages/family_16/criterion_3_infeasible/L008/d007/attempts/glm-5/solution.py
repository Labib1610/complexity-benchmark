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
    
    # Check JOB condition: p1_k + p2_k > T
    for i in range(j):
        if p1_list[i] + p2_list[i] > T:
            print(f"JOB {i+1}")
            return
    
    # Check LOAD 1: sum of p1 > T
    if sum(p1_list) > T:
        print("LOAD 1")
        return
    
    # Check LOAD 2: sum of p2 > T
    if sum(p2_list) > T:
        print("LOAD 2")
        return
    
    # If none of the above, output JOB 1 as default (should not happen per problem guarantee)
    print("JOB 1")

if __name__ == "__main__":
    solve()