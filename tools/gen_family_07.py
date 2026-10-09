#!/usr/bin/env python3
"""Seeded, deterministic input generators for family 07 (shortest common superstring).

Usage:
    python tools/gen_family_07.py --criterion 1 --k 14 --len 14 --seed 4 --alphabet ab
    python tools/gen_family_07.py --criterion 2 --n 100000 --seed 3 --mode worst
    python tools/gen_family_07.py --criterion 3 --k 30 --len 12 --seed 5 --at high
"""
import argparse
import random


# --- criterion 1: k fragments (small alphabet -> many spurious overlaps) --------
def gen_scs(k, length, seed, alphabet="ab"):
    """k random fragments over a small alphabet. A small alphabet maximises spurious
    suffix-prefix overlaps, so many orderings look promising and defeat the pruning of
    a permutation search, while the bitmask DP is unaffected. No fragment is a
    substring of another (regenerated until distinct enough) so all k stay 'live'."""
    rng = random.Random(seed * 1_000_003 + 11)
    A = list(alphabet)
    frags = []
    tries = 0
    while len(frags) < k and tries < 200 * k + 1000:
        tries += 1
        s = "".join(rng.choice(A) for _ in range(length))
        if any(s in f or f in s for f in frags):
            continue                              # avoid containment (keeps all live)
        frags.append(s)
    while len(frags) < k:                          # fallback: pad with distinct tails
        frags.append("".join(rng.choice(A) for _ in range(length)) + A[0] * (len(frags)))
    lines = [str(k)] + frags
    return "\n".join(lines) + "\n"


# --- criterion 2: two strings -------------------------------------------------
def gen_two_strings(n, seed, mode="worst"):
    """Two length-n strings. mode:
      worst      -> 'aa...a' and 'aa...ab': naive overlap compares maximally at every L.
      long       -> a real long shared overlap between the end of s1 and start of s2.
      none       -> no shared end/start (naive still scans all L before giving up).
      identical  -> s1 == s2.
    """
    rng = random.Random(seed * 2_000_003 + 7)
    if mode == "worst":
        s1 = "a" * n
        s2 = "a" * (n - 1) + "b"
    elif mode == "identical":
        s1 = "".join(rng.choice("ab") for _ in range(n)); s2 = s1
    elif mode == "long":
        ov = n // 2
        shared = "".join(rng.choice("ab") for _ in range(ov))
        s1 = "".join(rng.choice("ab") for _ in range(n - ov)) + shared
        s2 = shared + "".join(rng.choice("ab") for _ in range(n - ov))
    else:  # none: distinct alphabets at the seam so no suffix-prefix overlap
        s1 = "a" * n
        s2 = "b" * n
    return f"2\n{s1}\n{s2}\n"   # unified schema: k header (k=2)


# --- criterion 3: a fragment that contains the forbidden string ---------------
def gen_forbidden(k, length, seed, F="abab", at="high"):
    """k fragments over a small alphabet plus a forbidden string F; the fragment at a
    HIGH (or given) index contains F, others avoid it. Answer = smallest index whose
    fragment contains F. Fragments are hard-to-assemble (small alphabet) so a baseline
    that tries to build the superstring first TLEs."""
    rng = random.Random(seed * 3_000_003 + 5)
    if at == "high":
        at_idx = k
    elif at == "low":
        at_idx = 1
    else:
        at_idx = int(at)
    A = "ab"
    frags = []
    for i in range(1, k + 1):
        if i == at_idx:
            pre = "".join(rng.choice(A) for _ in range(max(0, length - len(F))))
            frags.append(pre + F)                 # contains F
        else:
            while True:
                s = "".join(rng.choice(A) for _ in range(length))
                if F not in s:
                    break
            frags.append(s)
    lines = [str(k)] + frags + [F]
    return "\n".join(lines) + "\n"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--criterion", type=int, required=True, choices=[1, 2, 3])
    p.add_argument("--k", type=int, default=0)
    p.add_argument("--n", type=int, default=0)
    p.add_argument("--len", type=int, default=14, dest="length")
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--alphabet", default="ab")
    p.add_argument("--mode", default="worst")
    p.add_argument("--F", default="abab")
    p.add_argument("--at", default="high")
    args = p.parse_args()

    if args.criterion == 1:
        out = gen_scs(args.k, args.length, args.seed, alphabet=args.alphabet)
    elif args.criterion == 2:
        out = gen_two_strings(args.n, args.seed, mode=args.mode)
    else:
        out = gen_forbidden(args.k, args.length, args.seed, F=args.F, at=args.at)

    import sys
    sys.stdout.write(out)


if __name__ == "__main__":
    main()
