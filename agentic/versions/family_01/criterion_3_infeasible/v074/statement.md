# Problem C — Conflict Resolution Study

Time limit: 2 s
Memory limit: 256 MB

The human resources department is conducting a study on workplace conflict. They have compiled a comprehensive registry of documented incompatibilities between pairs of employees. The goal of the study is to assemble a perfectly dysfunctional focus group. A group of employees is considered perfectly dysfunctional if every individual in the group has a documented incompatibility with every other individual in the same group.

Given that the company employs up to two thousand individuals, the number of potential focus groups is astronomically large, easily exceeding the number of atoms in the observable universe. Evaluating every conceivable subset of employees to check for total internal incompatibility would require an impractical amount of computation. You have been tasked with developing a tool to navigate this massive search space and identify a valid focus group to facilitate the study. The researchers have secured a budget to compensate exactly three employees for their participation in this phase, so the focus group must be exactly this size.

You are guaranteed that the registry contains at least one such focus group. If multiple valid groups can be formed, you must report the one whose members' employee ID numbers form the lexicographically smallest sequence when sorted in ascending order.

## Input
The first line of the input contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n \cdot (n-1)/2, 2\cdot 10^5)$), representing the number of employees and the number of documented incompatibility records, respectively. Employees are identified by integers from $1$ to $n$.

The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating a documented incompatibility between employee $u$ and employee $v$. Each pair is listed at most once, and the order of $u$ and $v$ does not matter. It is guaranteed that there is at least one perfectly dysfunctional focus group of the required size.

## Output
Output a single line containing three integers $a$, $b$, and $c$ with $a < b < c$, representing the employee IDs of the chosen focus group. The sequence $a, b, c$ must be the lexicographically smallest valid sequence (smallest $a$; in case of ties, smallest $b$; then smallest $c$).

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
