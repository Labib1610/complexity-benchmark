# Problem B — Facility Allocation

Time limit: 1 s
Memory limit: 256 MB

A corporation is distributing its $n$ employees between two separate production facilities, designated as Facility 1 and Facility 2. 

The HR department has identified $m$ compatibility issues. Each issue involves a specific pair of employees who have a history of conflict. To maintain productivity, any two employees involved in a shared compatibility issue must be placed in different facilities. 

To guarantee that the management system can process the data, the dataset satisfies the following structural properties:
1. The sum of the number of conflicts each employee is involved in, taken over all $n$ employees, is exactly $2m$.
2. If we group employees such that any two employees connected by a chain of conflicts are in the same group, the total number of these independent groups (including employees with zero conflicts) is at least $n - m$.

Your task is to determine if it is possible to assign every employee to either Facility 1 or Facility 2 without violating the compatibility restrictions. If it is possible, you must provide the assignment. If multiple valid assignments exist, you must provide the one that is lexicographically smallest when the assignment is represented as a sequence of facility numbers (1s and 2s) for employees $1$ through $n$.

## Input
The first line contains two integers $n$ and $m$ ($1 \le n \le 2\cdot 10^5$, $0 \le m \le 2\cdot 10^5$).
The following $m$ lines each contain two integers $u$ and $v$, representing a compatibility issue between employee $u$ and employee $v$.

## Output
If there is no way to assign the employees to the two facilities under the given rules, output a single line containing `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers separated by spaces, where the $i$-th integer is the facility number (1 or 2) assigned to employee $i$. This sequence must be the lexicographically smallest valid assignment.

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
