# Problem A — Server Cabinet Cabling

Time limit: 5 s   Memory limit: 256 MB

## Description
A new data center cabinet is being commissioned, and its servers must be installed along a single vertical rack. The rack is divided into a fixed number of consecutive slots, exactly one server per slot, and every server ends up in some slot; there are precisely as many slots as servers, so the installation is a one-to-one placement of servers onto slot positions numbered along the rack.

The servers exchange data over point-to-point patch cables. Whenever two servers must exchange data, a cable is run between their slots through the rack's vertical routing channel. Because the channel runs the length of the rack, the physical length of a cable is determined solely by how many slot positions separate the two servers it connects — adjacent slots cost one unit of cable, slots two apart cost two units, and so on. The specific routing hardware, connector types, and data directions are immaterial to this calculation; only the separation in slots matters.

Procurement has fixed a **total** cabling budget for the job: summed over every required patch cable, the combined cable length must not exceed the given budget. There is no per-cable limit and no limit on how many cables share the channel — the only constraint that binds is the grand total.

Decide whether the servers can be placed one-per-slot so that the total cable length over all required connections stays within the budget, and if so output a placement; otherwise report that no placement fits the budget. (A placement that is excellent for some connections may overshoot the total because of others, so local good choices do not guarantee a feasible total.)

## Input
First line: three integers n, m, B. Each of the next m lines: two integers u v — a required connection between servers u and v.

## Output
Print `YES` then a line with n integers — the slot position (1..n, a permutation) of server 1,2,...,n — such that the total length is <= B. Otherwise print `NO`.

## Example
### Input
```
4 4 6
1 2
2 3
3 4
4 1
```

### Output
```
YES
1 2 4 3
```
