import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    T = int(data[1])
    
    index = 2
    jobs = []
    sum1 = 0
    sum2 = 0
    
    for i in range(j):
        p1 = int(data[index])
        p2 = int(data[index+1])
        index += 2
        jobs.append((p1, p2))
        sum1 += p1
        sum2 += p2
        # Check if a single job is too long
        if p1 + p2 > T:
            print(f"JOB {i+1}")
            return
    
    # Check if a machine is overloaded
    if sum1 > T:
        print("LOAD 1")
        return
    if sum2 > T:
        print("LOAD 2")
        return

if __name__ == "__main__":
    main()