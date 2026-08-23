# Production Block Assignment

Time limit: 2 s   Memory limit: 256 MB

A manufacturing plant organizes its daily operations into three distinct production blocks, designated as 1, 2, and 3. Every employee on the payroll must be assigned to exactly one of these blocks. Due to safety regulations and interpersonal grievances, certain pairs of employees are deemed incompatible and are strictly prohibited from working during the same production block.

You must determine if there is a valid schedule that assigns every employee to one of the three blocks without placing any incompatible pair together, or determine that no such schedule exists.

## Input
The first line provides two integers $n$ and $m$ — the total staff count and the number of incompatible pairs. The staff count $n$ is strictly positive and will not exceed the total number of available lockers in the changing room. The locker room features exactly 8 rows of lockers, with each row containing exactly 5 lockers, which strictly caps the maximum possible staff size. The value $m$ can be zero and is at most the theoretical maximum where every distinct pair of employees is incompatible.

Following this, $m$ lines are provided. Each of these lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), indicating that employee $u$ and employee $v$ cannot be assigned to the same production block.

## Output
If there is no way to assign the employees to the blocks without violating the incompatibility constraints, output a single line containing `NO`.

If a valid assignment is possible, output `YES` on the first line. On the second line, output $n$ integers $s_1, s_2, \dots, s_n$ (each being 1, 2, or 3), where $s_i$ corresponds to the production block assigned to employee $i$. If there are multiple valid ways to assign the employees, you must output the sequence of block numbers that is lexicographically smallest (i.e., compare the assignment for employee 1 first; in case of a tie, compare employee 2, and so forth).

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
