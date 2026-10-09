import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    T = int(data[1])
    deadline = T + 1
    
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
        
        # Check Routing Delay
        if p1 + p2 >= deadline:
            print(f"JOB {i+1}")
            return
            
    # Check Throughput Saturation
    if sum_p1 >= deadline:
        print("LOAD 1")
        return
    if sum_p2 >= deadline:
        print("LOAD 2")
        return

if __name__ == "__main__":
    main()