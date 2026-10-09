import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    T = int(next(it))
    p1_list = []
    p2_list = []
    for _ in range(j):
        p1 = int(next(it))
        p2 = int(next(it))
        p1_list.append(p1)
        p2_list.append(p2)
    
    # Check Scenario A: single query i fails
    for i in range(j):
        if p1_list[i] + p2_list[i] > T:
            print(f"JOB {i+1}")
            return
    
    # Check Scenario B: Component 2 is infinitely fast (0 time)
    # Only Component 1 matters, must process all sequentially
    total_p1 = sum(p1_list)
    if total_p1 > T:
        print("LOAD 1")
        return
    
    # Check Scenario C: Component 1 is infinitely fast (0 time)
    # Only Component 2 matters, must process all sequentially
    total_p2 = sum(p2_list)
    if total_p2 > T:
        print("LOAD 2")
        return

if __name__ == "__main__":
    solve()