best = -1; bestc = INF
for x in uncovered:
    c = cnt[x]
    if c < bestc: bestc = c; best = x
    if c == 1: break  # can't do better... wait, c could be 0 → even better (fail).