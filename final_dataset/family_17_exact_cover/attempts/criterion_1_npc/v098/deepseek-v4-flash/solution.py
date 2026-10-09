import sys

def solve():
    input = sys.stdin.readline
    q, t = map(int, input().split())
    triples = []
    for _ in range(t):
        a, b, c = map(int, input().split())
        triples.append((a, b, c))
    
    used = [False] * (3 * q + 1)
    chosen = []
    
    # Sort triples by first element to help pruning
    triples.sort()
    
    def dfs(count):
        if count == q:
            return True
        # Find first unused material
        start = 1
        while start <= 3 * q and used[start]:
            start += 1
        if start > 3 * q:
            return False
        
        for a, b, c in triples:
            if a == start and not used[b] and not used[c]:
                used[a] = used[b] = used[c] = True
                chosen.append((a, b, c))
                if dfs(count + 1):
                    return True
                chosen.pop()
                used[a] = used[b] = used[c] = False
        return False
    
    if dfs(0):
        print("YES")
        for a, b, c in chosen:
            print(a, b, c)
    else:
        print("NO")

if __name__ == "__main__":
    solve()