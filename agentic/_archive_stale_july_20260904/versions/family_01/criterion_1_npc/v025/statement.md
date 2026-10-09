# Problem A — Memory Bank Allocation

Time limit: 2 s   Memory limit: 256 MB

You are optimizing the memory layout for a processing unit with $n$ distinct data blocks, numbered 1 to $n$. The architecture features exactly three separate memory banks, labeled 1, 2, and 3. Each data block must be allocated to exactly one of these memory banks.

Due to parallel access conflicts, certain pairs of data blocks cannot reside in the same memory bank. You are provided with $m$ such conflict pairs.

To comply with the strict architectural limits of the processing unit, every scenario you will process is mathematically guaranteed to satisfy the following safety constraints:
- The total number of data blocks $n$ is at most 40.
- The total number of access conflicts $m$ is at most 780.
- For any conflict pair involving block $u$ and block $v$, the sum of their identifiers $u + v$ is at most 80.

Your task is to assign each data block to one of the three memory banks such that no two conflicting blocks are placed in the same bank. 

If a valid allocation is impossible, you must report it. If multiple valid allocations are possible, the firmware requires the lexicographically smallest sequence of bank assignments (minimizing the bank number for block 1, then block 2, and so forth).

## Input
The first line contains two integers $n$ and $m$ — the number of data blocks and the number of conflict pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of conflicting data blocks.

## Output
If no valid allocation exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $b_1, b_2, \dots, b_n$ (where each $b_i \in \{1, 2, 3\}$), representing the memory bank assigned to data block $i$. Among all valid allocations, output the lexicographically smallest sequence.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
1 4
2 4
```
Output:
```
YES
1 2 3 3
```

## Example 2
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
NO
```
