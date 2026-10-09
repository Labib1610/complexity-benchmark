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
        triples.append((a, b, c))
    
    total = 3 * q
    full_mask = (1 << (total + 1)) - 1  # bits 1..total
    
    # Group triples by their smallest element
    by_min = [[] for _ in range(total + 1)]
    for i, (a, b, c) in enumerate(triples):
        by_min[a].append(i)
    
    # Sort each list by size of triple (not needed, but keep)
    # We'll use recursion with bitmask
    used = 0
    chosen = []
    
    # Precompute bitmask for each triple
    triple_mask = []
    for a, b, c in triples:
        triple_mask.append((1 << a) | (1 << b) | (1 << c))
    
    # Find smallest unused number
    def find_first_unused(mask):
        # bits 1..total
        for i in range(1, total + 1):
            if not (mask >> i) & 1:
                return i
        return -1
    
    def dfs(mask, depth):
        if depth == q:
            return True
        first = find_first_unused(mask)
        if first == -1:
            return False
        for idx in by_min[first]:
            if mask & triple_mask[idx] == 0:
                chosen.append(triples[idx])
                if dfs(mask | triple_mask[idx], depth + 1):
                    return True
                chosen.pop()
        return False
    
    if dfs(0, 0):
        print("YES")
        for a, b, c in chosen:
            print(a, b, c)
    else:
        print("NO")

if __name__ == "__main__":
    solve()