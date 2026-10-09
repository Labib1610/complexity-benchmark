# Linear Array Assembly for Data Hubs

Time limit: 5 s
Memory limit: 256 MB

## Description
A facility must install a set of data processing units along a single straight track. The track has exactly as many mounting slots as there are units, spaced evenly. Each unit must be assigned to exactly one slot, and no slot can be left empty.

The units communicate through a dedicated reporting structure. Every unit, except for one primary receiver, transmits data directly to exactly one other unit. This ensures all units are ultimately connected in a single reporting framework without any redundant communication loops.

When unit $u$ is placed in slot $p_u$ and unit $v$ is placed in slot $p_v$, a communication cable must be installed between them. The length of this cable is exactly the number of slot intervals between them, which is $|p_u - p_v|$. 

The installation is constrained by a strict total copper allocation. The sum of the lengths of all installed cables must not exceed this allocation. You must determine if there is a valid assignment of units to slots that satisfies this total length restriction, and if so, provide one such assignment.

## Input
The first line contains three integers: the inventory of units $n$, the tally of connections $m$, and the total copper allocation $B$. Because every unit except the primary receiver requires exactly one uplink to establish the framework, the tally of connections is physically constrained to be exactly one less than the inventory of units.

The next $m$ lines each contain two integers $u$ and $v$, representing a direct reporting requirement between unit $u$ and unit $v$.

## Output
If the installation is possible within the copper allocation, print `YES` on the first line. 

On the second line, print exactly $n$ integers separated by spaces. The $i$-th integer must represent the slot position assigned to the $i$-th unit. The track's slots are numbered sequentially starting from 1 up to the total inventory of units. Because each unit requires its own slot, the output must be a sequence of distinct integers drawn exactly from these available slot numbers.

If it is impossible to meet the copper allocation, print `NO`.

## Example

### Input
```text
5 4 6
1 2
1 3
1 4
1 5
```

### Output
```text
YES
3 1 2 4 5
```
