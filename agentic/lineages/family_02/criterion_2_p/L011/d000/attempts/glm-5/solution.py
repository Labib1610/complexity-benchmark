import sys

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    
    N = 2 * n
    # adjacency using CSR
    # First pass: count out-degrees
    # literals: for clause (a, b): edges neg(a)->b, neg(b)->a
    
    def lit_node(l):
        if l > 0:
            return 2 * (l - 1)
        else:
            return 2 * (-l - 1) + 1
    
    edges_from = [0] * (2 * m)
    edges_to = [0] * (2 * m)
    
    for e in range(m):
        a = int(input_data[idx]); idx += 1
        b = int(input_data[idx]); idx += 1
        na = lit_node(a) ^ 1
        nb = lit_node(b) ^ 1
        an = lit_node(a)
        bn = lit_node(b)
        edges_from[2*e] = na
        edges_to[2*e] = bn
        edges_from[2*e+1] = nb
        edges_to[2*e+1] = an
    
    # Build CSR
    deg = [0] * (N + 1)
    for v in edges_from:
        deg[v+1] += 1  # hmm, let me do prefix sums
    ...