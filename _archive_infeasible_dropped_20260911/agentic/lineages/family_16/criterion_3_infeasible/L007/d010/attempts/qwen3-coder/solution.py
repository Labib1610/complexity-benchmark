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
    
    # Check JOB condition for each row
    for i in range(j):
        p1 = p1_list[i]
        p2 = p2_list[i]
        # To satisfy Strict Abscissa Precedence, we need p1 + p2 columns at minimum for this row
        if p1 + p2 > T:
            print(f"JOB {i+1}")
            return
    
    # Check LOAD condition for set S1
    total_p1 = sum(p1_list)
    if total_p1 > T:
        print("LOAD 1")
        return
    
    # Check LOAD condition for set S2
    total_p2 = sum(p2_list)
    if total_p2 > T:
        print("LOAD 2")
        return
    
    # As per problem statement, exactly one condition must be the root cause.
    # But according to our checks, none failed. This shouldn't happen.
    # However, based on examples, it seems we should return the first failing condition.
    # Since we already checked JOB and LOAD above and none triggered, but the problem guarantees one,
    # let's recheck logic.
    # The example shows that even if individually sums are <= T, the combined constraint might fail.
    # But the problem says exactly one isolated condition is the root cause.
    # Let's assume that if we reach here, then it's LOAD 1 as default, but that's not right.
    # Re-examining example 2:
    # j=4, T=150
    # p1=[50,50,50,50] -> sum = 200 > 150 => LOAD 1
    # p2=[1,1,1,1] -> sum = 4 <= 150
    # So LOAD 1 is correct.
    # Example 1:
    # j=3, T=100
    # Row 1: p1=70, p2=60 => 70+60=130 <= 100? No, 130 > 100 => JOB 1
    # Our logic matches.
    # If we passed all checks, then there's no impossibility, but problem says one exists.
    # So we must have missed something.
    # Actually, the problem guarantees that exactly one of the conditions is the root cause.
    # So our order of checking matters: check JOB first, then LOAD.
    # If JOB doesn't trigger, then check LOAD.
    # If neither triggers, then there's an error in logic.
    # But since problem guarantees one, and our logic is sound, we should be fine.
    # Let's just ensure we're returning correctly.
    # In example 1, JOB 1 triggers.
    # In example 2, JOB doesn't trigger (50+1=51 <= 150), but LOAD 1 does (200 > 150).
    # So our logic is correct.

if __name__ == "__main__":
    main()