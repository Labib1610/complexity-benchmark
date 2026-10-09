import sys

def solve():
    input = sys.stdin.readline
    j = int(input())
    jobs = []
    for _ in range(j):
        p1, p2 = map(int, input().split())
        jobs.append((p1, p2))
    
    # Sort jobs using Johnson's rule
    A = []  # jobs where p1 <= p2
    B = []  # jobs where p1 > p2
    for p1, p2 in jobs:
        if p1 <= p2:
            A.append((p1, p2))
        else:
            B.append((p1, p2))
    
    # A sorted by p1 ascending
    A.sort(key=lambda x: x[0])
    # B sorted by p2 descending
    B.sort(key=lambda x: x[1], reverse=True)
    
    order = A + B
    
    time1 = 0
    time2 = 0
    for p1, p2 in order:
        time1 += p1
        if time2 < time1:
            time2 = time1
        time2 += p2
    
    print(time2)

if __name__ == "__main__":
    solve()