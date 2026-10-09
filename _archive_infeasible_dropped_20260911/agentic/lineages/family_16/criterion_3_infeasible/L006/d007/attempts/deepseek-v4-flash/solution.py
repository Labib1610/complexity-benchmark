import sys

def main():
    input_data = sys.stdin.read().strip().split()
    j = int(input_data[0])
    T = int(input_data[1])
    
    p1 = []
    p2 = []
    idx = 2
    for _ in range(j):
        p1.append(int(input_data[idx]))
        p2.append(int(input_data[idx+1]))
        idx += 2
    
    # Check JOB condition
    for i in range(j):
        if p1[i] + p2[i] > T:
            print(f"JOB {i+1}")
            return
    
    # Check LOAD condition
    if sum(p1) > T:
        print("LOAD 1")
        return
    if sum(p2) > T:
        print("LOAD 2")
        return

if __name__ == "__main__":
    main()