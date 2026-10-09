import sys, time, random

def main():
    start = time.time()
    data = sys.stdin.buffer.read().split()
    idx = 0
    q = int(data[idx]); idx+=1
    t = int(data[idx]); idx+=1
    n = 3*q
    triples = []
    seen = set()
    for _ in range(t):
        a = int(data[idx])-1; b = int(data[idx+1])-1; c = int(data[idx+2])-1; idx+=3
        key = (a,b,c)  # already sorted a<b<c
        if key in seen: continue
        seen.add(key)
        triples.append(key)
    # union-find
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for (a,b,c) in triples:
        ra, rb, rc = find(a), find(b), find(c)
        if ra != rb: parent[ra] = rb
        rb2 = find(b)
        rc = find(c)
        if rb2 != rc: parent[rb2] = rc
    # group elements by root
    from collections import defaultdict
    comp_elems = defaultdict(list)
    for e in range(n):
        comp_elems[find(e)].append(e)
    # check divisibility
    for root, els in comp_elems.items():
        if len(els) % 3 != 0:
            print("NO"); return
    # triples per component
    comp_triples = defaultdict(list)
    for (a,b,c) in triples:
        comp_triples[find(a)].append((a,b,c))
    ...