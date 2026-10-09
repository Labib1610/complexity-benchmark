# Problem A — Grid Maintenance Schedule

Time limit: 5 s
Memory limit: 256 MB

## Description
A utility provider operates a power grid made of facilities and interconnecting cables. The infrastructure is perfectly balanced: counting the cables attached to any given facility always yields the exact same total, regardless of which facility is checked.

Each cable must be deactivated for a single maintenance window. However, to maintain power stability, no facility can have more than one of its attached cables deactivated during the same window.

To finish the work as efficiently as possible, the provider restricts the total number of distinct maintenance windows used across the entire grid. This limit is set to precisely equal the number of cables attached to any single facility. 

You must determine if there is a valid way to assign each cable to a maintenance window without violating the stability rule at any facility.

## Input
The first line contains two integers $n$ and $m$ ($n$ is even, $m = 3n/2$, $2 \le n \le 2000$), representing the number of facilities and the number of cables. 
Each of the subsequent $m$ lines contains two integers $u$ and $v$ ($1 \le u < v \le n$), indicating that a cable connects facility $u$ and facility $v$.

## Output
If the maintenance can be scheduled under these rules, output `YES` on the first line. On the second line, output $m$ integers, each chosen from 1, 2, or 3, representing the maintenance window assigned to each cable, in the same order the cables are listed in the input. If no such schedule is possible, output `NO`.

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
