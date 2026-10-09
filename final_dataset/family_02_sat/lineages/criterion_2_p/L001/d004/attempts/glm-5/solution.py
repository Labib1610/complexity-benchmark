import sys

def main():
    input_data = sys.stdin.buffer.read().split()
    n = int(input_data[0])
    m = int(input_data[1])
    
    # nodes: 2n total. node 2*(i-1) = x_i true, 2*(i-1)+1 = x_i false
    N = 2 * n
    # adjacency using arrays (CSR format) for speed
    # First collect edges
    # For each clause with literal nodes a, b: edges (a^1, b) and (b^1, a)
    
    # Build edge lists
    num_edges = 2 * m
    eu = [0] * num_edges
    ev = [0] * num_edges
    idx = 0
    ptr = 2
    for _ in range(m):
        l1 = int(input_data[ptr]); l2 = int(input_data[ptr+1]); ptr += 2
        if l1 > 0:
            a = 2 * (l1 - 1)
        else:
            a = 2 * (-l1 - 1) + 1
        if l2 > 0:
            b = 2 * (l2 - 1)
        else:
            b = 2 * (-l2 - 1) + 1
        eu[idx] = a ^ 1; ev[idx] = b
        idx += 1
        eu[idx] = b ^ 1; ev[idx] = a
        idx += 1
    
    # Build CSR
    ...