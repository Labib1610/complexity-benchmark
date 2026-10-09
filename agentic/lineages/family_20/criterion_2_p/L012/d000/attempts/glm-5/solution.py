chain_edges = []
cur = v
c = a
while True:
    e = used[cur].get(c)
    if e is None: break
    chain_edges.append(e)
    cur = endpoints[e] other side
    c = b if c == a else a