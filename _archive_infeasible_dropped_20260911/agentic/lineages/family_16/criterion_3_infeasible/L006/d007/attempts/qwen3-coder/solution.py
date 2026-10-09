import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    T = int(data[1])
    
    p1 = [0] * (j + 1)
    p2 = [0] * (j + 1)
    
    idx = 2
    for i in range(1, j + 1):
        p1[i] = int(data[idx])
        p2[i] = int(data[idx + 1])
        idx += 2

    # Check Continuous Utilization Exhaustion first
    # For machine 1: set all p2 to 0
    A = 0
    B = 0
    exceeds = False
    for k in range(1, j + 1):
        A = A + p1[k]
        B = max(A, B) + 0
    if B > T:
        exceeds = True
        print("LOAD 1")
        return

    # For machine 2: set all p1 to 0
    A = 0
    B = 0
    for k in range(1, j + 1):
        A = A + 0
        B = max(A, B) + p2[k]
    if B > T:
        exceeds = True
        print("LOAD 2")
        return

    # If not Continuous Utilization Exhaustion, then it must be Isolated Job Obstruction
    if not exceeds:
        # Find a job i such that processing only job i exceeds T
        for i in range(1, j + 1):
            # Simulate processing only job i
            A_prev = 0  # A_{i-1} for the hypothetical sequence
            B_prev = 0  # B_{i-1} for the hypothetical sequence
            A_i = A_prev + p1[i]
            B_i = max(A_i, B_prev) + p2[i]
            # For jobs after i, p1=p2=0, so A_k = A_i and B_k = max(A_i, B_{k-1}) + 0 = max(A_i, B_{k-1})
            # Since A_i is fixed, B_k will be max(A_i, B_{i}) for k > i
            # So final B_j = max(A_i, B_i)
            final_B = max(A_i, B_i)
            if final_B > T:
                print(f"JOB {i}")
                return

if __name__ == "__main__":
    main()