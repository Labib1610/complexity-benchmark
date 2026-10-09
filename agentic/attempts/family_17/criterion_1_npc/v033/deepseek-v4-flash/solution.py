import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    q = int(input_data[0])
    t = int(input_data[1])
    triples = []
    idx = 2
    for _ in range(t):
        a = int(input_data[idx])
        b = int(input_data[idx+1])
        c = int(input_data[idx+2])
        idx += 3
        mask = (1 << (a-1)) | (1 << (b-1)) | (1 << (c-1))
        triples.append((mask, (a, b, c)))
    
    full_mask = (1 << (3*q)) - 1
    
    # Group triples by their smallest element for fast lookup
    by_min = [[] for _ in range(3*q)]
    for mask, triple in triples:
        # find smallest set bit
        min_bit = (mask & -mask).bit_length() - 1
        by_min[min_bit].append((mask, triple))
    
    chosen = []
    
    def dfs(covered):
        if covered == full_mask:
            return True
        # find first uncovered element
        # smallest uncovered index
        uncovered = (~covered) & full_mask
        # get lowest set bit
        lsb = uncovered & -uncovered
        idx_bit = lsb.bit_length() - 1
        for mask, triple in by_min[idx_bit]:
            if covered & mask == 0:
                chosen.append(triple)
                if dfs(covered | mask):
                    return True
                chosen.pop()
        return False
    
    if dfs(0):
        print("YES")
        for a, b, c in chosen:
            print(a, b, c)
    else:
        print("NO")

if __name__ == "__main__":
    solve()