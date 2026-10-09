import sys

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    n, m = int(input_data[0]), int(input_data[1])
    conflicts = [[] for _ in range(n)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx]) - 1
        v = int(input_data[idx + 1]) - 1
        idx += 2
        conflicts[u].append(v)
        conflicts[v].append(u)

    color = [0] * n

    def is_safe(worker, c):
        for neighbor in conflicts[worker]:
            if color[neighbor] == c:
                return False
        return True

    def backtrack(worker):
        if worker == n:
            return True
        for c in range(1, 4):
            if is_safe(worker, c):
                color[worker] = c
                if backtrack(worker + 1):
                    return True
                color[worker] = 0
        return False

    if backtrack(0):
        print("YES")
        print(" ".join(map(str, color)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()