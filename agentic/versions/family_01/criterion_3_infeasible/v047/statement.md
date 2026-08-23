# Grievance Log Audit

Time limit: 2 s   Memory limit: 256 MB

A mediation board is assessing a manufacturing plant's request to transition from a dual-shift system to a three-shift system. To approve this transition, the board requires documented proof that the two-shift system cannot accommodate the workforce. Management has provided a log of registered grievances, where each entry indicates two specific employees who refuse to work concurrently. Under board regulations, the definitive proof of a failed two-shift system is a triad of employees where every individual in the triad has a registered grievance against both of the others. Your assignment is to extract exactly one such triad from the logs to serve as the official certificate. To ensure a standardized audit process, if multiple such triads exist, you must select the one that is lexicographically first based on the employees' numerical identifiers.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), representing the number of employees and the number of registered grievances, respectively.
Each of the following $m$ lines contains two integers $u$ and $v$ — identifying a pair of employees who refuse to work concurrently.
It is guaranteed that the logs contain at least one valid triad of employees.

## Output
Print three integers $a$, $b$, and $c$ on a single line, ordered such that $a < b < c$, representing the employees in the triad. You must output the lexicographically smallest triad (i.e., the triad with the smallest $a$; in case of a tie, the smallest $b$; and if still tied, the smallest $c$).

## Example 1
Input:
```
4 5
1 2
1 3
2 3
2 4
3 4
```
Output:
```
1 2 3
```

## Example 2
Input:
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
Output:
```
1 2 4
```
