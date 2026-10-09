import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx+=1
    m = int(data[idx]); idx+=1
    B = int(data[idx]); idx+=1
    edges = []
    for _ in range(m):
        u = int(data[idx]); idx+=1
        v = int(data[idx]); idx+=1
        edges.append((u-1, v-1))