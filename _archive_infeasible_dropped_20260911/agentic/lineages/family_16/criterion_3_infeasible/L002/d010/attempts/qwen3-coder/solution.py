import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    T = int(data[1])
    
    jobs = []
    total_milling = 0
    total_polishing = 0
    
    idx = 2
    for i in range(j):
        q1 = int(data[idx])
        q2 = int(data[idx+1])
        idx += 2
        jobs.append((q1, q2))
        total_milling += q1
        total_polishing += q2
        
        # Check JOB certificate
        if q1 + q2 > T:
            print(f"JOB {i+1}")
            return
    
    # Check LOAD certificates
    if total_milling > T:
        print("LOAD 1")
        return
        
    if total_polishing > T:
        print("LOAD 2")
        return

if __name__ == "__main__":
    main()