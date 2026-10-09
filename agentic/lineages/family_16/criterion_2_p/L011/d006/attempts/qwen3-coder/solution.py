import sys
import threading

def main():
    import sys
    j = int(sys.stdin.readline())
    operations = []
    for _ in range(j):
        p1, p2 = map(int, sys.stdin.readline().split())
        operations.append((p1, p2))
    
    # Sort operations by p1 - p2 in ascending order (increasing p1 - p2)
    # This is the optimal ordering to minimize the total completion time
    operations.sort(key=lambda x: x[0] - x[1])
    
    # Simulate the process
    prepare_time = 0
    finalize_time = 0
    
    for p1, p2 in operations:
        prepare_time += p1
        finalize_time = max(finalize_time, prepare_time) + p2
    
    print(finalize_time)

# Use threading to increase recursion limit if needed, though not necessary for this approach
threading.Thread(target=main).start()