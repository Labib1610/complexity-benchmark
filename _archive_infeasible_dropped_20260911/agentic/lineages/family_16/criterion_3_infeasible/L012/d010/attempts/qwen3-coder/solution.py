import sys
import threading

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    j = int(data[0])
    T = int(data[1])
    
    durations = []
    idx = 2
    for _ in range(j):
        p1 = int(data[idx])
        p2 = int(data[idx+1])
        durations.append((p1, p2))
        idx += 2

    # Proof Type 1: Check if any job exceeds T with dedicated manifolds
    for i in range(j):
        p1, p2 = durations[i]
        finish_time = p1 + p2
        if finish_time > T:
            print(f"JOB {i+1}")
            return

    # Proof Type 2: Only Flux Compression, sum all p1
    total_flux = sum(p1 for p1, p2 in durations)
    if total_flux > T:
        print("LOAD 1")
        return

    # Proof Type 3: Only Plasma Venting, sum all p2
    total_venting = sum(p2 for p1, p2 in durations)
    if total_venting > T:
        print("LOAD 2")
        return

# Use threading to increase recursion limit if needed, though not necessary here
threading.Thread(target=main).start()