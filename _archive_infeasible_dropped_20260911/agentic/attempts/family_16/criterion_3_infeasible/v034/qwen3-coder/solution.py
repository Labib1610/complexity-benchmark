import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    T = int(data[1])
    
    # Precompute totals for both specialists
    total_1 = 0
    total_2 = 0
    
    # Also check for any single job that exceeds T
    for i in range(j):
        p1 = int(data[2 + 2*i])
        p2 = int(data[2 + 2*i + 1])
        total_1 += p1
        total_2 += p2
        if p1 + p2 > T:
            print(f"JOB {i+1}")
            return
    
    # If no single job exceeds T, check for overloaded specialists
    if total_1 > T:
        print("LOAD 1")
        return
    if total_2 > T:
        print("LOAD 2")
        return

if __name__ == "__main__":
    main()