import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    j = int(data[0])
    A = []
    B = []
    idx = 1
    for _ in range(j):
        p1 = int(data[idx]); p2 = int(data[idx+1])
        idx += 2
        A.append(p1)
        B.append(p2)
    
    total_A = sum(A)
    max_B = max(B)
    ans = total_A + max_B
    print(ans)

solve()