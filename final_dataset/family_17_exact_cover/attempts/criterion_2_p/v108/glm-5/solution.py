import sys

def main():
    data = sys.stdin.buffer.read().split()
    q = int(data[0]); t = int(data[1])
    # parse edges
    # adjacency: for left vertices 0..q-1 (surface a-1), right vertices 0..q-1 (orbital b-q-1)