# Problem B — Cascading Failsafes

Time limit: 1 s   Memory limit: 256 MB

## Description
A newly constructed control panel contains $n$ independent mechanical toggles. Each toggle operates in exactly one of two physical positions: active (1) or inactive (0).

To ensure safe operation, the engineers have programmed a set of $m$ failsafe rules. Each failsafe rule monitors exactly two specific toggle conditions. A condition is simply a requirement that a particular toggle must be in a specific position. A toggle being active is denoted by its positive index, while a toggle being inactive is denoted by its negative index. 

For a failsafe rule to be satisfied, the panel's current setup must match at least one of the two conditions monitored by that rule. If a toggle's state violates one of the conditions in a rule, the system mechanically forces the other condition in that rule to be met to prevent a critical failure. A single toggle might be monitored by many different failsafe rules.

Your objective is to find a complete layout for all $n$ toggles such that every single failsafe rule is satisfied simultaneously. If it is impossible to satisfy all rules without creating an unresolvable conflict, you must report that the system is unworkable.

## Input
The first line provides the number of toggles $n$ and the number of rules $m$. The panel's physical footprint guarantees at least 1 toggle and supports a maximum capacity of 100,000 toggles. The memory bank for the failsafes can store up to 200,000 rules, though it is possible for a panel to require none at all.

This is followed by $m$ lines. Each line defines a single failsafe rule using two non-zero integers $l_1$ and $l_2$. The magnitude of each integer identifies a specific toggle on the panel. A positive value $x$ means the rule monitors whether toggle $x$ is active, and a negative value $-x$ means the rule monitors whether toggle $x$ is inactive.

## Output
If no valid toggle layout can satisfy all failsafe rules, output a single line containing `NO`.
Otherwise, output `YES` on the first line. On the next line, output $n$ space-separated integers, each either 0 or 1, representing the state of each toggle (from 1 to $n$) in a valid layout. If there are multiple valid layouts, you may output any of them.

## Example 1
Input:
```
2 2
1 2
-1 -2
```
Output:
```
YES
1 0
```

## Example 2
Input:
```
1 2
1 1
-1 -1
```
Output:
```
NO
```
