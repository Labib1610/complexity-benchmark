import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    j = int(data[idx]); idx += 1
    
    set1 = []  # p1 <= p2, sort by p1 ascending
    set2 = []  # p1 > p2, sort by p2 descending
    
    for _ in range(j):
        p1 = int(data[idx]); idx += 1
        p2 = int(data[idx]); idx += 1
        if p1 <= p2:
            set1.append((p1, p2))
        else:
            set2.append((p1, p2))
    
    set1.sort(key=lambda x: x[0])
    set2.sort(key=lambda x: x[1], reverse=True)
    
    t1 = 0
    t2 = 0
    for p1, p2 in set1:
        t1 += p1
        if t1 > t2:
            t2 = t1
        t2 += p2
    
    for p1, p2 in set2:
        t1 += p1
        if t1 > t2:
            t2 = t1
        t2 += p2
    
    print(t2)

main()