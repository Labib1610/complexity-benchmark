import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    j = int(data[0])
    jobs = []
    idx = 1
    for _ in range(j):
        p1 = int(data[idx]); p2 = int(data[idx+1])
        idx += 2
        jobs.append((p1, p2))
    
    # Sort by extraction time descending
    jobs.sort(key=lambda x: x[0], reverse=True)
    
    total_extraction = 0
    current_time =  ​0
    for p1, p2 in jobs:
        total_extraction += p1
        # The transformation stage can start at max(current_time, total_extraction)
        # and finishes at max(current_time, total_extraction) + p2
        current_time = max(current_time, total_extraction) + p2
    
    print(current_time)

if __name__ == "__main__":
    solve()