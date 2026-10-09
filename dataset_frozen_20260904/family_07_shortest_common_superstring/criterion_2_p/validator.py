def _overlap(a, b):
    t = b + "\x00" + a
    pi = [0] * len(t)
    for i in range(1, len(t)):
        j = pi[i - 1]
        while j > 0 and t[i] != t[j]:
            j = pi[j - 1]
        if t[i] == t[j]:
            j += 1
        pi[i] = j
    return pi[-1]


def validate(input_text: str, output_text: str):
    data = input_text.split()
    k = int(data[0])
    s1 = data[1]
    s2 = data[2]

    # Minimum superstring length of two strings.
    cand = []
    if s1 in s2:
        cand.append(len(s2))
    if s2 in s1:
        cand.append(len(s1))
    cand.append(len(s1) + len(s2) - _overlap(s1, s2))
    cand.append(len(s2) + len(s1) - _overlap(s2, s1))
    min_len = min(cand)

    out = output_text.split()
    if not out:
        return False, "empty output"
    sup = out[0]

    if s1 not in sup:
        return False, "first fragment is not a substring of the output"
    if s2 not in sup:
        return False, "second fragment is not a substring of the output"
    if len(sup) != min_len:
        return False, f"output length {len(sup)} is not the minimum {min_len}"
    return True, "valid shortest common superstring"
