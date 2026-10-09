```python
import sys
from collections import deque

def main():
    input = sys.stdin.read().split()
    ptr = 0
    nA = int(input[ptr]); ptr +=1
    nB = int(input[ptr]); ptr +=1
    m = int(input[ptr]); ptr +=1