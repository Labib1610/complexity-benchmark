import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    T = int(data[1])
    
    # Check for JOB i certificate
    for i in range(j):
        p1 = int(data[2 + 2*i])
        p2 = int(data[3 + 2*i])
        # Total required time for this job is p1 + p2
        # Available time is T
        if p1 + p2 > T:
            print(f"JOB {i + 1}")
            return
    
    # Check for LOAD c certificate
    # Sum of all p1 and p2
    sum_p1 = 0
    sum_p2 = 0
    for i in range(j):
        p1 = int(data[2 + 2*i])
        p2 = int(data[3 + 2*i])
        sum_p1 += p1
        sum_p2 += p2
    
    if sum_p1 > T:
        print("LOAD 1")
        return
    if sum_p2 > T:
        print("LOAD 2")
        return

if __name__ == "__main__":
    main()