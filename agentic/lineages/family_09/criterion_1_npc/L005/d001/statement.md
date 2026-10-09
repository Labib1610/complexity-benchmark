# Problem A — Harmonious Delegation

Time limit: 5 s   Memory limit: 256 MB

## Description

A corporate department has **n** employees (numbered 1..n) and a record of **m** formal grievances. Each grievance indicates that one specific employee refuses to take direction from another specific employee.

A project delegation is **harmonious** if no employee in the delegation has a grievance on record against any other employee in the delegation.

Given a target delegation size **k**, decide whether a harmonious delegation of exactly **k** employees exists, and if so report one.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 46, 0 ≤ m ≤ n·(n−1)/2, 1 ≤ k ≤ n).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v), meaning employee **u** has a grievance against employee **v**. The input will never contain more than one grievance involving the same pair of employees (i.e., if **u** and **v** appear together on a line, they will not appear together on any other line in either order).

## Output

If a harmonious delegation of **k** employees exists, print `YES` on the first line, then on the second line print **k** distinct employee numbers forming such a delegation, separated by spaces. Any delegation in which no employee has a grievance against another member is accepted.

If no such delegation exists, print `NO`.

## Examples

### Example 1

**Input**
```
4 4 3
1 2
1 3
2 3
3 4
```

**Output**
```
NO
```

### Example 2

**Input**
```
5 2 3
1 2
3 4
```

**Output**
```
YES
1 3 5
```

### Example 3

**Input**
```
3 3 1
1 2
2 3
1 3
```

**Output**
```
YES
1
```

## Note

A harmonious delegation ensures no chosen employee has a grievance against another chosen employee. In Example 2, employees 1, 3, and 5 have no grievances among them. In Example 1, no three of the four employees can be selected without including a pair where one has a grievance against the other.