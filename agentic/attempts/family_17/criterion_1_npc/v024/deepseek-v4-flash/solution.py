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
        triples.append((a-1, b-1, c-1))  # 0-based
    
    n = 3 * q
    # Group triples by first element for quick lookup
    by_first = [[] for _ in range(n)]
    for triple in triples:
        a, b, c = triple
        by_first[a].append(triple)
    
    used = [False] * n
    result = []
    
    def backtrack():
        # Find first unused server
        try:
            first = used.index(False)
        except ValueError:
            return True  # all used
        
        # Try all triples starting with this server
        for a, b, c in by_first[first]:
            if not used[a] and not used[b] and not used[c]:
                used[a] = used[b] = used[c] = True
                result.append((a+1, b+1, c+1))
                if backtrack():
                    return True
                result.pop()
                used[a] = used[b] = used[c] = False
        return False
    
    if backtrack():
        print("YES")
        for triple in result:
            print(*triple)
    else:
        print("NO")

if __name__ == "__main__":
    solve()