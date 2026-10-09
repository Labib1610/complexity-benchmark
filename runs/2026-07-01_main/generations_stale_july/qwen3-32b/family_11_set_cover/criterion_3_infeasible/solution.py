import sys

def main():
    u, s = map(int, sys.stdin.readline().split())
    skills = [False] * (u + 1)
    for _ in range(s):
        data = list(map(int, sys.stdin.readline().split()))
        for skill in data[1:]:
            skills[skill] = True
    for i in range(1, u + 1):
        if not skills[i]:
            print(i)
            return

if __name__ == "__main__":
    main()