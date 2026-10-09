import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    j = int(data[idx]); idx += 1
    T = int(data[idx]); idx += 1
    
    sum1 = 0
    sum2 = 0
    found_job = -1
    
    for i in range(1, j + 1):
        p1 = int(data[idx]); idx += 1
        p2 = int(data[idx]); idx += 1
        sum1 += p1
        sum2 += p2
        if found_job == -1 and p1 + p2 > T:
            found_job = i
    
    if found_job != -1:
        print(f"JOB {found_job}")
    elif sum1 > T:
        print("LOAD 1")
    else:
        print("LOAD 2")

main()