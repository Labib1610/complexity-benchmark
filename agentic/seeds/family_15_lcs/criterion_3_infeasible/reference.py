import sys


def main():
    data = sys.stdin.buffer.read().split()
    k = int(data[0])
    seqs = [data[1 + i].decode() for i in range(k)]

    # A non-empty shared motif needs at least one letter present in every
    # sequence. Intersect the letter sets; if empty, none exists.
    common = set(seqs[0])
    for s in seqs[1:]:
        common &= set(s)

    if not common:
        print("NONE")
        return

    # Fallback (inputs for this criterion always have disjoint alphabets).
    print(min(common))


main()
