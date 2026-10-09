import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    j = int(data[idx]); idx += 1
    T = int(data[idx]); idx += 1
    
    sum1 = 0
    sum2 = 0
    
    for i in range(1, j + 1):
        p1 = int(data[idx]); idx += 1
        p2 = int(data[idx]); idx += 1
        if p1 + p2 > T:
            print(f"JOB {i}")
            return
        sum1 += p1
        sum2 += p2
    
    if sum1 > T:
        print("LOAD 1")
    else:
        print("LOAD 2")

main()