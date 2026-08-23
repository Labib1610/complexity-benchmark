# Problem A — Workflow Phases

Time limit: 2 s   Memory limit: 256 MB

A manufacturing plant is reorganizing its workforce of $n$ employees, numbered 1 through $n$. The daily schedule is divided into distinct operational phases. The phase identifiers available for assignment are 1, 2, and 3. Each employee must be assigned exactly one phase identifier.

During preliminary testing, it was observed that specific combinations of employees disrupt the workflow when operating simultaneously. You are provided with a ledger of these disruptions. Each entry in the ledger lists two employees. 

The scheduling system must enforce the following operational rule: for every entry in the ledger, the assignment is only valid if the phase identifier given to the first listed employee and the phase identifier given to the second listed employee are strictly unequal.

Determine if there is a valid phase assignment for all $n$ employees. If multiple valid assignments exist, you must resolve the ambiguity using a sequential tie-breaking process:
1. Consider the set of all valid assignments.
2. Restrict this set to only those assignments that give the smallest possible phase identifier to employee 1.
3. If the set still contains multiple assignments, further restrict it to those that give the smallest possible phase identifier to employee 2.
4. Continue this process for employee 3, employee 4, and so on, until exactly one assignment remains.

## Input
The first line contains two integers $n$ and $m$ — the number of employees and the number of ledger entries ($1 \le n \le 40$, $0 \le m \le n \cdot (n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ — the two employees listed in a ledger entry.

## Output
If no assignment can satisfy all rules, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (where each $s_i \in \{1, 2, 3\}$), representing the phase identifier assigned to employee $i$. If there are multiple valid assignments, output the one determined by the sequential tie-breaking process described above.

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
