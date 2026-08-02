import sys


def overlap(a: str, b: str) -> int:
    # longest L with a[-L:] == b[:L], via prefix-function of b + sep + a
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


def main():
    data = sys.stdin.buffer.read().split()
    s1 = data[0].decode()
    s2 = data[1].decode()

    cands = []
    if s1 in s2:
        cands.append(s2)
    if s2 in s1:
        cands.append(s1)
    cands.append(s1 + s2[overlap(s1, s2):])   # s1 then s2
    cands.append(s2 + s1[overlap(s2, s1):])   # s2 then s1

    best = min(cands, key=lambda x: (len(x), x))
    sys.stdout.write(best + "\n")


main()
