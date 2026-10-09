import sys

def solve():
    data = sys.stdin.buffer.read().split()
    j = int(data[0])
    ships = []
    idx = 1
    for _ in range(j):
        t1 = int(data[idx])
        t2 = int(data[idx + 1])
        idx += 2
        ships.append((t1, t2))
    
    # Johnson's rule: sort by t1 if t1 < t2, else by t2 descending
    first = []
    second = []
    for t1, t2 in ships:
        if t1 < t2:
            first.append((t1, t2))
        else:
            second.append((t1, t2))
    
    first.sort(key=lambda x: x[0])
    second.sort(key=lambda x: x[1], reverse=True)
    
    order = first + second
    
    time1 = 0
    time2 = 0
    for t1, t2 in order:
        time1 += t1
        if time2 < time1:
            time2 = time1
        time2 += t2
    
    print(time2)

if __name__ == "__main__":
    solve()