import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    j = int(data[0])
    vessels = []
    idx = 1
    for _ in range(j):
        p1 = int(data[idx]); p2 = int(data[idx+1])
        idx += 2
        vessels.append((p1, p2))
    
    # Sort by p2 descending, then p1 ascending
    vessels.sort(key=lambda x: (-x[1], x[0])))
    
    L = 0
    F = 0
    for p1, p2 in vessels:
        L += p1
        if F > L:
            F = F + p2
        else:
            F = L + p2
    
    print(F)

if __name__ == "__main__":
    solve()