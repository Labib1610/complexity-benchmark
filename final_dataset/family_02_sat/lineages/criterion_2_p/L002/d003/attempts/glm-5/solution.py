import sys

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx+=1
    m = int(input_data[idx]); idx+=1
    
    # nodes: 2*i = x_i true, 2*i+1 = x_i false
    # literal c: if c>0: node 2*(c-1); if c<0: node 2*(-c-1)+1
    # clause (a or b): edges: not_a -> b, not_b -> a
    # negation of node v: v^1
    
    N = 2*n
    # adjacency using arrays
    head = [-1]*(N)  # or build lists
    # Let's build adjacency lists as list of lists first, or use CSR for speed.