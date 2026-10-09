import sys, time, random

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    q = int(input_data[idx]); idx+=1
    t = int(input_data[idx]); idx+=1
    n = 3*q
    edge_set = set()
    for _ in range(t):
        a = int(input_data[idx]); b = int(input_data[idx+1]); c = int(input_data[idx+2]); idx+=3
        edge_set.add((a,b,c))
    edges = list(edge_set)
    
    # degree check
    deg0 = [0]*(n+1)
    for (a,b,c) in edges:
        deg0[a]+=1; deg0[b]+=1; deg0[c]+=1
    if any(deg0[v]==0 for v in range(1,n+1)):
        print("NO"); return
    
    # DSU components
    parent = list(range(n+1))
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]
            x=parent[x]
        return x
    for (a,b,c) in edges:
        ra,rb,rc = find(a),find(b),find(c)
        if ra!=rb: parent[ra]=rb
        rb2=find(b); rc=find(c)
        if rb2!=rc: parent[rc]=rb2
    comp_of = {}
    comps = {}
    for v in range(1,n+1):
        r = find(v)
        comps.setdefault(r, []).append(v)
    
    # check sizes divisible by 3
    comp_list = sorted(comps.values(), key=len)
    for cl in comp_list:
        if len(cl) % 3 != 0:
            print("NO"); return
    
    # solve each component
    ...