import sys

def main():
    data = sys.stdin.buffer.read().split()
    j = int(data[0])
    T = int(data[1])
    
    p1 = []
    p2 = []
    idx = 2
    for _ in range(j):
        p1.append(int(data[idx]))
        p2.append(int(data[idx+1]))
        idx += 2
    
    # Proof Type 1: each subsystem has dedicated manifolds
    for i in range(j):
        if p1[i] + p2[i] > T:
            print(f"JOB {i+1}")
            return
    
    # Proof Type 2: only Flux Compression, serial manifold
    total_p1 = sum(p1)
    if total_p1 > T:
        print("LOAD 1")
        return
    
    # Proof Type 3: only Plasma Venting, serial manifold
    total_p2 = sum(p2)
    if total_p2 > T:
        print("LOAD 2")
        return

if __name__ == "__main__":
    main()