import sys
from itertools import combinations

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    forbidden = [[False] * (n + 1) for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        forbidden[u][v] = True
        forbidden[v][u] = True
    
    # Split into two halves
    mid = n // 2
    left = list(range(1, mid + 1))
    right = list(range(mid + 1, n + 1))
    
    # Precompute which pairs in left are forbidden
    left_forbidden_pairs = set()
    for i in range(len(left)):
        for j in range(i + 1, len(left)):
            if forbidden[left[i]][left[j]]:
                left_forbidden_pairs.add((i, j))
    
    # Precompute which pairs in right are forbidden
    right_forbidden_pairs = set()
    for i in range(len(right)):
        for j in range(i + 1, len(right)):
            if forbidden[right[i]][right[j]]:
                right_forbidden_pairs.add((i, j))
    
    # Check if a subset is valid (no forbidden pairs)
    def is_valid_left(mask):
        bits = []
        for i in range(len(left)):
            if mask & (1 << i):
                bits.append(i)
        for i in range(len(bits)):
            for j in range(i + 1, len(bits)):
                if (bits[i], bits[j]) in left_forbidden_pairs:
                    return False
        return True
    
    def is_valid_right(mask):
        bits = []
        for i in range(len(right)):
            if mask & (1 << i):
                bits.append(i)
        for i in range(len(bits)):
            for j in range(i + 1, len(bits)):
                if (bits[i], bits[j]) in right_forbidden_pairs:
                    return False
        return True
    
    # Generate all valid subsets for left half
    left_valid = []
    for mask in range(1 << len(left)):
        if is_valid_left(mask):
            cnt = bin(mask).count('1')
            left_valid.append((cnt, mask))
    
    # Group by count
    left_by_count = {}
    for cnt, mask in left_valid:
        if cnt not in left_by_count:
            left_by_count[cnt] = []
        left_by_count[cnt].append(mask)
    
    # For each valid left subset, find compatible right subset
    for lcnt, lmask in left_valid:
        rcnt = k - lcnt
        if rcnt < 0 or rcnt > len(right):
            continue
        
        # Check all valid right subsets with count rcnt
        for rmask in range(1 << len(right)):
            if bin(rmask).count('1') != rcnt:
                continue
            if not is_valid_right(rmask):
                continue
            
            # Check cross-edges
            left_indices = [i for i in range(len(left)) if lmask & (1 << i)]
            right_indices = [i for i in range(len(right)) if rmask & (1 << i)]
            
            valid = True
            for li in left_indices:
                for ri in right_indices:
                    if forbidden[left[li]][right[ri]]:
                        valid = False
                        break
                if not valid:
                    break
            
            if valid:
                # Found solution
                result = []
                for i in left_indices:
                    result.append(left[i])
                for i in right_indices:
                    result.append(right[i])
                print("YES")
                print(' '.join(map(str, sorted(result))))
                return
    
    print("NO")

if __name__ == "__main__":
    solve()