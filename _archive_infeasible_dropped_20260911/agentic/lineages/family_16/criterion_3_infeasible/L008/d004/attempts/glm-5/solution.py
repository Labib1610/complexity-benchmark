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
    
    # Check JOB i: Rules A and B contradiction for individual job
    # Rule A: 0 <= G_k, G_k + p1 <= T, 0 <= S_k, S_k + p2 <= T
    # Rule B: G_k + p1 <= S_k
    # Combining: p1 <= S_k - G_k <= T - p2 - G_k
    # Since G_k >= 0, we need p1 <= T - p2
    # If p1 + p2 > T, contradiction
    
    for i in range(j):
        if p1_list[i] + p2_list[i] > T:
            print(f"JOB {i + 1}")
            return
    
    # Check LOAD 1: Rules A and C contradiction for gimbal phases
    # Rule A: Each gimbal phase fits in window
    # Rule C: Gimbal phases don't overlap
    # Total time needed = sum of all p1
    # If sum(p1) > T, contradiction
    
    total_p1 = sum(p1_list)
    if total_p1 > T:
        print("LOAD 1")
        return
    
    # Check LOAD 2: Rules A and D contradiction for sensor phases
    # Rule A: Each sensor phase fits in window
    # Rule D: Sensor phases don't overlap
    # Total time needed = sum of all p2
    # If sum(p2) > T, contradiction
    
    total_p2 = sum(p2_list)
    if total_p2 > T:
        print("LOAD 2")
        return
    
    # Should not reach here given problem guarantees
    print("LOAD 1")

if __name__ == "__main__":
    solve()