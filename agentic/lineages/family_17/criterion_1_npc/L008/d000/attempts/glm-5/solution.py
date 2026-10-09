def solve():
    import sys
    input_data = sys.stdin.buffer.read().split()
    q = int(input_data[0]); t = int(input_data[1])
    N = 3*q
    INF = 1 << 30
    # read triples
    triples = []
    seen = set()
    idx = 2
    for _ in range(t):
        a = int(input_data[idx]) - 1; b = int(input_data[idx+1]) - 1; c = int(input_data[idx+2]) - 1
        idx += 3
        key = (a,b,c)
        if key not in seen:
            seen.add(key)
            triples.append(key)
    # build triples_of
    triples_of = [[] for _ in range(N)]
    for ti, (a,b,c) in enumerate(triples):
        triples_of[a].append(ti)
        triples_of[b].append(ti)
        triples_of[c].append(ti)
    # initial counts
    cnt = [len(triples_of[e]) for e in range(N)]
    if N == 0: ... # q>=1 so N>=3
    if min(cnt) == 0:
        print("NO"); return
    ...