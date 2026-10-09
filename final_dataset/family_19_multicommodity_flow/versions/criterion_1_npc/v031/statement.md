# Problem A — Concurrent Packet Routing over a Shared Server Network

Time limit: 5 s   Memory limit: 256 MB

## Description
A telecommunications provider operates a directed network of servers connected by one-way fiber links. Each link has a strict ceiling on how many discrete data packets can traverse it per time window, regardless of what is being transmitted; this ceiling reflects the link's bandwidth and cannot be exceeded.

In the current window there are several distinct data streams to move. Each stream has its own source server, its own destination server, and a firm quantity — expressed in whole packets — that must be transmitted in full during this single window. Crucially, all streams draw on the **same** links: a link's ceiling applies to the combined packet count of every stream routed over it, so streams compete for the shared capacity even though they are otherwise independent. Packet counts are indivisible, so the number of packets of any given stream sent along any given link is a non-negative whole number.

Data is conserved at every server that is neither a stream's source nor its destination: for each stream separately, the packets of that stream entering an intermediate server must equal the packets of that stream leaving it. At a stream's source the net outflow of that stream equals its required quantity, and at its destination the net inflow equals that quantity. Latency, error correction, and link distances are outside the scope of this plan and should be ignored; only the per-link ceilings, the per-stream conservation, and the per-stream transmission quantities matter.

Produce a routing plan that transmits every stream's full quantity while respecting every link's shared ceiling, or determine that the network cannot carry all streams together in one window. (Routing any single stream alone may be trivial; the difficulty is that the streams must coexist on the shared links.)

## Input
Line 1: `n` `m` `k`. 
Next `k` lines: `s_i` `t_i` `d_i`. 
Next `m` lines: `u` `v` `cap` (directed link `u`->`v`).

## Output
`YES` then `k` lines, each with `m` integers — stream `i`'s packet count on link `j` (input order); or `NO`.

## Example

### Input
```text
4 5 2
1 4 1
2 3 1
1 2 1
1 3 1
2 4 1
3 4 1
2 3 1
```

### Output
```text
YES
1 0 1 0 0
0 0 0 0 1
```
