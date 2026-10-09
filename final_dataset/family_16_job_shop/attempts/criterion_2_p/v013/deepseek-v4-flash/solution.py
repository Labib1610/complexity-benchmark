import sys

def solve():
    input = sys.stdin.readline
    j = int(input())
    A = []
    B = []
    for _ in range(j):
        p1, p2 = map(int, input().split())
        if p1 < p2:
            A.append((p1, p2))
        else:
            B.append((p1, p2))
    
    # Sort A by p1 ascending, B by p2 descending
    A.sort(key=lambda x: x[0])
    B.sort(key=lambda x: x[1], reverse=True)
    
    seq = A + B
    t1 = 0
    t2 = 0
    for p1, p2 in seq:
        t1 += p1
        if t2 < t1:
            t2 = t1
        t2 += p2
    print(t2)

if __name__ == "__main__":
    solve()