import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    T = int(data[1])
    
    idx = 2
    jobs = []
    sum_p1 = 0
    sum_p2 = 0
    
    for i in range(j):
        p1 = int(data[idx])
        p2 = int(data[idx+1])
        idx += 2
        jobs.append((p1, p2))
        sum_p1 += p1
        sum_p2 += p2
        # Check if any individual job exceeds T
        if p1 + p2 > T:
            print(f"JOB {i+1}")
            return
    
    # Check if either unit is saturated
    if sum_p1 > T:
        print("LOAD 1")
    elif sum_p2 > T:
        print("LOAD 2")
    else:
        # This shouldn't happen according to problem statement,
        # but if it does, we'll default to one of the above.
        pass

if __name__ == "__main__":
    main()