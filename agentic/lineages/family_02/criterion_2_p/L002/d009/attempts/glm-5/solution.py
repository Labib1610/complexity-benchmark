import sys

def main():
    input_data = sys.stdin.buffer.read().split()
    n = int(input_data[0]); m = int(input_data[1])
    N = 2 * n
    # adjacency using arrays
    # edges: for each clause (a, b): (a^1) -> b, (b^1) -> a
    ...