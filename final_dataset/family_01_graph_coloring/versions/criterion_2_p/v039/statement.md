# Problem B — Phase Scheduling

Time limit: 1 s   Memory limit: 256 MB

A manufacturing facility requires exactly two maintenance phases per day, labeled 1 and 2. The facility employs $n$ technicians, and there are $m$ pairs of technicians who share specialized tools. You must schedule each technician into exactly one phase such that no two technicians who share tools are scheduled for the same phase, or report impossibility.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of technicians who share tools.

## Output
If no valid schedule exists, print a single line NO.
Otherwise print YES, then a second line with $n$ integers $s_1 \dots s_n$ (each in {1,2}), representing the lexicographically smallest valid schedule.

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
