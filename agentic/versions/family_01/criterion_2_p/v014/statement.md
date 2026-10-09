# Shift Allocation

Time limit: 1 s
Memory limit: 256 MB

A manufacturing plant operates continuously across a daytime rotation (labeled `1`) and a nighttime rotation (labeled `2`). The plant's locker room has exactly 200,000 lockers, and each employee requires one. The workforce size $n$ is at least one and cannot exceed this total locker count. 

The human resources department has compiled $m$ records of interpersonal friction between specific pairs of employees. The dispute tracking system has a fixed storage limit of 200,000 records, so the number of disputes $m$ can be anything from an empty list up to the system's maximum capacity.

You must assign every employee to either rotation `1` or rotation `2`. To maintain productivity, no two employees involved in a friction record may be assigned to the same rotation. If it is impossible to satisfy all constraints, you must report this.

If there are multiple valid ways to assign the rotations, you must choose the one that is lexicographically smallest when the assignments are listed in order of employee ID (from 1 to $n$).

## Input
The first line contains two integers $n$ and $m$, representing the number of employees and the number of friction records, respectively. Their possible ranges are determined by the physical and system limits described above.
Each of the following $m$ lines contains two integers $u$ and $v$, indicating a friction record between employee $u$ and employee $v$.

## Output
If there is no way to assign the employees to the two rotations without violating the friction constraints, output a single line containing `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ space-separated integers, each either `1` or `2`, representing the lexicographically smallest valid rotation assignment for employees 1 through $n$.

## Example 1
Input:
```
4 4
1 2
2 3
3 4
1 4
```
Output:
```
YES
1 2 1 2
```

## Example 2
Input:
```
3 3
1 2
1 3
2 3
```
Output:
```
NO
```
