import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    j = int(sys.stdin.readline())
    vessels = []
    for _ in range(j):
        p1, p2 = map(int, sys.stdin.readline().split())
        vessels.append((p1, p2))
    
    # Sort by p1 ascending, then by p2 descending for tie-breaking
    # This is a standard algorithm for minimizing makespan in two-machine flow shop
    vessels.sort(key=lambda x: (x[0], -x[1]))
    
    # Simulate the process
    local_time = 0
    federal_time = 0
    
    for p1, p2 in vessels:
        local_time += p1
        federal_time = max(federal_time, local_time) + p2
    
    print(federal_time)

threading.Thread(target=main).start()