import sys


def validate(input_text: str, output_text: str):
    sys.setrecursionlimit(10000)
    data = input_text.split()
    idx = 0
    k = int(data[idx]); idx += 1
    t = int(data[idx]); idx += 1

    allowed = set()
    by_x = [[] for _ in range(k + 1)]
    for _ in range(t):
        x = int(data[idx]); y = int(data[idx + 1]); z = int(data[idx + 2]); idx += 3
        allowed.add((x, y, z))
        by_x[x].append((y, z))

    # Re-derive ground truth: does a perfect selection exist? (backtracking)
    used_y = [False] * (k + 1)
    used_z = [False] * (k + 1)

    def solve(x):
        if x > k:
            return True
        for (y, z) in by_x[x]:
            if not used_y[y] and not used_z[z]:
                used_y[y] = used_z[z] = True
                if solve(x + 1):
                    used_y[y] = used_z[z] = False
                    return True
                used_y[y] = used_z[z] = False
        return False

    feasible = solve(1)

    toks = output_text.split()
    if not toks:
        return False, "empty output"

    head = toks[0].upper()
    if head == "NO":
        if feasible:
            return False, "reported NO but a valid selection of crews exists"
        return True, "correctly reported no selection"

    if head != "YES":
        return False, f"first token must be YES or NO, got {toks[0]!r}"

    if not feasible:
        return False, "reported YES but no valid selection exists"

    nums = toks[1:]
    if len(nums) != 3 * k:
        return False, f"expected {k} crews (3*k values after YES), got {len(nums)} values"

    try:
        vals = [int(v) for v in nums]
    except ValueError:
        return False, "non-integer value in crews"

    cov_x, cov_y, cov_z = set(), set(), set()
    for i in range(k):
        x, y, z = vals[3 * i], vals[3 * i + 1], vals[3 * i + 2]
        if (x, y, z) not in allowed:
            return False, f"crew ({x} {y} {z}) is not an allowed combination"
        if x in cov_x or y in cov_y or z in cov_z:
            return False, "a specialist, machine, or slot is used more than once"
        cov_x.add(x); cov_y.add(y); cov_z.add(z)

    full = set(range(1, k + 1))
    if cov_x != full or cov_y != full or cov_z != full:
        return False, "not every specialist, machine, and slot is covered exactly once"

    return True, "valid selection of k crews"
