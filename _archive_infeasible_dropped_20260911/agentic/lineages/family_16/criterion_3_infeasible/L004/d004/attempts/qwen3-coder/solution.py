import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    T = int(data[1])
    
    p1_list = []
    p2_list = []
    
    index = 2
    for _ in range(j):
        p1 = int(data[index])
        p1_list.append(p1)
        index += 1
        p2 = int(data[index])
        p2_list.append(p2)
        index += 1
    
    # Check for isolation witness
    for i in range(j):
        p1 = p1_list[i]
        p2 = p2_list[i]
        # Minimum time needed is p1 + p2 (since we must wait for p1 to finish before starting p2)
        if p1 + p2 > T:
            print(f"JOB {i+1}")
            return
    
    # Check for relaxation witness
    total_p1 = sum(p1_list)
    total_p2 = sum(p2_list)
    
    if total_p1 > T:
        print("LOAD 1")
        return
    if total_p2 > T:
        print("LOAD 2")
        return
    
    # If we reach here, there should be a contradiction since the problem guarantees unsatisfiability
    # But according to problem statement, exactly one of the two cases must hold.
    # Let's re-check logic.
    
    # Actually, the isolation check is: can job i finish by T even if it's the only job?
    # That means: S1 >=0, S2 >= S1 + p1, and both S1+p1 <= T and S2+p2 <= T
    # => S1 + p1 <= T and S2 + p2 <= T
    # Since S2 >= S1 + p1, we have S2 >= 0 + p1 = p1
    # So S2 + p2 >= p1 + p2
    # Therefore, we need p1 + p2 <= T for each job individually.
    # If any job has p1 + p2 > T, then JOB i is the answer.
    
    # Else, we check if total load on any machine exceeds T.
    # In relaxed problem, jobs can overlap in time on each machine,
    # but still each job must finish on both machines by T.
    # So on each machine, total processing time must be <= T.
    
    # This should have been caught above already.
    # Let's just ensure we cover all cases as per problem statement.
    
    # Reiterate: 
    # Case 1: Some job i has p1_i + p2_i > T  => JOB i
    # Case 2: Sum of p1's > T OR sum of p2's > T => LOAD c
    
    # We already checked both. There must be an issue with logic or understanding.
    # Wait, let's re-read example 1:
    # p1=70, p2=60. Min time is 70+60=130 > 100. So JOB 1.
    # Example 2: All p1=50, p2=1. Each job needs 50+1=51 <= 150. 
    # But sum of p1 = 4*50 = 200 > 150. So LOAD 1.
    
    # Our logic seems correct. But we must make sure we return something.
    # According to problem, one of them MUST hold.
    # If neither isolation nor load holds, then maybe integer overflow or misreading?
    # No, constraints say T up to 1e9, j up to 2e5, pi up to 1e6.
    # So sum can be up to 2e11 which fits in long long.
    
    # Let's double-check with examples:
    
    # Example 1:
    # Job 1: 70 + 60 = 130 > 100 => JOB 1. Correct.
    
    # Example 2:
    # Jobs: (50,1), (50,1), (50,1), (50,1)
    # Isolation: 50+1=51 <= 150. Not violated.
    # Load: sum(p1)=200 > 150 => LOAD 1. Correct.
    
    # So our approach is right. Just implement carefully.
    
    # Final implementation:
    
    # Check isolation
    for i in range(j):
        if p1_list[i] + p2_list[i] > T:
            print(f"JOB {i+1}")
            return
            
    # Check load
    if sum(p1_list) > T:
        print("LOAD 1")
        return
    if sum(p2_list) > T:
        print("LOAD 2")
        return

if __name__ == "__main__":
    main()