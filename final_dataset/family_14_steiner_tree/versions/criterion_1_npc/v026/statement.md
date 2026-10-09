# Problem A — Phase II: Link Synthesis

Time limit: 5 s
Memory limit: 256 MB

## Description

The overall mission objective is to exfiltrate encrypted ledgers from a segmented corporate intranet. The operation is strictly divided into three sequential phases:

**Phase I: Target Acquisition**
Reconnaissance algorithms have mapped the intranet, which consists of **n** distinct hardware systems (numbered 1 to **n**). The algorithms have successfully isolated **t** critical systems that contain the fragmented ledger data. The output of this phase is provided to you.

**Phase II: Link Synthesis (Your Task)**
To synchronize and decrypt the fragmented ledgers, all **t** critical systems must be capable of exchanging data with each other over a single, continuous communication channel. Intelligence has provided a list of **m** available bidirectional exploits. Each exploit bridges a specific pair of systems and carries a quantified risk cost. 

Your objective is to select a subset of these exploits such that every critical system is linked into the same unified network (either directly or by hopping through intermediate systems). The total risk cost of your selection is the sum of the risk costs of the chosen exploits. You may freely route the channel through any of the remaining non-critical systems if doing so lowers the total risk cost. You must calculate the minimum possible total risk cost to establish this unified channel.

**Phase III: Payload Deployment**
Once the optimal topology is determined, an automated extraction payload will be broadcast across the synthesized links. You do not need to simulate or plan this deployment; your software is only responsible for calculating the minimum cost required by Phase II.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers: the ids of the critical systems identified in Phase I.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), indicating that an exploit can bridge system u and system v at a risk cost of w.
It is guaranteed that the available exploits are sufficient to link all critical systems.

## Output

Print a single integer: the minimum total risk cost to establish a unified channel among all critical systems.

## Examples

### Example 1

**Input**
```
4 6 3
1 2 3
1 4 1
2 4 1
3 4 1
1 2 2
2 3 2
1 3 2
```

**Output**
```
3
```

### Example 2

**Input**
```
4 4 3
1 2 3
1 2 1
2 3 1
1 4 10
3 4 10
```

**Output**
```
2
```

### Example 3

**Input**
```
3 2 1
1
1 2 5
2 3 5
```

**Output**
```
0
```

## Note

In Example 1, synthesizing the links through the non-critical system 4 (which incurs a total risk cost of 1+1+1 = 3) is less risky than linking the three critical systems directly to each other (which would incur a cost of 4). 

In Example 3, Phase I only identified a single critical system. Since it does not need to communicate with any other critical system to synchronize data, Phase II requires no exploits, resulting in a total risk cost of 0.
