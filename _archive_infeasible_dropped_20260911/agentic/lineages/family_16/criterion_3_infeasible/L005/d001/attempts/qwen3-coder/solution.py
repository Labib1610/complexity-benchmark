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
        p2 = int(data[index+1])
        p1_list.append(p1)
        p2_list.append(p2)
        index += 2
        
    # Check for Routing Delay
    for i in range(j):
        if p1_list[i] + p2_list[i] > T:
            print(f"JOB {i+1}")
            return
            
    # Check for Throughput Saturation
    total_p1 = sum(p1_list)
    total_p2 = sum(p2_list)
    
    if total_p1 > T:
        print("LOAD 1")
        return
    if total_p2 > T:
        print("LOAD 2")
        return
        
    # If we reach here, there should be no valid schedule
    # But according to problem statement, exactly one category applies
    # So we must have missed something - let's recheck logic
    
    # The problem guarantees that no valid schedule exists
    # So one of the above conditions must be true
    # But let's consider that both routing delay and throughput 
    # saturation might not occur, yet still no schedule exists
    
    # Actually, the problem says exactly one applies when no schedule exists
    # So we just need to check which one is the reason
    
    # But we already checked both. Let's see if there's another case
    # Wait, the problem guarantees that exactly one of the two applies
    # when no valid schedule exists. So our logic should be correct.
    
    # Let's double-check with examples:
    # Example 1: job 1 needs 70+60=130 > 100 => JOB 1
    # Example 2: total p1 = 200 > 150 => LOAD 1
    
    # But what if neither condition is met? The problem says 
    # that for every given configuration, no valid schedule exists
    # and exactly one category applies. So we must have one of them.
    
    # Let's think of a case where total_p1 <= T and total_p2 <= T
    # and for all i, p1[i] + p2[i] <= T, but still no schedule exists.
    # This is possible due to the ordering constraints.
    
    # But the problem says exactly one of the two proof categories applies.
    # So if neither Routing Delay nor Throughput Saturation applies,
    # then the problem statement would be wrong.
    
    # Re-reading: "For every given configuration, no valid schedule exists"
    # "Exactly one of the following two proof categories will apply"
    
    # So our approach is correct. One of them must apply.
    # If we checked both and none triggered, there's a logic error.
    
    # Actually, let's just implement the checks as described:
    
    # Check 1: Routing Delay - any job's p1 + p2 > T
    for i in range(j):
        if p1_list[i] + p2_list[i] > T:
            print(f"JOB {i+1}")
            return
    
    # Check 2: Throughput Saturation - total processing time at a station > T
    if sum(p1_list) > T:
        print("LOAD 1")
        return
        
    if sum(p2_list) > T:
        print("LOAD 2")
        return

if __name__ == "__main__":
    main()