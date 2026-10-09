import sys

def main():
    data = sys.stdin.buffer.read().split()
    j = int(data[0])
    T = int(data[1])
    
    q1_sum = 0
    q2_sum = 0
    
    idx = 2
    for i in range(1, j + 1):
        q1 = int(data[idx])
        q2 = int(data[idx + 1])
        idx += 2
        
        if q1 + q2 > T:
            print(f"JOB {i}")
            return
        
        q1_sum += q1
        q2_sum += q2
    
    if q1_sum > T:
        print("LOAD 1")
        return
    
    if q2_sum > T:
        print("LOAD 2")
        return

if __name__ == "__main__":
    main()