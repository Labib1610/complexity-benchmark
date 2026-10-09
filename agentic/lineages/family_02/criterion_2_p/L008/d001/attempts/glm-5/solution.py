import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    
    N = 2 * n  # nodes: 2*(i-1) = relay i mode 1, 2*(i-1)+1 = relay i mode 0
    
    # Edges: for clause (a, b): (¬a → b), (¬b → a)
    # We'll build CSR directly.
    
    # First, compute out-degrees.
    # edge count = 2*m
    
    # Let's collect edges as arrays.
    esrc = [0] * (2 * m)
    edst = [0] * (2 * m)
    
    def lit(v):
        # v is signed nonzero integer
        if v > 0:
            return 2 * (v - 1)
        else:
            return 2 * (-v - 1) + 1
    
    for e in range(m):
        a = int(data[idx]); idx += 1
        b = int(data[idx]); idx += 1
        la = lit(a); lb = lit(b)
        # ¬la → lb
        esrc[2*e] = la ^ 1
        edst[2*e] = lb
        # ¬lb → la
        esrc[2*e+1] = lb ^ 1
        edst[2*e+1] = la
    
    # Build CSR for G and G^T.
    ...