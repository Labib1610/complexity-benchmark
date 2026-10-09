# Problem A — Pneumatic Tube Network Allocation

Time limit: 5 s   Memory limit: 256 MB

## Description
A hospital relies on an automated pneumatic tube network to transport medical supplies between stations. The network consists of one-way tube segments connecting various stations. Each tube segment operates with a strict mechanical limit on the total number of capsules it can transport during a standard operating window. This limit applies to the combined sum of all capsules routed through the segment, regardless of which department sent them.

During the upcoming window, several departments have urgent transport requests. Each request specifies a starting station, a receiving station, and an exact number of capsules that must be delivered. Capsules are indivisible physical objects, so the number of capsules assigned to any segment must be a non-negative whole number.

Stations cannot store capsules. Therefore, for each individual request, any station that is neither its starting nor receiving point must immediately forward all arriving capsules for that request; the number of arriving capsules for a specific request must exactly equal the number departing. At a request's starting station, the outgoing capsules minus any incoming capsules for that request must equal the required delivery amount. Similarly, at the receiving station, the net incoming capsules (incoming minus outgoing) for that request must equal the required amount.

Determine if there is a routing plan that fulfills all department requests simultaneously without exceeding the mechanical limit of any tube segment. If such a plan exists, you must specify how many capsules from each request are routed through each tube segment.

## Input
The first line contains three integers $n$, $m$, and $k$: the number of stations, the number of one-way tube segments, and the number of transport requests.
The next $k$ lines each contain three integers $s_i$, $t_i$, and $d_i$, representing the starting station, receiving station, and the exact number of capsules required for request $i$.
The next $m$ lines each contain three integers $u$, $v$, and $cap$, representing a one-way tube segment from station $u$ to station $v$ with a mechanical limit of $cap$ capsules.

## Output
If a valid routing plan exists, print `YES` on the first line. Following this, print $k$ lines, each containing $m$ integers. The $j$-th integer on the $i$-th line must represent the number of capsules from request $i$ routed through the $j$-th tube segment (in the exact order the segments were given in the input).
If no such plan can be formed, print `NO`.

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
