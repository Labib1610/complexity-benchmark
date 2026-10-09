# Problem A — Automated Payload Routing

Time limit: 5 s
Memory limit: 256 MB

## Description
An industrial facility transfers materials using a system of directed pressure conduits connecting various junctions. During each operational cycle, the system must handle several simultaneous transfer orders.

Each order requires moving a specific, indivisible number of payloads from an injection junction to an extraction junction. You must determine how many payloads belonging to each order will travel through each conduit.

The system is strictly governed by the following operational constraints:
- **Thresholds**: Each conduit has a strict physical limit on the total number of payloads it can carry per cycle. This limit is evaluated by summing the payloads across all orders that utilize the conduit.
- **Continuity**: Payloads are discrete and cannot be stored or consumed. For any specific order, if a junction is neither the injection nor the extraction point for that order, the count of entering payloads for that order must exactly equal the count of leaving payloads for that order.
- **Fulfillment**: For a specific order, at its injection junction, the count of departing payloads for that order minus the count of arriving payloads for that order must exactly equal the required order size. At its extraction junction, the count of arriving payloads for that order minus the count of departing payloads for that order must exactly equal the order size.
- **Integrity**: Every assigned payload count on a conduit must be a non-negative integer.

Determine if a routing configuration exists that satisfies all transfer orders without violating any conduit thresholds. If it does, provide the detailed payload assignments.

## Input
The first line contains three integers $n$, $m$, and $k$: the number of junctions, the number of pressure conduits, and the number of transfer orders.
The next $k$ lines each contain three integers $s_i$, $t_i$, and $d_i$, representing the injection junction, extraction junction, and the exact number of payloads required for order $i$.
The next $m$ lines each contain three integers $u$, $v$, and $cap$, representing a conduit operating from junction $u$ to junction $v$ with a maximum threshold of $cap$ payloads.

## Output
If a valid configuration exists, output `YES` on the first line. Then, output $k$ lines, each containing $m$ integers. On the $i$-th line, the $j$-th integer must represent the number of payloads from order $i$ assigned to the $j$-th conduit (following the exact order the conduits appear in the input).
If no such configuration is possible, output `NO`.

## Example

### Input
```
4 5 2
1 4 2
2 3 1
1 2 2
2 4 1
1 3 1
3 4 2
2 3 1
```

### Output
```
YES
1 1 1 1 0
0 0 0 0 1
```
