# Refinery Valve Configuration

Time limit: 2 s   Memory limit: 256 MB

## Description
A refinery network contains $n$ junctions connected by $m$ one-way pipes, currently configured to handle a single chemical extract. The control system must execute a transfer of exactly $d$ liters from the holding reservoir (junction $s$) to the cracking unit (junction $t$) during a single production cycle.

Each pipe connects a starting junction $u$ to an ending junction $v$ and has a physical diameter that imposes a strict upper limit of $cap$ liters per cycle. The flow routed through each pipe must be a non-negative integer. To prevent pressure buildup or cavitation, the total volume of extract entering any junction other than the reservoir and the cracking unit must exactly equal the total volume leaving it. The reservoir must have a net outflow (total leaving minus total entering) of exactly $d$, and the cracking unit must have a net inflow (total entering minus total leaving) of exactly $d$.

Determine if the network can support this exact transfer volume.

## Input
The first line contains three integers: $n$, $m$, and $1$ (indicating the single extract type).
The second line contains three integers: $s$, $t$, and $d$.
The next $m$ lines each contain three integers: $u$, $v$, and $cap$, describing a pipe from junction $u$ to junction $v$ with maximum capacity $cap$.

## Output
If the required transfer volume can be achieved, print `YES` on the first line. On the second line, print $m$ integers representing the flow assigned to each pipe, in the exact order the pipes were given in the input.
If the transfer volume cannot be achieved, print `NO`.

## Example

### Input
```text
4 5 1
1 4 10
1 2 10
1 3 5
2 3 5
2 4 5
3 4 10
```

### Output
```text
YES
5 5 0 5 5
```
