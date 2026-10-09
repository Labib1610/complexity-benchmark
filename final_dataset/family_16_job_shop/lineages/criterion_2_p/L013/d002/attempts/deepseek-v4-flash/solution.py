import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    j = int(data[0])
    trains = []
    idx = 1
    for _ in range(j):
        p1 = int(data[idx])
        p2 = int(data[idx+1])
        idx += 2
        trains.append((p1, p2))
    
    # Johnson's rule
    first = []
    second = []
    for p1, p2 in trains:
        if p1 <= p2:
            first.append((p1, p2))
        else:
            second.append((p1, p2))
    
    first.sort(key=lambda x: x[0])   # sort by p1 ascending
    second.sort(key=lambda x: x[1], reverse=True)  # sort by p2 descending
    
    order = first + second
    
    A = 0
    B = 0
    for p1, p2 in order:
        A += p1
        if B < A:
            B = A + p2
        else:
            B += p2
    
    print(B)

if __name__ == "__main__":
    solve()