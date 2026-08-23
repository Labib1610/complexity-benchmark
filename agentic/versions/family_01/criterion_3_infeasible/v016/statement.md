# Problem C — Shift Assignment Failure

Time limit: 2 s   Memory limit: 256 MB

The manufacturing plant operates exclusively on a day shift and a night shift. Management has gathered a list of incompatibilities between certain employees who refuse to work the same shift. It has already been determined that assigning everyone to just two shifts is an unsolvable task. Your objective is not to attempt an assignment, but to provide concrete evidence of this failure to the human resources department.

Specifically, any group of three employees where every individual refuses to work with both of the other two constitutes undeniable proof that two shifts are inadequate. You must identify one such trio.

## Input
The first line contains the employee headcount $n$ and the total number of incompatibilities $m$.
The factory's locker room has exactly 2,000 lockers, meaning $n$ is at most this capacity. Naturally, $n$ is at least the size of the trio you are trying to find.
The HR database has a hard limit of 200,000 incompatibility records. Thus, $m$ never exceeds this database limit, nor does it exceed the maximum possible number of distinct pairs among the $n$ employees. The value of $m$ is at least the number of incompatibilities that exist among the three members of the aforementioned undeniable proof.

The next $m$ lines each contain two integers $u$ and $v$ — the ID numbers of an incompatible pair of employees. Employee IDs are integers from $1$ to $n$. It is guaranteed that the records contain at least one trio of the required type.

## Output
Print three integers $a$, $b$, and $c$ on one line with $a < b < c$, representing the IDs of three employees who are all mutually incompatible with one another. If multiple such groups exist, output the one that is lexicographically smallest (the one with the smallest $a$; in case of a tie, the smallest $b$; and if still tied, the smallest $c$).

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
