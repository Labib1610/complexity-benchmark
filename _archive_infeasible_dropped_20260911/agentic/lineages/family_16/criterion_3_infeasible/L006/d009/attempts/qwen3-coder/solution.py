import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    T = int(data[1])
    p1 = []
    p2 = []
    
    index = 2
    for _ in range(j):
        p1.append(int(data[index]))
        p2.append(int(data[index+1]))
        index += 2
    
    # Check for Isolated Job Bottleneck
    for i in range(j):
        # Create hypothetical sequence where only job i has non-zero processing times
        E_prev = 0
        T_prev = 0
        for k in range(j):
            if k == i:
                E_k = E_prev + p1[k]
                T_k = max(E_k, T_prev) + p2[k]
            else:
                E_k = E_prev + 0
                T_k = max(E_k, T_prev) + 0
            E_prev = E_k
            T_prev = T_k
        if T_prev > T:
            print(f"JOB {i+1}")
            return
    
    # Check for Machine Saturation
    # Case LOAD 1: machine 2 takes 0 time
    E_prev = 0
    T_prev = 0
    for k in range(j):
        E_k = E_prev + p1[k]
        T_k = max(E_k, T_prev) + 0
        E_prev = E_k
        T_prev = T_k
    if T_prev > T:
        print("LOAD 1")
        return
    
    # Case LOAD 2: machine 1 takes 0 time
    E_prev = 0
    T_prev = 0
    for k in range(j):
        E_k = E_prev + 0
        T_k = max(E_k, T_prev) + p2[k]
        E_prev = E_k
        T_prev = T_k
    if T_prev > T:
        print("LOAD 2")
        return

if __name__ == "__main__":
    main()