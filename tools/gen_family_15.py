#!/usr/bin/env python3
"""Seeded, deterministic input generators for family 15 (longest common subsequence).

Usage:
    python tools/gen_family_15.py --criterion 1 --k 4 --L 20 --seed 4 --alphabet abc
    python tools/gen_family_15.py --criterion 2 --L 2000 --seed 3 --mode identical
    python tools/gen_family_15.py --criterion 3 --k 3 --L 2000 --seed 5
"""
import argparse
import random
import string


# --- criterion 1: k sequences, small alphabet (many partial matches) ------------
def gen_lcs_multi(k, L, seed, alphabet="abc"):
    """k random sequences of length L over a SMALL alphabet. A small alphabet creates
    many partial matches, so a memo-less recursive LCS branches maximally (~k^L), while
    the k-dimensional DP reference is O(L^k)."""
    rng = random.Random(seed * 1_000_003 + 11)
    A = list(alphabet)
    seqs = ["".join(rng.choice(A) for _ in range(L)) for _ in range(k)]
    return f"{k}\n" + "\n".join(seqs) + "\n"


# --- criterion 2: two sequences -------------------------------------------------
def gen_lcs_two(L, seed, mode="random"):
    """Two length-L sequences. mode:
      identical -> equal strings (LCS = the whole string).
      low       -> mostly different so the LCS is short (~1).
      random    -> random over a small alphabet.
    """
    # Unified schema (audit B4): a "k" header (k=2) then the two sequences, matching criterion 1.
    rng = random.Random(seed * 2_000_003 + 7)
    if mode == "identical":
        s = "".join(rng.choice("abcdefgh") for _ in range(L))
        return f"2\n{s}\n{s}\n"
    if mode == "low":
        # first uses letters a-m, second uses n-z, but share exactly one 'a' each -> LCS ~1
        s1 = "".join(rng.choice("abcdefghijklm") for _ in range(L - 1)) + "a"
        s2 = "a" + "".join(rng.choice("nopqrstuvwxyz") for _ in range(L - 1))
        return f"2\n{s1}\n{s2}\n"
    s1 = "".join(rng.choice("abcd") for _ in range(L))
    s2 = "".join(rng.choice("abcd") for _ in range(L))
    return f"2\n{s1}\n{s2}\n"


# --- criterion 3: disjoint alphabets --------------------------------------------
def gen_disjoint_alphabets(k, L, seed):
    """k sequences over MUTUALLY DISJOINT letter sets (partition the 26 letters into k
    blocks), so no letter is common to all -> no non-empty shared motif. A memo-less LCS
    attempt still explores exponentially before concluding NONE."""
    rng = random.Random(seed * 3_000_003 + 5)
    letters = list(string.ascii_lowercase)
    block = max(1, len(letters) // k)
    seqs = []
    for i in range(k):
        alpha = letters[i * block:(i + 1) * block] or [letters[i % 26]]
        seqs.append("".join(rng.choice(alpha) for _ in range(L)))
    return f"{k}\n" + "\n".join(seqs) + "\n"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--criterion", type=int, required=True, choices=[1, 2, 3])
    p.add_argument("--k", type=int, default=3)
    p.add_argument("--L", type=int, default=20)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--alphabet", default="abc")
    p.add_argument("--mode", default="random")
    args = p.parse_args()

    if args.criterion == 1:
        out = gen_lcs_multi(args.k, args.L, args.seed, alphabet=args.alphabet)
    elif args.criterion == 2:
        out = gen_lcs_two(args.L, args.seed, mode=args.mode)
    else:
        out = gen_disjoint_alphabets(args.k, args.L, args.seed)

    import sys
    sys.stdout.write(out)


if __name__ == "__main__":
    main()
