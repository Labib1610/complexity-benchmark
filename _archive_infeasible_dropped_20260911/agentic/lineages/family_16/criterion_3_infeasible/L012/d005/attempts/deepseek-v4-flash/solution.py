import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    j = int(data[0])
    T = int(data[1])
    
    p1_sum = 0
    p2_sum = 0
    
    idx = 2
    for i in range(1, j + 1):
        p1 = int(data[idx])
        p2 = int(data[idx + 1])
        idx += 2
        
        if p1 + p2 > T:
            print(f"JOB {i}")
            return
        
        p1_sum += p1
        p2_sum += p2
    
    if p1_sum > T:
        print("LOAD 1")
        return
    
    if p2_sum > T:
        print("LOAD 2")
        return

if __name__ == "__main__":
    main()