# Problem A — Network Provisioning

Time limit: 5 s   Memory limit: 256 MB

## Description

A distributed computing system contains **n** processing nodes (numbered 1 through **n**). A designated group of **t** core controllers must be fully interconnected to exchange telemetry data.

You can provision bidirectional communication channels between certain pairs of nodes. Each available channel requires a specific amount of power to maintain. 

Data exchange operates across the provisioned channels: telemetry can be transmitted directly between two nodes if a channel is provisioned between them. Telemetry transmission is transitive: if data can be transmitted between node A and node B, and between node B and node C, then it can be transmitted between node A and node C.

Your objective is to select a set of channels to provision such that telemetry can be exchanged among all core controllers. You may provision channels involving standard processing nodes if using them as intermediaries reduces the overall power consumption.

Find the minimum total power required to provision a valid set of channels.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers: the identifiers of the core controllers.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), representing an available bidirectional channel between node **u** and node **v** that requires **w** units of power to maintain.
It is guaranteed that there exists at least one set of channels that allows all core controllers to exchange telemetry data.

## Output

Print a single integer: the minimum total power required to provision channels such that all core controllers can exchange telemetry data with each other.

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

In Example 1, provisioning channels through the standard processing node 4 (requiring 1+1+1 = 3 power) is more efficient than linking the three core controllers directly (which would require 2+2 = 4 power). In Example 3, there is only one core controller, so no channels need to be provisioned (0 power).