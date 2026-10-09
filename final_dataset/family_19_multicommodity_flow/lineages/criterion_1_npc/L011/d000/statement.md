# Problem A — Intermodal Rail Network Routing

Time limit: 5 s   Memory limit: 256 MB

## Description
A logistics operator manages a network of $n$ terminals connected by $m$ one-way rail segments. Each segment has a strict daily limit on the total number of train cars it can handle, regardless of their contents. This limit is due to track signaling and cannot be exceeded.

The operator has signed $k$ client contracts for the day. Each contract specifies an origin terminal, a destination terminal, and a fixed number of cars that must be delivered. All cars from all contracts run on the same track infrastructure. The total number of cars—summed across all contracts—passing through any single rail segment cannot exceed that segment's daily limit. 

Train cars cannot be split or partially routed; the number of cars assigned to any segment for any contract must be a non-negative whole number. At any terminal, unless it is a contract's origin or destination, the number of cars for that specific contract arriving must exactly equal the number of cars for that contract departing. For a contract's origin, the number of departing cars minus arriving cars must equal the contracted amount. For the destination, arriving minus departing must equal the contracted amount.

Determine if there is a routing plan that satisfies all contracts simultaneously without exceeding any rail segment's limit. If possible, provide the exact number of cars from each contract to route over each segment.

## Input
The first line contains three integers $n$, $m$, and $k$, representing the number of terminals, rail segments, and client contracts.
The next $k$ lines each contain three integers $s_i$, $t_i$, and $d_i$, representing the origin terminal, destination terminal, and the fixed number of train cars required for contract $i$.
The final $m$ lines each contain three integers $u_j$, $v_j$, and $c_j$, representing a one-way rail segment from terminal $u_j$ to terminal $v_j$ with a daily limit of $c_j$ cars.

## Output
If no valid routing plan exists, output `NO`.
Otherwise, output `YES` on the first line. Then, output $k$ lines. The $i$-th of these lines must contain $m$ space-separated integers, where the $j$-th integer represents the number of train cars from contract $i$ routed over the $j$-th rail segment (following the exact order the segments were provided in the input).

## Example

### Input
```
4 5 2
1 4 2
1 3 1
1 2 2
2 4 2
1 3 2
3 4 2
2 3 1
```

### Output
```
YES
2 2 0 0 0
0 0 1 0 0
```
