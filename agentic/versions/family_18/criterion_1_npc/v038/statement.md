# Problem A — Linear Array Synchronization

Time limit: 5 s   Memory limit: 256 MB

## Description
A manufacturing facility is deploying a sequence of $n$ processing units along a single straight conveyor track. The track features exactly $n$ uniformly spaced mounting slots. Each processing unit must be assigned to exactly one slot, and every slot must contain exactly one unit. The slots are sequentially numbered from $1$ to $n$ along the track.

Certain pairs of processing units must synchronize their operations via direct fiber-optic cables. The facility's blueprint specifies $m$ such required connections. The track contains a dedicated cable trough that runs parallel to the slots. When a cable connects a unit in slot $x$ to a unit in slot $y$, the length of fiber-optic cable consumed is exactly $|x - y|$ meters. 

The facility has a strict materials budget of $B$ meters of fiber-optic cable in total. You must determine if there exists an assignment of units to slots such that the sum of the lengths of all $m$ required cables is at most $B$. 

To ensure structural integrity, your proposed assignment must satisfy the following conditions:
1. The physical distance spanned by any single cable must be strictly less than $n$ meters.
2. The absolute difference in slot numbers between any two units, whether they are connected by a cable or not, must be an integer.

If a valid configuration exists that meets all conditions and stays within budget, you must provide it. 

## Input
The first line contains three integers $n$, $m$, and $B$.
Each of the subsequent $m$ lines contains two integers $u$ and $v$, indicating that a fiber-optic cable must be installed between processing unit $u$ and processing unit $v$. 

## Output
If it is possible to assign all units to slots without exceeding the total cable budget $B$, print `YES` on the first line. On the second line, print $n$ integers separated by spaces, where the $i$-th integer represents the slot number (from $1$ to $n$) assigned to processing unit $i$. Every integer from $1$ to $n$ must appear exactly once.
If no such assignment is possible, print `NO`.

## Example 1
### Input
```
4 3 4
1 2
2 3
3 4
```
### Output
```
YES
1 2 3 4
```

## Example 2
### Input
```
3 3 2
1 2
2 3
3 1
```
### Output
```
NO
```
