import sys

# Increase recursion depth just in case
sys.setrecursionlimit(10000)

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    q = int(input_data[0])
    t = int(input_data[1])

    triples_by_a = [[] for _ in range(3 * q + 1)]
    
    idx = 2
    for _ in range(t):
        a = int(input_data[idx])
        b = int(input_data[idx+1])
        c = int(input_data[idx+2])
        idx += 3
        triples_by_a[a].append((b, c))

    used = [False] * (3 * q + 1)
    chosen = []

    def solve(cur_min):
        while cur_min <= 3 * q and used[cur_min]:
            cur_min += 1
        
        if cur_min > 3 * q:
            return True

        for b, c in triples_by_a[cur_min]:
            if not used[b] and not used[c]:
                used[cur_min] = used[b] = used[c] = True
                chosen.append((cur_min, b, c))
                
                if solve(cur_min + 1):
                    return True
                
                chosen.pop()
                used[cur_min] = used[b] = used[c] = False

        return False

    if solve(1):
        print("YES")
        out = []
        for a, b, c in chosen:
            out.append(f"{a} {b} {c}")
        print("\n".join(out))
    else:
        print("NO")

if __name__ == '__main__':
    main()