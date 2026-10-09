import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    
    idx = 0
    n = int(data[idx]); idx += 1
    T = int(data[idx]); idx += 1
    
    sum1 = 0
    sum2 = 0
    
    for i in range(1, n + 1):
        a = int(data[idx]); idx += 1
        b = int(data[idx]); idx += 1
        if a + b > T:
            print(f"JOB {i}")
            return
        sum1 += a
        sum2 += b
    
    if sum1 > T:
        print("LOAD 1")
        return
    if sum2 > T:
        print("LOAD 2")
        return

if __name__ == "__main__":
    main()