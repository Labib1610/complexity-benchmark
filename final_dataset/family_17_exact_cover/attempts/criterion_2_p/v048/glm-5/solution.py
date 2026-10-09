import sys
from collections import deque

def main():
    data = sys.stdin.buffer.read().split()
    q = int(data[0]); t = int(data[1])
    # build CSR
    # edges: a in 1..q, b in q+1..2q -> right index b-q-1 in 0..q-1
    ...