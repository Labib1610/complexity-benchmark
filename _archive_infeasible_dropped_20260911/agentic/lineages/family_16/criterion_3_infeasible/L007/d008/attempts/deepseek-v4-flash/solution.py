import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    j = int(data[0])
    T = int(data[1])
    p1_list = []
    p2_list = []
    idx = 2
    for _ in range(j):
        p1 = int(data[idx])
        p2 = int(data[idx+1])
        idx += 2
        p1_list.append(p1)
        p2_list.append(p2)
    
    # Check JOB condition
    for i in range(j):
        if p1_list[i] + p2_list[i] > T:
            print(f"JOB {i+1}")
            return
    
    # Check LOAD condition
    if sum(p1_list) > T:
        print("LOAD 1")
        return
    if sum(p2_list) > T:
        print("LOAD 2")
        return

if __name__ == "__main__":
    main()