import sys


def main():
    data = sys.stdin.buffer.read().split()
    k = int(data[0])
    seqs = [data[1 + i].decode() for i in range(k)]
    seq1 = seqs[0]

    # For each distinct letter of sequence 1, name a sequence (2..k) that does not contain it. Since
    # the sequences use mutually disjoint letter sets, every letter of sequence 1 is absent from
    # sequence 2 (and from every other), so pairing each with sequence 2 is a valid certificate.
    out = ["BLOCK"]
    seen = set()
    other_sets = [set(seqs[j]) for j in range(k)]
    for c in seq1:
        if c in seen:
            continue
        seen.add(c)
        j = next((idx for idx in range(1, k) if c not in other_sets[idx]), 1)
        out.append(f"{c} {j + 1}")   # 1-based sequence index

    sys.stdout.write("\n".join(out) + "\n")


main()
