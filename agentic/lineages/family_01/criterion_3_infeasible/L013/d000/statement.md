# Problem C — Proof of Impossibility

Time limit: 2 s   Memory limit: 256 MB

A manufacturing plant employs $n$ individuals, numbered 1 through $n$. The HR department has identified $m$ specific pairs of employees who exhibit irreconcilable differences. If two employees share an irreconcilable difference, they cannot be placed on the same schedule. It is guaranteed that the provided records contain at least one triad of employees where all three individuals mutually refuse to work with one another—meaning every employee in the triad has an irreconcilable difference with both of the other two.

Management initially proposed dividing the workforce into exactly two daily shifts. However, this proposal is fundamentally unworkable. Because of the existence of such a triad, no two-shift system can possibly accommodate them without forcing two incompatible employees to work together.

To finalize the rejection of the two-shift proposal, you must provide a formal certificate of its failure. Your task is to identify one of these mutually incompatible triads.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2 \cdot 10^5)$).
The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), representing an irreconcilable difference between employee $u$ and employee $v$. Each incompatible pair is listed at most once.
It is guaranteed that at least one mutually incompatible triad exists.

## Output
Print three integers $a$, $b$, and $c$ on a single line, separated by spaces, representing the IDs of three employees who form a mutually incompatible triad. The IDs must be printed in ascending order ($a < b < c$).
If there are multiple such triads, you must output the one that is lexicographically smallest. That is, minimize $a$; if there is a tie, minimize $b$; and if there is still a tie, minimize $c$.

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
