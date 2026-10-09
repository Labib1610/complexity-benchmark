import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    mask = [0] * (n + 1)
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        mask[u] |= 1 << v
        mask[v] |= 1 << u
        
    for a in range(1, n + 1):
        m_a = mask[a]
        for b in range(a + 1, n + 1):
            if (m_a >> b) & 1:
                common = (m_a & mask[b]) >> (b + 1)
                if common:
                    c = (common & -common).bit_length() + b
                    print(f"{a} {b} {c}")
                    return

if __name__ == '__main__':
    main()