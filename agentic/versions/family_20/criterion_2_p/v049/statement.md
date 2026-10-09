# Cross-Zone Synchronization

Time limit: 2 s   Memory limit: 256 MB

## Description
A computing facility is physically partitioned into two distinct zones, designated Alpha and Beta. Within this facility, a set of $m$ synchronization operations is defined. Every operation establishes a dedicated link between exactly one machine in the Alpha zone and exactly one machine in the Beta zone. There are never any operations connecting two machines within the same zone.

During execution, hardware limitations dictate that no individual machine can participate in more than one synchronization operation during the same cycle. If multiple operations involve the same machine, they must be strictly separated into different execution cycles. 

Let $T$ denote the peak load of the system, defined as the maximum number of synchronization operations configured for any single machine across the entire facility. 

Given these structural rules, your objective is to assign an execution cycle $c_i$ to each of the $m$ operations. To ensure optimal throughput, every assigned cycle must be an integer from $1$ to $T$ inclusive. The properties of the two-zone partition guarantee that a valid assignment restricted to these $T$ cycles always exists. You must output `YES` followed by one such valid cycle assignment for all operations.

## Input
The first line contains three integers $n_A$, $n_B$, and $m$ (1 ≤ $n_A$, $n_B$ ≤ 100,000, 0 ≤ $m$ ≤ 400,000), representing the number of Alpha machines, the number of Beta machines, and the total number of operations.
The next $m$ lines each contain two integers $u$ and $v$ (1 ≤ $u$ ≤ $n_A$, 1 ≤ $v$ ≤ $n_B$), indicating an operation between Alpha machine $u$ and Beta machine $v$.

## Output
Print `YES` on the first line.
On the second line, print $m$ space-separated integers, where the $i$-th integer is the execution cycle $c_i \in \{1, \dots, T\}$ assigned to the $i$-th operation (in the order the operations appear in the input). If there are multiple valid assignments, you may output any of them.

## Example

### Input
```text
3 3 5
1 1
1 2
2 1
2 3
3 2
```

### Output
```text
YES
1 2 2 1 1
```
