# Problem A — Data Stream Routing

Time limit: 5 s   Memory limit: 256 MB

## Description
A computer network consists of several routers connected by directed communication links. Each link has a strict hardware transmission limit dictating the maximum number of data packets it can process. This limit applies to the combined traffic from all sources passing through the link.

There are several distinct data streams that need to be delivered. Each stream is defined by a specific source router where the data originates, a specific destination router where the data is required, and an exact payload size measured in packets. All streams are transmitted simultaneously. A link's transmission limit restricts the combined number of packets from all streams routed through it, meaning different streams compete for the same network resources. Packets cannot be fragmented, so the number of packets from any stream traversing a given link is a non-negative whole number.

Packets must continuously traverse the network without being buffered indefinitely. For any router that is neither a stream's source nor its destination, every packet belonging to that stream which arrives at the router must subsequently be forwarded out of it. At a stream's source router, the net outward transmission (packets sent out minus any packets of the same stream that happen to arrive) must perfectly account for the stream's entire payload. At the destination router, the net inward reception (packets arriving minus any packets forwarded away) must perfectly account for the payload.

Determine a routing configuration that successfully delivers every stream's full payload to its respective destination without exceeding the hardware transmission limit of any communication link. If it is impossible to route all streams together under these shared limits, you must report this.

## Input
The first line contains three integers: $n$ (number of routers), $m$ (number of links), and $k$ (number of data streams).
The next $k$ lines each contain three integers: $s_i$ (source router for stream $i$), $t_i$ (destination router for stream $i$), and $d_i$ (payload size in packets for stream $i$).
The next $m$ lines each contain three integers: $u$, $v$, and $cap$, representing a directed link from router $u$ to router $v$ that can transmit at most $cap$ packets in total.

## Output
If a valid routing configuration exists, print `YES` on the first line. Then, print $k$ lines, each containing $m$ integers. The $j$-th integer on the $i$-th line must be the number of packets from data stream $i$ traversing link $j$ (where links are indexed 1 to $m$ in the order they appear in the input). 
If no such configuration is possible, print `NO`.

## Example

**Input:**
```
4 5 2
1 4 10
2 3 5
1 2 10
2 4 10
1 3 10
3 4 10
2 3 5
```

**Output:**
```
YES
5 5 5 5 0
0 0 0 0 5
```
