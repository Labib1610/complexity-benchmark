import sys

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0]); m = int(data[1])
    # literal to node: positive x -> 2*(x-1), negative -x -> 2*(x-1)+1
    N = 2 * n
    # Build adjacency using arrays (CSR) for speed
    # edges: for clause (a, b): add ¬a -> b, ¬b -> a
    # negation of literal node: node ^ 1
    # literal value to node:
    def lit_node(v):
        if v > 0:
            return 2 * (v - 1)
        else:
            return 2 * (-v - 1) + 1
    
    head = [0] * (N + 1)
    us = [0] * (2 * m)
    vs = [0] * (2 * m)
    idx = 0
    pos = 2
    for i in range(m):
        a = int(data[pos]); b = int(data[pos+1]); pos += 2
        na = lit_node(a); nb = lit_node(b)
        # ¬a -> b : edge from na^1 to nb
        us[idx] = na ^ 1; vs[idx] = nb; idx += 1
        us[idx] = nb ^ 1; vs[idx] = na; idx += 1
    # CSR
    for i in range(2*m):
        head[us[i]] += 1
    # prefix sums
    for i in range(N):
        head[i+1] += head[i]
    # hmm, standard CSR construction