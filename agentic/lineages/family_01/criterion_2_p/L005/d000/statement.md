# Problem B — Day and Night

Time limit: 1 s   Memory limit: 256 MB

The factory now runs only two shifts, labeled 1 and 2. There are $n$ workers and $m$ interaction records between pairs of workers. Assign each worker exactly one shift such that if an interaction record exists between two workers, they are placed in different shifts. If no such assignment can be made, report impossibility.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of workers with an interaction record.

## Output
If no valid assignment exists, print a single line NO.
Otherwise print YES, then a second line with $n$ integers $s_1 \dots s_n$ (each in {1,2}), the lexicographically smallest valid assignment.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```
