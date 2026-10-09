import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    j = int(next(it))
    commissions = []
    for _ in range(j):
        p1 = int(next(it))
        p2 = int(next(it))
        commissions.append((p1, p2))
    
    # Johnson's rule: sort by key
    # If p1 <= p2: key = (0, p1)
    # If p1 > p2:  key = (1, -p2)
    # This sorts group 0 first (by p1 ascending), then group 1 (by p2 descending)
    commissions.sort(key=lambda x: (0, x[0]) if x[0] <= x[1] else (1, -x[1]))
    
    time_a = 0
    time_b = 0
    
    for p1, p2 in commissions:
        time_a += p1
        # Artist B starts when both: commission is done with A, and B is free
        time_b = max(time_b, time_a) + p2
    
    print(time_b)

if __name__ == "__main__":
    solve()