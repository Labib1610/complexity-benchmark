# Problem A — Task Window Assignment

Time limit: 2 s   Memory limit: 256 MB

A project has n tasks. Each task can be either active (1) or inactive (0). The
project has m compatibility requirements. Each requirement lists three task-state
conditions and demands that at least one of them holds. A condition is either
"task i is active" (written as the positive integer i) or "task i is inactive"
(written as the negative integer −i).

Decide whether it is possible to assign every task a state so that all requirements
are satisfied. If yes, output the lexicographically smallest valid assignment.

## Input
The first line contains two integers n and m (1 ≤ n ≤ 90, 0 ≤ m ≤ 400).
Each of the next m lines contains three non-zero signed integers l1 l2 l3,
with |li| ≤ n. At least one of the three stated conditions must hold.

## Output
If no valid assignment exists, print a single line NO.
Otherwise print YES on the first line. On the second line print n integers
s1 s2 … sn (each in {0, 1}), where si is the state of task i. Among all valid
assignments output the lexicographically smallest sequence (compare s1 first,
then s2, and so on).

## Example 1
Input:
```
3 2
1 2 3
-1 2 -3
```
Output:
```
YES
0 0 1
```

## Example 2
Input:
```
1 2
1 1 1
-1 -1 -1
```
Output:
```
NO
```

## Note
Each requirement group has exactly three entries. The same task index may appear
more than once in a group.
