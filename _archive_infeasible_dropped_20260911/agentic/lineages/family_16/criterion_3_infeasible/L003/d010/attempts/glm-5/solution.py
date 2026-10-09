import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    j = int(data[idx]); idx += 1
    T = int(data[idx]); idx += 1
    
    p1_list = []
    p2_list = []
    sum1 = 0
    sum2 = 0
    
    for i in range(j):
        p1 = int(data[idx]); idx += 1
        p2 = int(data[idx]); idx += 1
        p1_list.append(p1)
        p2_list.append(p2)
        sum1 += p1
        sum2 += p2
        if p1 + p2 > T:
            print(f"JOB {i+1}")
            return
    
    if sum1 > T:
        print("LOAD 1")
    else:
        print("LOAD 2")

main()