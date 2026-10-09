import sys
from collections import deque

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    q = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    # adjacency using arrays
    # Read edges
    ...