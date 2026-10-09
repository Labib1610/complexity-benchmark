import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    trains = []
    idx = 1
    for _ in range(n):
        s = int(data[idx])
        c = int(data[idx+1])
        idx += 2
        trains.append((s, c))
    
    # Johnson's rule
    front = []
    back = []
    for s, c in trains:
        if s < c:
            front.append((s, c))
        else:
            back.append((s, c))
    
    # Sort front by s ascending, back by c descending
    front.sort(key=lambda x: x[0])
    back.sort(key=lambda x: x[1], reverse=True)
    
    order = front + back
    
    A = 0
    B = 0
    for s, c in order:
        A += s
        B = max(A, B) + c
    
    print(B)

if __name__ == "__main__":
    solve()