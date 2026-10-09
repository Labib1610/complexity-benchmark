# Problem A — Staggered Rotations

Time limit: 2 s   Memory limit: 256 MB

A manufacturing plant organizes its daily schedule into a Morning, Evening, and Night rotation (represented by the numbers 1, 2, and 3). The plant employs a workforce of technicians. Over time, various pairs of technicians have filed formal grievances against each other. To maintain productivity and avoid workplace incidents, management mandates that no two technicians who share a grievance may be assigned to the same daily rotation. Every technician must be placed into exactly one of the three available rotations. 

Determine if there is a valid rotation assignment for all technicians, and if so, provide one.

## Input
The first line contains two integers $n$ and $m$. The facility guarantees at least one technician is employed, and due to the limited number of 40 safety lockers on the assembly floor, the headcount $n$ never exceeds this capacity. The integer $m$ represents the number of formal grievances, which is non-negative and will not exceed the maximum possible number of distinct pairs among the $n$ technicians.

Each of the following $m$ lines contains two integers $u$ and $v$, indicating that technician $u$ and technician $v$ have a grievance against each other.

## Output
If no valid rotation schedule exists, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $s_1, s_2, \dots, s_n$ (each being 1, 2, or 3), where $s_i$ is the rotation assigned to the $i$-th technician. Any valid assignment is accepted.

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
