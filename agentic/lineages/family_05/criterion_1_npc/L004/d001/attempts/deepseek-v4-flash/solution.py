import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    k = int(next(it))
    t = int(next(it))
    
    options = [[] for _ in range(k+1)]
    for _ in range(t):
        p1 = int(next(it))
        p2 = int(next(it))
        p3 = int(next(it))
        options[p1].append((p2, p3))
    
    # If any p1 has no options, impossible
    for i in range(1, k+1):
        if not options[i]:
            print("NO")
            return
    
    chosen = []
    
    def dfs(i, used2, used3):
        if i == k+1:
            return True
        for p2, p3 in options[i]:
            if not (used2 & (1 << (p2-1))) and not (used3 & (1 << (p3-1))):
                chosen.append((i, p2, p3))
                if dfs(i+1, used2 | (1 << (p2-1)), used3 | (1 << (p3-1))):
                    return True
                chosen.pop()
        return False
    
    if dfs(1, 0, 0):
        print("YES")
        for p1, p2, p3 in chosen:
            print(p1, p2, p3)
    else:
        print("NO")

if __name__ == "__main__":
    solve()