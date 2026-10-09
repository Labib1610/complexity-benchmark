import sys

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    m = int(data[1])
    
    adj_mask = [0] * (n + 1)
    adj_list = [[] for _ in range(n + 1)]
    
    idx = 2
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        adj_mask[u] |= (1 << v)
        adj_mask[v] |= (1 << u)
        if u < v:
            adj_list[u].append(v)
        else:
            adj_list[v].append(u)
            
    for u in range(1, n + 1):
        adj_list[u].sort()
        
    for a in range(1, n + 1):
        mask_a = adj_mask[a]
        for b in adj_list[a]:
            common = mask_a & adj_mask[b]
            # Keep only vertices c > b
            common &= ~((1 << (b + 1)) - 1)
            if common:
                lsb = common & -common
                c = lsb.bit_length() - 1
                print(f"{a} {b} {c}")
                return

if __name__ == '__main__':
    main()