import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    q = int(input_data[0])
    t = int(input_data[1])
    scripts = []
    idx = 2
    for _ in range(t):
        a = int(input_data[idx])
        b = int(input_data[idx+1])
        c = int(input_data[idx+2])
        idx += 3
        scripts.append((a, b, c))
    
    # Sort by first element, then second, then third
    scripts.sort()
    
    used = [False] * (3*q + 1)
    chosen = []
    
    for a, b, c in scripts:
        if len(chosen) == q:
            break
        if not used[a] and not used[b] and not used[c]:
            used[a] = used[b] = used[c] = True
            chosen.append((a, b, c))
    
    if len(chosen) == q:
        print("YES")
        for a, b, c in chosen:
            print(a, b, c)
    else:
        print("NO")

if __name__ == "__main__":
    solve()