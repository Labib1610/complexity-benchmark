# Combinatorial Load Balancing over Directed Networks

Time limit: 2 s
Memory limit: 256 MB

## Description
A complex logistics network is composed of $n$ facilities and $m$ directed transmission channels. Each channel $j$ has an operational upper bound $c_j$. An allocation strategy is a vector of $m$ non-negative integers representing the load on each channel. Finding a valid allocation strategy requires navigating a massive state space: since each channel can independently carry any integer load between $0$ and $c_j$, the total number of possible configurations is $\prod_{j=1}^m (c_j + 1)$. The vast majority of these configurations are invalid because they violate strict structural constraints at the facilities. A brute-force enumeration of this space is computationally infeasible for large networks.

Specifically, for any facility $x$, the total load on incoming channels must perfectly match the total load on outgoing channels, ensuring no material is created or destroyed. The only exceptions are two special facilities: an injection point $s$ and an extraction point $t$. The network is tasked with processing a total demand $d$. Thus, the net load departing $s$ (outgoing minus incoming) must equal exactly $d$, and the net load arriving at $t$ (incoming minus outgoing) must also equal exactly $d$.

You are given the network topology, the bounds for each channel, and the demand $d$. The number of distinct product varieties being routed is exactly 1, meaning the entire configuration only needs to track a single uniform resource. You must determine if there exists at least one configuration in the state space that satisfies all operational bounds and conservation laws simultaneously. If such a configuration exists, you must output it.

## Input
The first line contains three integers: $n$, $m$, and the number of product varieties (always 1).
The second line contains three integers: $s$, $t$, and $d$.
The next $m$ lines each contain three integers $u$, $v$, and $c$, indicating a directed channel from facility $u$ to facility $v$ with operational upper bound $c$.

## Output
If a valid configuration exists, print `YES` on the first line, followed by a second line containing $m$ space-separated integers representing the load on each channel (in the same order the channels were given in the input). If multiple valid configurations exist, you may output any of them. If no such configuration exists, print `NO`.

## Example

**Input**
```text
4 5 1
1 4 10
1 2 10
1 3 5
2 3 5
2 4 5
3 4 10
```

**Output**
```text
YES
5 5 0 5 5
```
