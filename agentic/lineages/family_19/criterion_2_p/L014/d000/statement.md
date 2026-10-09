# Volume Routing Protocol

Time limit: 2 s   Memory limit: 256 MB

## Description
A distribution network consists of a series of junctions connected by one-way conduits. Each conduit has a strict upper limit on the number of discrete units it can transfer during an operational cycle. 

An order requires moving a specific target volume of identical resource units from a designated starting junction to a designated ending junction. Because all units being moved are completely interchangeable, any unit arriving at an intermediate junction can be forwarded along any outgoing conduit. There are no competing orders or different types of resources sharing the network; every unit in the system originates at the starting junction and is intended for the ending junction.

During the cycle, the number of units routed through any conduit must be a non-negative integer that does not exceed its upper limit. At every junction except the starting and ending ones, the total number of incoming units must exactly equal the total number of outgoing units. At the starting junction, the total outgoing units minus the total incoming units must equal the target volume. At the ending junction, the total incoming units minus the total outgoing units must equal the target volume.

Determine a valid assignment of units to each conduit that successfully routes the entire target volume in a single cycle, or determine that this target volume cannot be accommodated.

## Input
The first line contains three integers: $n$ (the number of junctions), $m$ (the number of conduits), and $1$ (indicating the number of active orders).
The second line contains three integers: $s$ (the starting junction), $t$ (the ending junction), and $d$ (the target volume).
The next $m$ lines each contain three integers $u$, $v$, and $cap$, representing a one-way conduit from junction $u$ to junction $v$ with an upper limit of $cap$ units.

## Output
If the target volume can be routed, print `YES` on the first line. On the second line, print $m$ integers separated by spaces, representing the number of units assigned to each conduit in the exact order they were provided in the input. If it is impossible, print `NO`.

### Example

**Input**
```text
4 5 1
1 4 10
1 2 10
2 4 5
1 3 5
3 4 5
2 3 5
```

**Output**
```text
YES
5 5 5 5 0
```
