import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    j = int(data[0])
    T = int(data[1])
    p1s = []
    p2s = []
    idx = 2
    for i in range(j):
        p1 = int(data[idx])
        p2 = int(data[idx+1])
        idx += 2
        p1s.append(p1)
        p2s.append(p2)
    
    # Check JOB
    for i in range(j):
        if p1s[i] + p2s[i] > T:
            print(f"JOB {i+1}")
            return
    
    # Check LOAD 1
    sum_p1 = sum(p1s)
    max_p1 = max(p1s)
    min_p1 = min(p1s)
    if sum_p1 > 2*T - max_p1 - min_p1:
        print("LOAD 1")
        return
    
    # Check LOAD 2
    sum_p2 = sum(p2s)
    max_p2 = max(p2s)
    min_p2 = min(p2s)
    if sum_p2 > 2*T - max_p2 - min_p2:
        print("LOAD 2")
        return

if __name__ == "__main__":
    main()