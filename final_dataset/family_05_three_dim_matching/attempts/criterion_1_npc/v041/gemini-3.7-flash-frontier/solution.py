import sys

# Increase recursion depth just in case
sys.setrecursionlimit(2000)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    k = int(input_data[0])
    t = int(input_data[1])

    trios_by_s = [[] for _ in range(k)]
    idx = 2
    for _ in range(t):
        s = int(input_data[idx]) - 1
        c = int(input_data[idx + 1]) - 1
        f = int(input_data[idx + 2]) - 1
        idx += 3
        trios_by_s[s].append((c, f))

    for s in range(k):
        if not trios_by_s[s]:
            print("NO")
            return

    solution = [None] * k

    def backtrack(starters_left, mask_c, mask_f):
        if not starters_left:
            return True

        best_s = -1
        best_valid_pairs = None
        min_choices = 1000000

        for s in starters_left:
            valid = []
            for c, f in trios_by_s[s]:
                if not ((mask_c & (1 << c)) or (mask_f & (1 << f))):
                    valid.append((c, f))
            if len(valid) < min_choices:
                min_choices = len(valid)
                best_s = s
                best_valid_pairs = valid
                if min_choices == 0:
                    return False

        rem_starters = [s for s in starters_left if s != best_s]
        for c, f in best_valid_pairs:
            solution[best_s] = (c, f)
            if backtrack(rem_starters, mask_c | (1 << c), mask_f | (1 << f)):
                return True
            solution[best_s] = None

        return False

    starters_left = list(range(k))
    if backtrack(starters_left, 0, 0):
        print("YES")
        for s in range(k):
            c, f = solution[s]
            print(f"{s + 1} {c + 1} {f + 1}")
    else:
        print("NO")


if __name__ == "__main__":
    solve()