import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        adj[u].append(v)
        adj[v].append(u)
    
    # Sort neighbors for each vertex
    for i in range(1, n + 1):
        adj[i].sort()
    
    # Build bitsets for neighbors > vertex
    bits = [0] * (n + 1)
    for i in range(1, n + 1):
        b = 0
        for nb in adj[i]:
            if nb > i:
                b |= (1 << nb)
        bits[i] = b
    
    for a in range(1, n + 1):
        a_bits = bits[a]
        if a_bits == 0:
            continue
        for b in adj[a]:
            if b < a:
                continue
            # c must be > b and neighbor of both a and b
            mask = a_bits & bits[b]
            # Clear bits <= b
            mask &= ~((1 << (b + 1)) - 1)
            if mask:
                c = (mask & -mask).bit_length() - 1
                print(f"{a} {b} {c}")
                return
    
    # Should not reach here per problem guarantee
    print("-1 -1 -1")

main()