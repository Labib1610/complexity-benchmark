# Problem C — Proof of Impossibility

Time limit: 2 s
Memory limit: 256 MB

Management insists on dividing the workforce into exactly two non-overlapping shifts. However, the HR department knows this plan is doomed. You must provide undeniable proof of this failure.

You are given a list of grievances. Each grievance indicates that a specific pair of employees refuse to be assigned to the same shift. 

It is a known fact that within the workforce, there exists at least one trio of employees who all mutually refuse to work with one another (meaning all three possible pairs among them have filed grievances). Such a trio mathematically guarantees that two shifts are inadequate. Your task is to identify and report one such trio to HR.

## Input
The first line contains two integers n and m (3 ≤ n ≤ 2000, 3 ≤ m ≤ min(n·(n−1)/2, 2·10⁵)), representing the number of employees and the number of grievances, respectively. Employees are identified by integers from 1 to n.

Each of the next m lines contains two integers u and v (1 ≤ u, v ≤ n, u ≠ v), representing a pair of employees who refuse to share a shift.

It is guaranteed that at least one trio of mutually incompatible employees exists.

## Output
Print three integers a, b, and c, separated by spaces, representing the IDs of the employees in the trio. You must list them in ascending order (a < b < c).

To ensure a unique valid response when multiple such trios exist, you must select the trio that minimizes the value of a. If there is a tie, minimize the value of b among the tied trios, and if a tie still persists, minimize c.

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