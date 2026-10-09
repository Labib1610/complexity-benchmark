import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    nA = int(data[idx]); idx += 1
    nB = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    
    edges = []
    degA = [0] * (nA + 1)
    degB = [0] * (nB + 1)
    
    for i in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        edges.append((u, v))
        degA[u] += 1
        degB[v] += 1
    
    D = 0
    for i in range(1, nA + 1):
        if degA[i] > D:
            D = degA[i]
    for i in range(1, nB + 1):
        if degB[i] > D:
            D = degB[i]
    
    color = [0] * m
    usedA = bytearray(nA + 1)
    usedB = bytearray(nB + 1)
    remaining = list(range(m))
    
    c = 1
    while remaining and c <= D:
        usedA = bytearray(nA + 1)
        usedB = bytearray(nB + 1)
        new_remaining = []
        for ei in remaining:
            u, v = edges[ei]
            if not usedA[u] and not usedB[v]:
                color[ei] = c
                usedA[u] = 1
                usedB[v] = 1
            else:
                new_remaining.append(ei)
        remaining = new_remaining
        c += 1
    
    out = ['YES']
    out.append(' '.join(map(str, color)))
    sys.stdout.write('\n'.join(out) + '\n')

main()