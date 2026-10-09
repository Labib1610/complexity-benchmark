import sys

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0]); m = int(data[1])
    idx = 2
    clauses_raw = []
    for _ in range(m):
        lits = [int(data[idx]), int(data[idx+1]), int(data[idx+2])]
        idx += 3
        clauses_raw.append(lits)
    ...