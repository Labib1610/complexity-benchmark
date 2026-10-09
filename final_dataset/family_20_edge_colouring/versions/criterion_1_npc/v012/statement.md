# Problem A — Rotating Maintenance Windows on the Trunk Grid

Time limit: 5 s   Memory limit: 256 MB

## Description
A utility company is scheduling maintenance for its trunk grid, which consists of splice points and the cables connecting them. The architecture of the grid ensures a strict local topology: at any splice point, a technician disconnecting cables one by one will perform exactly three disconnections before the point is completely isolated from the rest of the grid.

The global maintenance schedule is limited to exactly three rotating windows (labelled 1, 2, and 3). When a cable undergoes maintenance, it is taken offline for the entirety of its assigned window. 

To maintain structural continuity, safety rules dictate that no two cables meeting at the same splice point may be taken offline during the same window. The physical properties of the cables do not affect the schedule. The sole requirement is to allocate one of the three global windows to each cable such that the continuity rule is respected everywhere. 

You must determine if such a schedule is possible. If it is, provide the window assignment for each cable.

## Input
The first line contains two integers $n$ and $m$ ($n$ is even, $m = 3n/2$, $2 \le n \le 2000$), representing the number of splice points and the total number of cables.
Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u < v \le n$), indicating that a cable connects splice point $u$ and splice point $v$.

## Output
If a valid maintenance schedule can be formed, print `YES` on the first line. On the second line, output $m$ integers from the set {1, 2, 3}, representing the maintenance window assigned to each cable in the order they appear in the input. If multiple schedules are valid, output any of them.
If no such schedule is possible, print `NO`.

## Example
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
YES
1 2 3 3 2 1
```
