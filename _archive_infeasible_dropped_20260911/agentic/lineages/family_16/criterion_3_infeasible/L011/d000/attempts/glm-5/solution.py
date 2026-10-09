import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    j = int(data[idx]); idx += 1
    T = int(data[idx]); idx += 1
    
    total1 = 0
    total2 = 0
    
    for i in range(1, j + 1):
        p1 = int(data[idx]); idx += 1
        p2 = int(data[idx]); idx += 1
        if p1 + p2 > T:
            print(f"JOB {i}")
            return
        total1 += p1
        total2 += p2
    
    if total1 > T:
        print("LOAD 1")
    else:
        print("LOAD 2")

main()