import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    j = int(data[0])
    lenses = []
    idx = 1
    for _ in range(j):
        d1 = int(data[idx]); d2 = int(data[idx+1])
        lenses.append((d1, d2))
        idx += 2

    lenses.sort(key=lambda x: x[0])  # sort by d1 ascending

    prefix_d1 = [0] * j
    suffix_d2 = [0] * j

    s = 0
    for i in range(j):
        s += lenses[i][0]
        prefix_d1[i] = s

    s = 0
    for i in range(j-1, -1, -1):
        s += lenses[i][1]
        suffix_d2[i] = s

    ans = 0
    for i in range(j):
        val = prefix_d1[i] + suffix_d2[i]
        if val > ans:
            ans = val

    print(ans)

if __name__ == "__main__":
    solve()