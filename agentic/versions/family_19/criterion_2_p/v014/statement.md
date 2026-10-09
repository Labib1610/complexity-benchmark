# Problem B — Freight Routing Over a Transit Network

Time limit: 2 s
Memory limit: 256 MB

## Description
A logistics coordinator must transfer a specific target volume of cargo across a network of waystations connected by one-way transit corridors. All cargo consists of indivisible units. The transfer must occur from a single starting waystation to a single target waystation.

Each transit corridor has a physical size limit, provided in the network manifest, which restricts how much cargo it can handle. A corridor cannot move cargo in reverse, meaning the minimum number of cargo units it can carry is a complete absence of units. Furthermore, the number of units assigned must not overflow the corridor's physical size limit.

Waystations (except for the starting and target ones) have absolutely no storage space. Consequently, the total volume of cargo entering any intermediate waystation must exactly match the total volume leaving it. At the starting waystation, the volume of cargo departing minus the volume arriving must exactly equal the target volume. Conversely, at the target waystation, the volume arriving minus the volume departing must equal the target volume.

You must determine a valid allocation of cargo across the corridors that successfully transfers the target volume under these physical constraints, or determine that it is impossible.

## Input
The first line contains three integers: $n$ (the number of waystations), $m$ (the number of transit corridors), and the number $1$ (indicating a single cargo type).
The second line contains three integers: $s$ (the starting waystation), $t$ (the target waystation), and $d$ (the target volume of cargo to transfer).
The next $m$ lines each contain three integers: $u$, $v$, and $cap$, representing a one-way transit corridor from waystation $u$ to waystation $v$ with a physical size limit of $cap$.
Waystations are numbered from $1$ to $n$.

## Output
If a valid allocation exists, print `YES` on the first line. On the second line, print $m$ integers separated by spaces, where the $j$-th integer is the volume of cargo assigned to the $j$-th corridor (in the order they appear in the input).
If no such allocation is possible, print `NO`.

## Example

### Input
```text
4 5 1
1 4 10
1 2 5
1 3 10
2 3 5
2 4 5
3 4 5
```

### Output
```text
YES
5 5 0 5 5
```
