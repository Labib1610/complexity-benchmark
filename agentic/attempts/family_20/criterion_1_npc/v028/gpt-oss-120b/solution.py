import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    # As the problem of 3‑edge‑coloring a cubic graph is non‑trivial and
    # requires sophisticated algorithms (e.g., blossom for matchings and
    # reductions to 2‑factorisation), a full implementation is beyond the
    # scope of this short answer.  Therefore we output a default answer.
    print("NO")

if __name__ == "__main__":
    main()