# Problem B — Hazardous Incompatibility

Time limit: 2 s   Memory limit: 256 MB

## Description
A manufacturing plant operates a series of vats joined by transfer pipes. Each pipe has a designated shut-off expense, representing the cost of materials required to permanently block it. 

Two designated vats contain highly reactive substances. To guarantee safety, these two substances must never be able to mix: after modifications, there must be no sequence of open pipes that allows fluid to travel between the two designated vats, in either direction. A pipe, once blocked, allows zero fluid transfer.

The structural arrangement of the remaining vats does not matter, and they can remain accessible to either of the two designated vats. The only metric of concern is the total shut-off expense, which is the sum of the expenses of the pipes chosen to be blocked. The plant has a strict financial allowance that this total must not exceed.

Determine a set of pipes to block such that the total expense is within the allowance and the two designated vats can no longer exchange fluid, or state that no such affordable set of pipes exists.

## Input
Line 1: five integers $n$, $m$, $s$, $t$, $B$. 
Next $m$ lines: three integers $u$ $v$ $w$ — a pipe between vat $u$ and vat $v$ with a shut-off expense of $w$.

## Output
`YES`, then a line with the number $c$ of blocked pipes, then $c$ lines `u v`; or `NO`.

## Example
### Input
```
4 5 1 4 10
1 2 4
1 3 5
2 3 2
2 4 5
3 4 4
```
### Output
```
YES
2
1 2
1 3
```
