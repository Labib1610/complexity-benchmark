import sys

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    
    N = 2 * n
    # adjacency using arrays
    # Build edge lists
    # For clause (l1, l2): edge neg(l1) -> l2, neg(l2) -> l1
    # node for literal v: if v>0: 2*(v-1); if v<0: 2*(-v-1)+1
    # negation: flip last bit.
    
    # Build adjacency with head/next arrays (forward star) for efficiency
    ...