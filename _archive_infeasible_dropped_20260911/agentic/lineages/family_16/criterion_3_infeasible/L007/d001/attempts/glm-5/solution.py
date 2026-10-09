import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    T = int(next(it))
    
    # Check JOB violation: any single item's total time exceeds T
    for i in range(1, j + 1):
        p1 = int(next(it))
        p2 = int(next(it))
        if p1 + p2 > T:
            print(f"JOB {i}")
            return
    
    # If no JOB violation, must be LOAD violation
    # Since problem guarantees exactly one violation exists and no JOB was found,
    # LOAD violation must exist. We need to find which stage.
    
    # Re-read data for LOAD check (we already consumed it above, so we need to adjust)
    # Actually, we need to re-process. Let's re-read.
    
    # Re-reading approach:
    # Reset iterator or re-split. Since data is already in memory, let's re-iterate.
    
    # We already consumed the data in the first loop. We need to re-process.
    # Let's re-read the data properly.
    
    # Actually, the above loop consumed the data. We need to store it or re-read.
    # Let's re-read the input.
    
    # Re-read input
    data = sys.stdin.read().split()
    # Wait, we already read everything. The iterator 'it' is exhausted.
    # We need to re-process the data list.
    
    # Let's re-process the data list.
    # data = sys.stdin.read().split() was called at the start.
    # We consumed it in the first loop.
    # We need to re-iterate from the start.
    
    # Re-iterate from the start
    it = iter(data)
    j = int(next(it))
    T = int(next(it))
    
    total_p1 = 0
    total_p2 = 0
    
    for _ in range(j):
        p1 = int(next(it))
        p2 = int(next(it))
        total_p1 += p1
        total_p2 += p2
    
    if total_p1 > T:
        print("LOAD 1")
    else:
        print("LOAD 2")

if __name__ == "__main__":
    solve()