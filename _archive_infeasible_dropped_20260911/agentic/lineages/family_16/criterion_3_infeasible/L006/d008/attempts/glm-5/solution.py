import sys

def main():
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
    
    # Check Isolated Job Obstruction
    # For each job i, compute S + D when only job i is active
    # S = p1[i], D = max(0, 0 - p1[i]) + p2[i] = p2[i]
    # So metric = p1[i] + p2[i]
    for i in range(j):
        if p1_list[i] + p2_list[i] > T:
            print(f"JOB {i + 1}")
            return
    
    # Check Continuous Utilization Exhaustion for component 1
    # All v = 0, use u = p1[k]
    # D stays at 0 throughout (since D starts at 0, max(0, 0 - u) + 0 = 0)
    # S = sum of all p1[k]
    sum_p1 = sum(p1_list)
    if sum_p1 > T:
        print("LOAD 1")
        return
    
    # Check Continuous Utilization Exhaustion for component 2
    # All u = 0, use v = p2[k]
    # S stays at 0
    # D accumulates: D = D + p2[k] at each step
    # Final D = sum of all p2[k]
    sum_p2 = sum(p2_list)
    if sum_p2 > T:
        print("LOAD 2")
        return

if __name__ == "__main__":
    main()