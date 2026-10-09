import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    k = int(input_data[0])
    t = int(input_data[1])
    relays = []
    idx = 2
    for _ in range(t):
        x = int(input_data[idx])
        y = int(input_data[idx+1])
        z = int(input_data[idx+2])
        idx += 3
        relays.append((x-1, y-1, z-1))  # 0-based

    # Group relays by x for faster lookup
    by_x = [[] for _ in range(k)]
    for r in relays:
        by_x[r[0]].append(r)

    # Backtracking
    used_y = 0
    used_z = 0
    chosen = []

    def dfs(i, used_y, used_z):
        if i == k:
            return True
        for (x, y, z) in by_x[i]:
            if not (used_y & (1 << y)) and not (used_z & (1 << z)):
                chosen.append((x+1, y+1, z+1))
                if dfs(i+1, used_y | (1 << y), used_z | (1 << z)):
                    return True
                chosen.pop()
        return False

    if dfs(0, 0, 0):
        print("YES")
        for r in chosen:
            print(*r)
    else:
        print("NO")

if __name__ == "__main__":
    solve()