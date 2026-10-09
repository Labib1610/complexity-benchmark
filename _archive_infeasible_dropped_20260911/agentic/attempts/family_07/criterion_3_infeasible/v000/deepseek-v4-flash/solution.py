import sys

def main():
    data = sys.stdin.read().splitlines()
    k = int(data[0])
    fragments = data[1:1+k]
    F = data[1+k]
    
    for i, frag in enumerate(fragments, start=1):
        if F in frag:
            print(i)
            return

if __name__ == "__main__":
    main()