import sys
import threading

def solve():
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    it = iter(data)
    u = next(it)
    s = next(it)
    k = next(it)
    masks = []
    for _ in range(s):
        c = next(it)
        mask = 0
        for _ in range(c):
            skill = next(it) - 1
            mask |= 1 << skill
        masks.append(mask)

    full_mask = (1 << u) - 1
    if full_mask == 0:
        print("YES")
        print()
        return

    # Build skill to consultants mapping
    skill_to_consultants = [[] for _ in range(u)]
    for idx, m in enumerate(masks):
        tmp = m
        while tmp:
            lsb = tmp & -tmp
            skill = lsb.bit_length() - 1
            skill_to_consultants[skill].append(idx)
            tmp ^= lsb

    # If any skill has no consultant, impossible
    for skill in range(u):
        if not skill_to_consultants[skill]:
            print("NO")
            return

    max_skills_per_consultant = max(m.bit_count() for m in masks)
    if max_skills_per_consultant == 0:
        print("NO")
        return

    sys.setrecursionlimit(10000)
    memo = {}

    def dfs(mask, depth):
        if mask == 0:
            return []
        if depth > k:
            return None
        # lower bound pruning
        remaining = mask.bit_count()
        if depth + (remaining + max_skills_per_consultant - 1) // max_skills_per_consultant > k:
            return None
        prev = memo.get(mask)
        if prev is not None and prev <= depth:
            return None
        memo[mask] = depth

        # choose skill with fewest consultants
        min_len = 10**9
        min_skill = -1
        tmp = mask
        while tmp:
            lsb = tmp & -tmp
            skill = lsb.bit_length() - 1
            l = len(skill_to_consultants[skill])
            if l < min_len:
                min_len = l
                min_skill = skill
                if l == 1:
                    break
            tmp ^= lsb

        for i in skill_to_consultants[min_skill]:
            newmask = mask & ~masks[i]
            res = dfs(newmask, depth + 1)
            if res is not None:
                return [i] + res
        return None

    result = dfs(full_mask, 0)
    if result is None:
        print("NO")
    else:
        print("YES")
        # convert to 1-based indices
        print(' '.join(str(i + 1) for i in result))

def main():
    solve()

threading.Thread(target=main).start()