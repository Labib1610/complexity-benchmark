# Problem C — Shift Assignment Pipeline: Stage 2

Time limit: 2 s   Memory limit: 256 MB

You are developing an automated scheduling pipeline for a manufacturing plant that operates exclusively on two daily shifts. The pipeline executes in three distinct stages:

**Stage 1: Data Ingestion.** The system aggregates all employee records and interpersonal conflict reports, producing a consolidated list of mutual incompatibilities.

**Stage 2: Feasibility Analysis (Your Task).** Before deploying the main assignment logic, the system must fast-track cases that are fundamentally unsolvable. If there is a trio of employees where every individual refuses to work with the other two, a two-shift schedule cannot possibly be formed. 

**Stage 3: HR Escalation.** If Stage 2 finds a broken configuration, the pipeline halts and forwards minimal evidence to Human Resources for manual intervention.

Your job is to implement Stage 2. You will receive the parsed output from Stage 1. It is guaranteed that the provided data contains at least one trio of employees who are completely mutually incompatible with one another. To ensure the escalation reports are consistent and reproducible, you must identify exactly one such trio according to a strict tie-breaking rule to pass on to Stage 3.

## Input
The first line provides two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2 \cdot 10^5)$), representing the number of employees and the total number of mutual incompatibilities. Employees are identified by integers from $1$ to $n$.

The following $m$ lines each contain two integers $u$ and $v$, indicating that employee $u$ and employee $v$ cannot be assigned to the same shift. 

It is guaranteed that at least one trio of mutually incompatible employees exists in the data.

## Output
Output a single line containing three integers $a$, $b$, and $c$, representing the identifiers of three employees who all refuse to work with each other. 

The three identifiers must be printed in ascending order ($a < b < c$). 

If there are multiple such trios, output the one that is lexicographically first (i.e., minimize $a$; if tied, minimize $b$; if still tied, minimize $c$).

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
