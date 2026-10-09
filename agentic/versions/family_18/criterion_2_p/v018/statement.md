# Problem B — Backbone Trenching for a Reporting Hierarchy

Time limit: 5 s
Memory limit: 256 MB

## Description
At a monitoring facility, hardware units must be installed into a linear chassis. The chassis contains exactly $n$ mounting slots, numbered sequentially from $1$ to $n$. Every unit must be assigned to exactly one slot, such that all slots are occupied.

The facility's operations rely on a specific reporting structure among the units. This structure consists of $m$ direct communication links between pairs of units. The connections are organized such that all units are linked together without any closed loops, meaning every unit (except for a single top-level unit) reports directly to exactly one superior.

To establish these links, a cable is run between the slots of each connected pair. The length of cable consumed by a single link is exactly the number of slot positions separating the two units (i.e., the absolute difference of their assigned slot numbers). The facility has been allocated a total cabling budget of $B$ to cover all $m$ links combined. There is no cap on the length of any individual cable, and multiple cables may run parallel along the chassis without interference.

You must evaluate whether the units can be assigned to the slots in a way that respects the overall cabling budget. If a valid configuration exists whose total cable usage is at most $B$, you must find it.

## Input
The first line contains three integers $n$, $m$, and $B$.
Each of the next $m$ lines contains two integers $u$ and $v$, representing a reporting link between unit $u$ and unit $v$. (It is guaranteed that $m = n - 1$ and the links form the structure described).

## Output
If the total cable length can be kept within the budget $B$, print `YES` on the first line. On the second line, print $n$ integers representing a valid placement, where the $i$-th integer is the slot position (from $1$ to $n$) assigned to unit $i$. If there are multiple valid placements, any will be accepted. If it is impossible to satisfy the budget, print `NO`.

## Examples

**Input 1:**
```
5 4 5
1 2
1 3
3 4
3 5
```

**Output 1:**
```
YES
2 1 4 3 5
```

**Input 2:**
```
5 4 4
1 2
1 3
3 4
3 5
```

**Output 2:**
```
NO
```
