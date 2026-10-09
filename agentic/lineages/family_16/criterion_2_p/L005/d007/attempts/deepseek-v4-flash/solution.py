import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    j = int(data[0])
    neg = []
    pos = []
    S = 0
    idx = 1
    for _ in range(j):
        t1 = int(data[idx])
        t2 = int(data[idx+1])
        idx += 2
        S += t2
        d = t1 - t2
        if d < 0:
            neg.append((t2, d))
        else:
            pos.append((t2, d))
    
    # sort neg by t2 ascending
    neg.sort(key=lambda x: x[0])
    # sort pos by t2 descending
    pos.sort(key=lambda x: -x[0])
    
    order = neg + pos
    
    prefix = 0
    max_spike = 0
    for t2, d in order:
        prefix += d
        spike = S + prefix + t2
        if spike > max_spike:
            max_spike = spike
    
    print(max_spike)

if __name__ == "__main__":
    solve()