import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    T = int(next(it))
    
    total_uplink = 0
    total_downlink = 0
    
    for i in range(1, j + 1):
        p1 = int(next(it))
        p2 = int(next(it))
        
        # Check for isolated structural impossibility
        if p1 + p2 > T:
            print(f"JOB {i}")
            return
        
        total_uplink += p1
        total_downlink += p2
    
    # Check for aggregate throughput failure
    if total_uplink > T:
        print("LOAD 1")
    else:
        print("LOAD 2")

if __name__ == "__main__":
    solve()