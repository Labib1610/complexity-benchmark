import sys


def validate(input_text: str, output_text: str):
    sys.setrecursionlimit(1 << 20)
    data = input_text.split()
    idx = 0
    k = int(data[idx]); idx += 1
    e = int(data[idx]); idx += 1

    allowed = set()
    adj = [[] for _ in range(k + 1)]
    for _ in range(e):
        x = int(data[idx]); y = int(data[idx + 1]); idx += 2
        allowed.add((x, y))
        adj[x].append(y)

    # Re-derive ground truth via Kuhn's augmenting-path matching.
    match_y = [0] * (k + 1)

    def try_augment(x, visited):
        for y in adj[x]:
            if not visited[y]:
                visited[y] = True
                if match_y[y] == 0 or try_augment(match_y[y], visited):
                    match_y[y] = x
                    return True
        return False

    matched = 0
    for x in range(1, k + 1):
        if try_augment(x, [False] * (k + 1)):
            matched += 1
    feasible = matched == k

    toks = output_text.split()
    if not toks:
        return False, "empty output"

    head = toks[0].upper()
    if head == "NO":
        if feasible:
            return False, "reported NO but a valid assignment exists"
        return True, "correctly reported no assignment"

    if head != "YES":
        return False, f"first token must be YES or NO, got {toks[0]!r}"

    if not feasible:
        return False, "reported YES but no valid assignment exists"

    nums = toks[1:]
    if len(nums) != k:
        return False, f"expected {k} task numbers after YES, got {len(nums)}"

    try:
        part = [int(v) for v in nums]
    except ValueError:
        return False, "non-integer task number"

    if len(set(part)) != k:
        return False, "two workers were assigned the same task"

    for i, y in enumerate(part):
        x = i + 1
        if y < 1 or y > k:
            return False, f"task {y} out of range 1..{k}"
        if (x, y) not in allowed:
            return False, f"pair (worker {x}, task {y}) is not allowed"

    return True, "valid assignment"
