# Problem A — Cloud Provisioning

Time limit: 5 s   Memory limit: 256 MB

## Description

A cloud infrastructure team must deploy **k** isolated instances. Each instance requires exactly one compute node, one container image, and one database shard. The available inventory consists of **k** compute nodes (numbered 1 to k), **k** container images (numbered 1 to k), and **k** database shards (numbered 1 to k). 

Because of architecture differences and network policies, only specific combinations of a compute node, a container image, and a database shard will successfully initialize. You are given the list of all viable combinations.

You must select exactly **k** combinations to deploy so that no compute node, container image, or database shard is left unused or assigned to multiple instances. Determine whether this deployment is possible, and if so, report one valid assignment.

## Input

The first line contains two integers **k** and **t** (1 ≤ k ≤ 22, 0 ≤ t ≤ k·k·k): the inventory size for each resource type and the number of viable combinations.
Each of the next **t** lines contains three integers **x**, **y**, **z** (1 ≤ x, y, z ≤ k), representing a viable combination of compute node **x**, container image **y**, and database shard **z**. No combination is listed more than once.

## Output

If a valid deployment of **k** instances exists, print `YES` on the first line. Then, print **k** lines, each containing three integers `x y z` representing the compute node, container image, and database shard of one deployed instance. Any assignment in which every resource is used exactly once is accepted; the instances may be printed in any order.

If no valid deployment exists, print `NO`.

## Examples

### Example 1

**Input**
```
2 3
1 1 1
1 2 2
2 2 2
```

**Output**
```
YES
1 1 1
2 2 2
```

### Example 2

**Input**
```
2 2
1 1 1
2 1 2
```

**Output**
```
NO
```

### Example 3

**Input**
```
1 1
1 1 1
```

**Output**
```
YES
1 1 1
```

## Note

In Example 2, both viable combinations require container image 1, meaning container image 2 can never be deployed.
