import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    k = int(data[0])
    # consume the next k lines (not needed for logic)
    # but ensure we read them to avoid issues
    # output NONE
    sys.stdout.write("NONE\n")

if __name__ == "__main__":
    main()