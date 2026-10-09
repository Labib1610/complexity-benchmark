import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    j = int(data[0])
    T = int(data[1])
    p1 = []
    p2 = []
    idx = 2
    for _ in range(j):
        a = int(data[idx])
        b = int(data[idx+1])
        idx += 2
        p1.append(a)
        p2.append(b)
    
    # Check JOB i
    for i in range(j):
        if p1[i] + p2[i] > T:
            print(f"JOB {i+1}")
            return
    
    # Check LOAD 1
    if sum(p1) > T:
        print("LOAD 1")
        return
    
    # Check LOAD 2
    if sum(p2) > T:
        print("LOAD 2")
        return

if __name__ == "__main__":
    main()