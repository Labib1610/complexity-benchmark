import sys

def solve():
    input_data = sys.stdin.buffer.read().split()
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [0] * (n + 1)
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
    
    full_mask = (1 << (n + 1)) - 1
    
    for a in range(1, n + 1):
        # neighbors of a with index > a
        set_b = adj[a] & (full_mask ^ ((1 << (a + 1)) - 1))
        while set_b:
            # get lowest set bit
            lsb = set_b & -set_b
            b = lsb.bit_length() - 1
            # common neighbors > b
            set_c = adj[a] & adj[b] & (full_mask ^ ((1 << (b + 1)) - 1))
            if set_c:
                lsb_c = set_c & -set_c
                c = lsb_c.bit_length() - 1
                print(a, b, c)
                return
            set_b ^= lsb
    
if __name__ == "__main__":
    solve()