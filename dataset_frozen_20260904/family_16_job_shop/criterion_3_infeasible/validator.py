def validate(input_text: str, output_text: str):
    data = input_text.split()
    idx = 0
    j = int(data[idx]); T = int(data[idx + 1]); idx += 2
    p1 = [0] * j
    p2 = [0] * j
    for i in range(j):
        p1[i] = int(data[idx]); p2[i] = int(data[idx + 1]); idx += 2

    toks = output_text.split()
    if not toks:
        return False, "empty output"

    head = toks[0].upper()

    # A bare NO (or any non-certificate) must fail: this arm requires a checkable proof of
    # impossibility, not a constant answer (audit B5).
    if head == "JOB":
        if len(toks) < 2:
            return False, "JOB certificate missing the job index"
        try:
            i = int(toks[1])
        except ValueError:
            return False, f"job index must be an integer, got {toks[1]!r}"
        if i < 1 or i > j:
            return False, f"job index {i} out of range 1..{j}"
        if p1[i - 1] + p2[i - 1] > T:
            return True, f"valid JOB certificate: job {i} needs {p1[i-1]+p2[i-1]} > T={T}"
        return False, f"JOB certificate invalid: job {i} total {p1[i-1]+p2[i-1]} does not exceed T={T}"

    if head == "LOAD":
        if len(toks) < 2:
            return False, "LOAD certificate missing the machine index"
        try:
            c = int(toks[1])
        except ValueError:
            return False, f"machine index must be an integer, got {toks[1]!r}"
        if c == 1:
            load = sum(p1)
        elif c == 2:
            load = sum(p2)
        else:
            return False, f"machine index must be 1 or 2, got {c}"
        if load > T:
            return True, f"valid LOAD certificate: machine {c} total load {load} > T={T}"
        return False, f"LOAD certificate invalid: machine {c} load {load} does not exceed T={T}"

    return False, f"first token must be JOB or LOAD, got {toks[0]!r}"
