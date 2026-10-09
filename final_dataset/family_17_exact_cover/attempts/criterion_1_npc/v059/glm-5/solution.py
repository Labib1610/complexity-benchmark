import sys, random, time

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    q = int(input_data[idx]); idx+=1
    t = int(input_data[idx]); idx+=1
    n = 3*q
    triples = []
    seen = set()
    for _ in range(t):
        a = int(input_data[idx]); b = int(input_data[idx+1]); c = int(input_data[idx+2])
        idx += 3
        key = (a,b,c)
        if key not in seen:
            seen.add(key)
            triples.append((a-1,b-1,c-1))
    t = len(triples)
    
    # element -> triple list
    elem_triples = [[] for _ in range(n)]
    for i,(a,b,c) in enumerate(triples):
        elem_triples[a].append(i)
        elem_triples[b].append(i)
        elem_triples[c].append(i)
    
    # check coverage
    for e in range(n):
        if not elem_triples[e]:
            print("NO"); return
    if t < q:
        print("NO"); return