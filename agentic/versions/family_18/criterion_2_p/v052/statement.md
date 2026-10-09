# Problem B — Linear Slot Assignment for Hardware Integration

Time limit: 5 s
Memory limit: 256 MB

## Description
An engineering team is installing a system of $n$ hardware components. The installation site features a straight chassis with exactly $n$ mounting slots, numbered sequentially from $1$ to $n$. Each slot must house exactly one component.

The system relies on $m$ dedicated point-to-point data links, each permanently hardwired to a specific pair of components. The wiring is designed to ensure full communication capability without any redundancy: a signal can travel between any two components via some sequence of links, but cutting any single link would permanently isolate some components from others. Because of this strict minimal-connectivity design, the total number of links $m$ is always exactly $n - 1$.

When a link connects a component placed in slot $x$ and a component placed in slot $y$, the physical wire length required is $|x - y|$. Wires can run parallel to each other along the chassis without interference. The installation has a strict total wire budget of $B$, meaning the sum of the physical lengths of all $m$ wires cannot exceed $B$.

Determine an assignment of components to slots such that the total wire length is at most $B$, or determine that the budget is insufficient.

## Input
The first line provides three integers $n$, $m$, and $B$, representing the number of components, the number of links, and the maximum allowed total wire length.
Each of the following $m$ lines provides two integers $u$ and $v$ ($1 \le u, v \le n$), indicating that a link is hardwired between component $u$ and component $v$.

## Output
If a valid assignment exists, print `YES` on the first line. On the second line, print $n$ integers. The $i$-th integer must be the slot number (from $1$ to $n$) where component $i$ is installed. Every slot number from $1$ to $n$ must appear exactly once.
If no such assignment is possible, print `NO`.

## Example
### Input
```text
5 4 6
1 2
1 3
3 4
3 5
```

### Output
```text
YES
3 2 4 1 5
```
