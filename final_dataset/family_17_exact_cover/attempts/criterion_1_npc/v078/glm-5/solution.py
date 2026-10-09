import sys
from sys import setrecursionlimit

def main():
    input_data = sys.stdin.buffer.read().split()
    q = int(input_data[0]); t = int(input_data[1])
    n = 3 * q
    triples = []
    seen = set()
    idx = 2
    for _ in range(t):
        a = int(input_data[idx]); b = int(input_data[idx+1]); c = int(input_data[idx+2])
        idx += 3
        # convert to 0-based
        key = (a-1, b-1, c-1)
        if key not in seen:
            seen.add(key)
            triples.append(key)
    ...