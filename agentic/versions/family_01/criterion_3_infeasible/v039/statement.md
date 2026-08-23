# Problem C — Proof of Impossibility

Time limit: 2 s   Memory limit: 256 MB

The manufacturing plant relies on two operating teams, but the current personnel roster is fundamentally flawed. Your task is not to assign employees to teams, but to provide the formal documentation proving that a valid arrangement is unattainable. It is a known fact that the personnel records contain at least one group of three employees where every individual in the group has a mutual incompatibility with both of the other two. Any such trio guarantees that two teams are inadequate. You must identify and output the members of one such trio.

## Input
The first line provides the employee headcount $n$ and the number of incompatibility records $m$. The headcount $n$ starts at a minimum of 3 and reaches up to the facility capacity of 2000. The number of records $m$ is at least 3 and never exceeds the lesser of the total number of possible unique pairs among the $n$ employees and the database limit of 200000.
Each of the subsequent $m$ lines contains two integers $u$ and $v$ representing an incompatible employee pair.
It is guaranteed that at least one group of three mutually incompatible employees exists.

## Output
Output a single line containing three integers $a$, $b$, and $c$ with $a < b < c$, such that the pairs $a$ and $b$, $a$ and $c$, and $b$ and $c$ are all present in the incompatibility records. You must output the trio that comes first numerically (the smallest value for $a$; in case of a tie, the smallest value for $b$; and if still tied, the smallest value for $c$).

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
