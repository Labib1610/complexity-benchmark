import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    T = int(data[1])
    
    jobs = []
    load1_total = 0
    load2_total = 0
    
    for i in range(j):
        p1 = int(data[2 + 2*i])
        p2 = int(data[3 + 2*i])
        jobs.append((p1, p2))
        load1_total += p1
        load2_total += p2
        
        # Check for job-specific contradiction
        if p1 + p2 > T:
            print(f"JOB {i + 1}")
            return
    
    # Check for load-specific contradiction
    if load1_total > T:
        print("LOAD 1")
        return
    if load2_total > T:
        print("LOAD 2")
        return

if __name__ == "__main__":
    main()