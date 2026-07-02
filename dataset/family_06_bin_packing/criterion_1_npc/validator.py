import sys


def validate(input_text: str, output_text: str):
    sys.setrecursionlimit(10000)
    data = input_text.split()
    idx = 0
    n = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1
    C = int(data[idx]); idx += 1
    w = [int(data[idx + i]) for i in range(n)]; idx += n

    # Re-derive ground truth: can all items be packed into k containers?
    order = sorted(range(n), key=lambda i: -w[i])
    load = [0] * k

    def solve(pos):
        if pos == n:
            return True
        wi = w[order[pos]]
        for b in range(k):
            if load[b] + wi <= C:
                load[b] += wi
                if solve(pos + 1):
                    load[b] -= wi
                    return True
                load[b] -= wi
            if load[b] == 0:
                break
        return False

    feasible = solve(0)

    toks = output_text.split()
    if not toks:
        return False, "empty output"

    head = toks[0].upper()
    if head == "NO":
        if feasible:
            return False, "reported NO but a valid loading exists"
        return True, "correctly reported no loading"

    if head != "YES":
        return False, f"first token must be YES or NO, got {toks[0]!r}"

    if not feasible:
        return False, "reported YES but the items cannot be loaded into k containers"

    nums = toks[1:]
    if len(nums) != n:
        return False, f"expected {n} container numbers after YES, got {len(nums)}"

    try:
        bins = [int(v) for v in nums]
    except ValueError:
        return False, "non-integer container number"

    loads = [0] * (k + 1)
    for i, b in enumerate(bins):
        if b < 1 or b > k:
            return False, f"container {b} out of range 1..{k}"
        loads[b] += w[i]
    for b in range(1, k + 1):
        if loads[b] > C:
            return False, f"container {b} holds {loads[b]} > capacity {C}"

    return True, "valid loading"
