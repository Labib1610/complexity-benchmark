# Problem B — Day and Night

Time limit: 1 s   Memory limit: 256 MB

The factory operates continuously using exactly two shifts, labeled 1 and 2. There are $n$ workers. The factory features $m$ workstations. For each workstation, exactly two specific workers are trained to use it.

To ensure every workstation is active around the clock, its two trained workers must be distributed across the two shifts: one must be assigned to shift 1, and the other to shift 2.

Assign each worker exactly one shift so that all workstations are active in both shifts, or report impossibility.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — the two workers trained to use that workstation.

## Output
If no valid assignment exists, print a single line NO.
Otherwise print YES, then a second line with $n$ integers $s_1 \dots s_n$ (each in $\{1,2\}$), representing the lexicographically smallest valid assignment.

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