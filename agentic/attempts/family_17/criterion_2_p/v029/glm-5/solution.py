import sys

def main():
    data = sys.stdin.buffer.read().split()
    q = int(data[0]); t = int(data[1])
    n = q  # left size, right size
    # edges: a in 1..q, b in q+1..2q
    # left index: a-1, right index: b-q-1
    # Build CSR
    # Count degrees
    deg = [0]*(n)
    idx = 2
    # First pass: count
    es = []
    for i in range(t):
        a = int(data[idx]); b = int(data[idx+1]); idx += 2
        ...