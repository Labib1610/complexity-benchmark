import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj_bit = [0] * (n + 1)
    adj_list = [[] for _ in range(n + 1)]
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        
        adj_bit[u] |= 1 << v
        adj_bit[v] |= 1 << u
        if u < v:
            adj_list[u].append(v)
        else:
            adj_list[v].append(u)
            
    for a in range(1, n + 1):
        adj_list[a].sort()
        bit_a = adj_bit[a]
        for b in adj_list[a]:
            shift = b + 1
            common = (bit_a & adj_bit[b]) >> shift
            if common:
                c = shift + (common & -common).bit_length() - 1
                print(f"{a} {b} {c}")
                return

if __name__ == '__main__':
    main()