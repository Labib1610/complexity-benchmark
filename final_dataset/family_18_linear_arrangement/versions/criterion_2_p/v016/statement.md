# Problem B — Linear Slot Assignment for a Connected Facility

Time limit: 5 s
Memory limit: 256 MB

## Description
A monitoring installation places its units along a single straight line of mounting slots. There is exactly one unit per slot, and the number of slots equals the number of units. This forms a one-to-one placement of units onto positions numbered $1$ to $n$ along the line. 

The units communicate through reporting links. Each link is carried by a cable whose length is determined entirely by the physical distance between the two units it connects. Specifically, if a link connects a unit at slot $p_u$ and a unit at slot $p_v$, the length of the cable required is $|p_u - p_v|$. The connector details and the direction of reporting do not affect this length. 

The installation has a single total cabling budget $B$ that covers the sum of the lengths of all cables used. There is no individual cap on the length of any single cable, and multiple cables can share the same physical space along the slots.

You must find a one-to-one placement of the $n$ units onto the $n$ slots such that the total length of all cables is at most $B$. If no such placement is possible within the budget, you must report that it cannot be met.

## Input
The first line contains three integers $n$, $m$, and $B$, representing the number of units, the number of reporting links, and the total cabling budget, respectively.
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that a reporting link exists between unit $u$ and unit $v$.

To ensure standardized topography, the input is guaranteed to satisfy the following structural constraints:
1. The network of links connects all $n$ units together into a single unified whole (a path of links exists between any two units).
2. The total number of links $m$ is strictly less than $n$.
3. If you count the number of direct links attached to each unit and sum these counts across all $n$ units, the total is exactly $2n - 2$.
4. The units can be partitioned into two disjoint groups such that every reporting link connects a unit from the first group to a unit from the second group.

## Output
If there is a valid placement whose total cable length is at most $B$, print `YES` on the first line. On the second line, print $n$ integers representing the assigned slot positions (a permutation of the numbers from $1$ to $n$) for units $1, 2, \dots, n$ respectively.
If the budget cannot be met, print `NO`.

## Example

### Input
```text
5 4 5
1 2
1 3
3 4
3 5
```

### Output
```text
YES
2 1 3 4 5
```
