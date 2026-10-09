# Problem A — Simultaneous Logistics Manifest

Time limit: 5 s   Memory limit: 256 MB

## Description
A logistics company manages a system of $n$ distribution centers connected by $m$ one-way transit corridors. Each corridor has a strict structural limit on the total number of containers it can process during a single shift.

During the current shift, there are $k$ distinct client contracts to fulfill. Contract $i$ requires exactly $d_i$ whole containers of a specific product to be transferred from a production center $s_i$ to a fulfillment center $t_i$. 

Because the corridors are shared infrastructure, products from different contracts compete for the same space. The combined number of containers (across all $k$ contracts) traversing any single corridor must not exceed that corridor's structural limit. Containers are indivisible physical units, so the number of containers of any product on any corridor must be a non-negative integer.

For each individual contract, any distribution center that is neither its production center $s_i$ nor its fulfillment center $t_i$ acts purely as a pass-through: the total number of containers for that contract arriving at the center must exactly equal the total number departing from it. At the production center $s_i$, the number of departing containers for contract $i$ minus the arriving containers for contract $i$ must exactly equal $d_i$. At the fulfillment center $t_i$, the arriving containers for contract $i$ minus the departing containers for contract $i$ must exactly equal $d_i$.

Determine if there is a valid assignment of containers to corridors for all contracts that meets all requirements and structural limits simultaneously. If such an assignment exists, provide the detailed manifest.

## Input
The first line contains three integers $n$, $m$, and $k$.
The next $k$ lines each contain three integers $s_i$, $t_i$, and $d_i$, specifying the production center, fulfillment center, and required number of containers for contract $i$.
The next $m$ lines each contain three integers $u$, $v$, and $cap$, representing a one-way corridor from center $u$ to center $v$ with a structural limit of $cap$ containers.

## Output
If all contracts can be fulfilled simultaneously, output `YES` on the first line. Then, output $k$ lines. The $i$-th of these lines should contain $m$ integers, representing the number of containers for contract $i$ assigned to each of the $m$ corridors, in the exact order the corridors appeared in the input. If there are multiple valid manifests, you may output any of them.
If it is impossible to fulfill all contracts without exceeding the structural limits, output `NO`.

## Example 1

**Input:**
```text
4 4 2
1 4 1
2 3 1
1 2 1
2 3 1
3 4 2
1 3 1
```

**Output:**
```text
YES
0 0 1 1
0 1 0 0
```

## Example 2

**Input:**
```text
4 4 2
1 4 2
2 3 1
1 2 1
2 3 1
3 4 2
1 3 1
```

**Output:**
```text
NO
```
