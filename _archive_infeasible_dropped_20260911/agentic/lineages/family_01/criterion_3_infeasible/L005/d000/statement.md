# Problem C — Justifying the Roster Failure

Time limit: 2 s   Memory limit: 256 MB

The management wants to assign all personnel to two distinct working periods. However, the current list of incompatibilities makes this division strictly unachievable. You are required to provide the management with a concrete justification for this failure. 

It is a known fact that if there is a group of three individuals where every individual has a documented incompatibility with both of the other two, it becomes logically impossible to place them into just two periods. The management guarantees that the provided records contain at least one such group of three individuals. Your task is to identify one such group.

## Input
The first line contains two integers n and m (3 ≤ n ≤ 2000, 3 ≤ m ≤ min(n·(n−1)/2, 2·10⁵)), representing the number of personnel and the number of documented incompatibilities, respectively. Personnel are numbered from 1 to n.

Each of the next m lines contains two integers u and v — indicating that individual u and individual v cannot be assigned to the same working period.

It is guaranteed that at least one group of three mutually incompatible individuals exists.

## Output
Print three integers a, b, and c on a single line, satisfying a < b < c, such that a is incompatible with b, a is incompatible with c, and b is incompatible with c.

If there are multiple such groups, output the one that comes first lexicographically (minimize a; in case of a tie, minimize b; and finally minimize c).

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
