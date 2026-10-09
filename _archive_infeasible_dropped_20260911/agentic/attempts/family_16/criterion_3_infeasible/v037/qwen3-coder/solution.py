import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    T = int(data[1])
    
    idx = 2
    jobs = []
    total_p1 = 0
    total_p2 = 0
    
    for i in range(j):
        p1 = int(data[idx])
        p2 = int(data[idx+1])
        idx += 2
        jobs.append((p1, p2))
        total_p1 += p1
        total_p2 += p2
        if p1 + p2 > T:
            print(f"JOB {i+1}")
            return
    
    if total_p1 > T:
        print("LOAD 1")
    elif total_p2 > T:
        print("LOAD 2")
    else:
        # This shouldn't happen according to problem statement,
        # but we'll handle it just in case.
        pass

if __name__ == "__main__":
    main()