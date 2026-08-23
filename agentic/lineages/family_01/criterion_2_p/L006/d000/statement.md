# Shift Scheduling

Time limit: 1 s   Memory limit: 256 MB

A manufacturing facility runs two daily shifts, labeled 1 and 2. The facility employs $n$ technicians, numbered 1 to $n$. Because they must share a single specialized tool, certain pairs of technicians cannot work during the same shift. There are $m$ such incompatible pairs.

Assign each technician a shift so that no incompatible pair works the same shift. To respect seniority, if multiple valid assignments exist, you must output the one that is lexicographically smallest (assigning lower-numbered technicians to shift 1 whenever possible). If no valid schedule exists, report impossibility.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a pair of technicians who cannot share a shift.

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
