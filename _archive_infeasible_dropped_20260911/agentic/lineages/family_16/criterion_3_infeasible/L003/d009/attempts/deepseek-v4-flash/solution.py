import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    j = int(data[0])
    T = int(data[1])
    
    lane1_total = 0
    lane2_total = 0
    
    idx = 2
    for i in range(1, j + 1):
        p1 = int(data[idx])
        p2 = int(data[idx + 1])
        idx += 2
        
        if p1 + p2 > T:
            print(f"JOB {i}")
            return
        
        lane1_total += p1
        lane2_total += p2
    
    if lane1_total > T:
        print("LOAD 1")
        return
    
    if lane2_total > T:
        print("LOAD 2")
        return

if __name__ == "__main__":
    main()