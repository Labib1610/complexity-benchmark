# Problem B — Day and Night

Time limit: 1 s   Memory limit: 256 MB

A manufacturing plant employs $n$ workers, numbered 1 through $n$. The plant's safety system contains $m$ records of worker pairs who have previously had altercations. To prevent future incidents, management has established a strict rule: any two workers involved in a recorded altercation must be separated. The plant operates on exactly two shifts, shift 1 and shift 2. Each worker must be assigned to exactly one of these two shifts.

You must process the safety records and output a shift assignment for all $n$ workers. The assignment must comply with management's separation rule. If there are multiple compliant assignments, you must select the one yielding the lexicographically smallest sequence of shift numbers ($s_1, s_2, \dots, s_n$). If no compliant assignment is possible, you must report that it cannot be done.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
Each of the next $m$ lines contains two integers $u$ and $v$, representing a pair of workers who have a recorded altercation.

## Output
If no compliant shift assignment exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1 \dots s_n$ (each either 1 or 2), representing the lexicographically smallest compliant shift assignment.

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
