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
        a = int(input_data[idx]) - 1
        b = int(input_data[idx+1]) - 1
        c = int(input_data[idx+2]) - 1
        idx += 3
        mask = (1 << a) | (1 << b) | (1 << c)
        triples.append((mask, a, b, c))
    
    full_mask = (1 << (3*q)) - 1
    
    # Sort triples: prefer those with smallest first uncovered element
    # We'll sort by the smallest bit index in the mask
    triples.sort(key=lambda x: (x[0] & -x[0]).bit_length() - 1)
    
    chosen = []
    
    def backtrack(covered, start):
        if covered == full_mask:
            return True
        # Find first uncovered anomaly
        # We can find the lowest zero bit
        inv = (~covered) & full_mask
        if inv == 0:
            return False
        # lowest uncovered bit
        low_bit = inv & -inv
        low_idx = low_bit.bit_length() - 1
        
        # Try triples that contain this bit
        for i in range(start, t):
            mask, a, b, c = triples[i]
            if (mask & low_bit) == 0:
                continue
            if (mask & covered) != 0:
                continue
            chosen.append((a+1, b+1, c+1))
            if backtrack(covered | mask, i+1):
                return True
            chosen.pop()
        return False
    
    if backtrack(0, 0):
        print("YES")
        for a,b,c in chosen:
            print(a,b,c)
    else:
        print("NO")

if __name__ == "__main__":
    solve()