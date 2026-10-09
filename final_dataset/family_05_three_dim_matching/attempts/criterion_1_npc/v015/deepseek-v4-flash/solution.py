import sys
sys.setrecursionlimit(1 << 25)

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    k = int(next(it))
    t = int(next(it))
    
    options = [[] for _ in range(k)]
    for _ in range(t):
        x = int(next(it)) - 1
        y = int(next(it)) - 1
        z = int(next(it)) - 1
        options[x].append((y, z))
    
    # Sort nodes by degree for better backtracking
    order = sorted(range(k), key=lambda i: len(options[i]))
    
    used_img = 0
    used_shard = 0
    assignment = [None] * k
    
    # Memoization dictionary
    memo = {}
    
    def dfs(idx):
        if idx == k:
            return True
        node = order[idx]
        for y, z in options[node]:
            img_bit = 1 << y
            shard_bit = 1 << z
            if (used_img & img_bit) or (used_shard & shard_bit):
                continue
            used_img |= img_bit
            used_shard |= shard_bit
            assignment[node] = (node + 1, y + 1, z + 1)
            state = (idx + 1, used_img, used_shard)
            if state not in memo:
                memo[state] = dfs(idx + 1)
            if memo[state]:
                return True
            used_img ^= img_bit
            used_shard ^= shard_bit
        return False
    
    if dfs(0):
        print("YES")
        for ans in assignment:
            print(*ans)
    else:
        print("NO")

if __name__ == "__main__":
    solve()