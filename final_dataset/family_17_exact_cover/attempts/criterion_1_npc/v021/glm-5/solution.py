import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    q = int(data[idx]); idx+=1
    t = int(data[idx]); idx+=1
    n = 3*q
    triples = []
    for _ in range(t):
        a = int(data[idx]); b = int(data[idx+1]); c = int(data[idx+2]); idx+=3
        triples.append((a,b,c))
    # dedupe? Input says a<b<c, could have duplicates? Possibly. Dedupe to be safe.
    ...