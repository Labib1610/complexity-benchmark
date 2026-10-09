import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    
    # node for literal: machine i (1-indexed): true node = 2*i, false node = 2*i+1
    # feed c: c>0 -> literal "machine c is mode 0" = false node of c = 2*c+1
    #         c<0 -> literal "machine |c| is mode 1" = true node = 2*|c|
    # clause: (not L1) or (not L2): edges L1 -> not L2, L2 -> not L1
    
    # Build CSR
    # count edges
    us = []
    vs = []
    for _ in range(m):
        c1 = int(data[idx]); idx += 1
        c2 = int(data[idx]); idx += 1
        if c1 > 0:
            l1 = 2*c1 + 1
        else:
            l1 = 2*(-c1)
        if c2 > 0:
            l2 = 2*c2 + 1
        else:
            l2 = 2*(-c2)
        # edge l1 -> not l2, l2 -> not l1
        # not of node v: v^1 (since true=2i, false=2i+1, XOR 1 flips)
        us.append(l1); vs.append(l2 ^ 1)
        us.append(l2); vs.append(l1 ^ 1)
    
    N = 2*n + 2  # nodes 0..2n+1, but node 0 unused (machine 0 doesn't exist). Actually machines are 1..n, so nodes 2..2n+1. Let's just use size 2n+2.