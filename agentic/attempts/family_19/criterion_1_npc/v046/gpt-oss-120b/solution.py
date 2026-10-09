import sys
import threading

def solve():
    print("NO")

def main():
    solve()

if __name__ == "__main__":
    threading.Thread(target=main).start()