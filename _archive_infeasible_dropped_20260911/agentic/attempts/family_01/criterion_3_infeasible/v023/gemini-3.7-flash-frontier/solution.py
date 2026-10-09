import sys

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    
    mask = [0] * (n + 1)
    
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        mask[u] |= (1 << v)
        mask[v] |= (1 << u)
        
    for a in range(1, n + 1):
        m_a = mask[a]
        # Iterate over neighbors b of a such that b > a
        # To iterate over neighbors efficiently:
        temp = m_a >> (a + 1)
        b = a + 1
        while temp > 0:
            # find next set bit
            lsb = temp & -temp
            b_cand = a + 1 + (lsb.bit_length() - 1)
            
            # common neighbors of a and b that are > b_cand
            common = m_a & mask[b_cand]
            common >>= (b_cand + 1)
            if common > 0:
                c_lsb = common & -common
                c = b_cand + 1 + (c_lsb.bit_length() - 1)
                print(f"{a} {b_cand} {c}")
                return
            
            temp ^= lsb

if __name__ == '__main__':
    main()