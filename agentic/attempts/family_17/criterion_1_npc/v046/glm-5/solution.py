import sys
from sys import setrecursionlimit

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    q = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    n = 3 * q
    triples = []
    seen = set()
    for _ in range(t):
        a = int(input_data[idx]) - 1; b = int(input_data[idx+1]) - 1; c = int(input_data[idx+2]) - 1
        idx += 3
        key = (a, b, c)
        if key not in seen:
            seen.add(key)
            triples.append(key)
    ...