import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    j = int(data[0])
    idx = 1
    A = []  # p1 <= p2, sort by p1 ascending
    B = []  # p1 > p2, sort by p2 descending
    for _ in range(j):
        p1 = int(data[idx]); p2 = int(data[idx+1])
        idx += 2
        if p1 <= p2:
            A.append((p1, p2))
        else:
            B.append((p1, p2))
    A.sort(key=lambda x: x[0])
    B.sort(key=lambda x: x[1], reverse=True)
    
    upper_free = 0
    lower_free = 0
    for p1, p2 in A:
        upper_free += p1
        if upper_free > lower_free:
            lower_free = upper_free + p2
        else:
            lower_free += p2
    for p1, p2 in B:
        upper_free += p1
        if upper_free > lower_free:
            lower_free = upper_free + p2
        else:
            lower_free += p2
    
    print(lower_free)

main()