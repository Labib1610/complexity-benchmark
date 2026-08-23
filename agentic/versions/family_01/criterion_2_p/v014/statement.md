# Factory Schedules

Time limit: 1 s   Memory limit: 256 MB

The factory is transitioning to a dual-schedule framework. Every staff member must be assigned to exactly one of two operational periods: the morning period (labeled 1) or the evening period (labeled 2).

The HR department maintains a list of interpersonal grievances. Each grievance involves a pair of staff members who cannot work during the same period. Your task is to determine whether it is possible to assign every staff member to a period such that no two individuals involved in a mutual grievance share the same period.

If there are multiple valid assignments, you must choose the one that results in the lexicographically smallest sequence of period labels when ordered by the staff members' ID numbers (from 1 to $n$).

## Input
The first line provides two integers, $n$ and $m$. The company guarantees at least one staff member is employed, but the total headcount $n$ cannot exceed the facility's maximum capacity of two hundred thousand personnel. The grievance log contains $m$ entries; it may be completely empty, or it could be full up to its strict maximum limit of two hundred thousand records.
Each of the subsequent $m$ lines contains two integers $u$ and $v$, representing a pair of staff members who have a grievance against each other.

## Output
If there is no way to assign the periods without violating the grievance constraints, output a single line containing `NO`.
Otherwise, output `YES` on the first line. On the second line, output $n$ integers separated by spaces, where the $i$-th integer is the period (1 or 2) assigned to the staff member with ID $i$. This sequence must be the lexicographically smallest valid assignment.

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
