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
    for _ in range(j):
        p1 = int(data[idx])
        p2 = int(data[idx+1])
        idx += 2
        p1s.append(p1)
        p2s.append(p2)
    
    # Check separation failure
    for i in range(j):
        if p1s[i] + p2s[i] > T:
            print(f"JOB {i+1}")
            return
    
    # Check X exhaustion
    if sum(p1s) > T:
        print("LOAD 1")
        return
    
    # Check Y exhaustion
    if sum(p2s) > T:
        print("LOAD 2")
        return

if __name__ == "__main__":
    main()