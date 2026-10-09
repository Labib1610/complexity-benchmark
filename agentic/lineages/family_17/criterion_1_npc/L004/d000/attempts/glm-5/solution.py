import sys, random

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    q = int(input_data[idx]); idx+=1
    t = int(input_data[idx]); idx+=1
    n = 3*q
    triples = []
    seen = set()
    for _ in range(t):
        a = int(input_data[idx])-1; b = int(input_data[idx+1])-1; c = int(input_data[idx+2])-1
        idx += 3
        key = (a,b,c)
        if key not in seen and a>=0... # a<b<c guaranteed
        seen.add(key)
        triples.append((a,b,c))
    t = len(triples)
    
    # triples_of
    triples_of = [[] for _ in range(n)]
    for j,(a,b,c) in enumerate(triples):
        triples_of[a].append(j)
        triples_of[b].append(j)
        triples_of[c].append(j)
    
    # initial cnt
    cnt = [len(triples_of[e]) for e in range(n)]
    maxdeg = max(cnt) if n else 0
    buckets = [set() for _ in range(maxdeg+2)]
    for e in range(n):
        buckets[cnt[e]].add(e)
    deadcnt = [0]*t
    covered = [False]*n
    chosen = []
    
    # quick check: any element with cnt 0 -> NO
    if n>0 and (maxdeg==0 or not any(...)) hmm just check min.