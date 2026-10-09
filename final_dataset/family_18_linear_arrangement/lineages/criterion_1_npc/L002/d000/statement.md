# Problem A — Backbone Trenching for the Control Vault

Time limit: 5 s   Memory limit: 256 MB

## Description
A facility is installing $n$ interconnected hardware units. These units must be mounted into a single continuous row of $n$ slots. Each slot holds exactly one unit, and every unit must be assigned a slot. The slots are numbered sequentially from 1 to $n$.

Certain pairs of units must communicate. For every required communication link between two units, a physical wire is laid in a shared conduit that runs parallel to the slots. The length of the wire required for a single link is calculated as the absolute difference between the slot numbers where the two communicating units are mounted. For example, if two units are placed in slot 2 and slot 5, the wire length for their link is 3.

The facility has a maximum allowance $B$ for the aggregate length of all wires used. The number of wires running through any part of the conduit is not restricted; the only limitation is the sum of the lengths of all individual communication wires.

Determine if there is a valid slot assignment for all $n$ units such that the combined length of all necessary wires is at most $B$. If such an assignment exists, provide it.

## Input
The first line contains three integers $n$, $m$, and $B$ — the number of hardware units, the number of communication links, and the maximum total wire length, respectively.
The following $m$ lines each contain two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that a communication wire must connect unit $u$ and unit $v$.

## Output
If there is a valid assignment that meets the budget, print `YES` on the first line. On the second line, print $n$ integers separated by spaces, where the $i$-th integer represents the slot number (from 1 to $n$) assigned to unit $i$. Every slot number from 1 to $n$ must appear exactly once.
If no such assignment is possible, print `NO`.

## Example

**Input:**
```
4 3 3
1 2
2 3
3 4
```

**Output:**
```
YES
1 2 3 4
```
