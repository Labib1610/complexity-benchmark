import sys
from collections import deque

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0]); m = int(data[1])
    # build adjacency using CSR
    ...