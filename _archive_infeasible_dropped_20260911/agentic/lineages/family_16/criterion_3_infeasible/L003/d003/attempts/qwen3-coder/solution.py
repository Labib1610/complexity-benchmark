import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    T = int(data[1])
    jobs = []
    index = 2
    for i in range(j):
        p1 = int(data[index])
        p2 = int(data[index+1])
        jobs.append((p1, p2))
        index += 2
    
    # Check for JOB certificate
    for i in range(j):
        p1, p2 = jobs[i]
        if p1 + p2 > T:
            print(f"JOB {i+1}")
            return
    
    # Check for LOAD certificates
    total_p1 = sum(job[0] for job in jobs)
    if total_p1 > T:
        print("LOAD 1")
        return
        
    total_p2 = sum(job[1] for job in jobs)
    if total_p2 > T:
        print("LOAD 2")
        return

if __name__ == "__main__":
    main()