import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    models = []
    for _ in range(t):
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))
        models.append((a, b, c))
    
    # If not enough models, impossible
    if t < k:
        print("NO")
        return

    # Sort models to help pruning
    models.sort()
    
    used_alpha = set()
    used_beta = set()
    used_gamma = set()
    chosen = []
    
    def dfs(start):
        if len(chosen) == k:
            return True
        for i in range(start, t):
            a, b, c = models[i]
            if a in used_alpha or b in used_beta or c in used_gamma:
                continue
            # choose
            used_alpha.add(a)
            used_beta.add(b)
            used_gamma.add(c)
            chosen.append((a, b, c))
            if dfs(i + 1):
                return True
            # backtrack
            chosen.pop()
            used_alpha.remove(a)
            used_beta.remove(b)
            used_gamma.remove(c)
        return False
    
    if dfs(0):
        print("YES")
        for a, b, c in chosen:
            print(a, b, c)
    else:
        print("NO")

if __name__ == "__main__":
    solve()