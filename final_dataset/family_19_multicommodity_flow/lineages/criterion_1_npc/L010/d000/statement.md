# Problem A — Cloud Fabric Stream Allocation

Time limit: 5 s
Memory limit: 256 MB

## Description
A modern cloud fabric consists of `n` routing switches connected by `m` directed optical links. To ensure predictable latency, the fabric uses a synchronous transmission cycle. During each cycle, each link can transmit a strict maximum of `cap` discrete data blocks.

The fabric is currently tasked with serving `k` independent data streams. Each stream `i` requires exactly `d_i` data blocks to be routed from its ingress switch `s_i` to its egress switch `t_i` during the cycle. 

Because the data blocks for all streams are completely standardized and uniform in size, they share the optical links seamlessly. The capacity limit on any link applies to the sum of all blocks from all streams utilizing that link. Despite this shared infrastructure, blocks from different streams remain distinct and must be delivered to their respective egress switches. 

The routing must satisfy standard conservation rules:
- For every stream, the number of its blocks entering any intermediate switch (which is neither its ingress nor its egress) must exactly equal the number of its blocks leaving that switch.
- At the ingress switch for a stream, the net outgoing number of blocks for that stream must be exactly `d_i`.
- At the egress switch for a stream, the net incoming number of blocks for that stream must be exactly `d_i`.
- Blocks are indivisible entities; therefore, the number of blocks assigned to any stream on any link must be a non-negative integer.

Given the uniform nature of the data blocks and the strictly integer capacities of the optical links, the network possesses a highly regular, homogeneous structure. Your task is to determine whether all `k` streams can be successfully routed in a single cycle without exceeding any link's shared capacity. If such a routing is possible, you must also provide the specific block assignments.

## Input
The first line contains three integers: `n`, `m`, and `k`.
The next `k` lines each contain three integers `s_i`, `t_i`, and `d_i`, representing the ingress switch, egress switch, and the required number of blocks for stream `i`.
The next `m` lines each contain three integers `u`, `v`, and `cap`, representing a directed optical link from switch `u` to switch `v` with a maximum capacity of `cap` blocks per cycle.

## Output
If the routing is possible, print `YES` on the first line. Then, print `k` lines. The `i`-th of these lines should contain `m` space-separated integers, representing the number of blocks of stream `i` routed along each of the `m` links (in the exact order the links were given in the input).
If it is impossible to route all streams together, print `NO`.

## Example

**Input:**
```
4 5 2
1 4 1
2 3 1
1 2 1
1 3 1
2 4 1
3 4 1
2 3 1
```

**Output:**
```
YES
1 0 1 0 0
0 0 0 0 1
```
