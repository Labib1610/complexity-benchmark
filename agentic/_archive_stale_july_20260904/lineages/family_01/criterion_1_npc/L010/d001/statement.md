# Problem A — Reactive Storage

Time limit: 2 s   Memory limit: 256 MB

A laboratory operates three storage units identified by the digits 1, 2, and 3. The facility holds $n$ chemical specimens, numbered from 1 to $n$. Certain pairs of specimens are volatile when brought together and must never be placed in the same storage unit. Your task is to allocate each specimen to exactly one of the three units ensuring no volatile pair ends up in the same unit, or determine that no such allocation is possible.

## Input
The first line specifies two integers $n$ and $m$ — representing the total number of specimens and the number of volatile pairs, respectively ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
The following $m$ lines each provide two integers $u$ and $v$ — indicating a pair of specimens that are volatile together.

## Output
If a safe allocation cannot be found, print a single line containing `NO`.
If it is possible, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (each chosen from {1, 2, 3}), where $s_i$ denotes the unit assigned to specimen $i$. Should multiple safe allocations exist, you must resolve ties by preferring the allocation that assigns the lowest possible unit number to specimen 1; if still tied, prefer the lowest possible unit number to specimen 2, and continue this tie-breaking process sequentially up to specimen $n$.

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