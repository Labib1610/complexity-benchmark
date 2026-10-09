import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    j = int(data[idx]); idx += 1
    T = int(data[idx]); idx += 1
    
    total_p1 = 0
    total_p2 = 0
    
    for i in range(1, j + 1):
        p1 = int(data[idx]); idx += 1
        p2 = int(data[idx]); idx += 1
        total_p1 += p1
        total_p2 += p2
        
        if p1 + p2 > T:
            print(f"JOB {i}")
            return
    
    if total_p1 > T:
        print("LOAD 1")
        return
    
    print("LOAD 2")

main()