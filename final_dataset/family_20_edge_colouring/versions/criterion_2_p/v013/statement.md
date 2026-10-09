# Heterogeneous Transfer Scheduling

Time limit: 2 s   Memory limit: 256 MB

## Description
A high-performance computing cluster must execute $m$ synchronous data transfers. Each transfer $i$ must be assigned a specific execution timeslot $c_i$. With $m$ up to 400,000, the configuration space of all possible timeslot assignments is astronomically large, making the search for a conflict-free schedule appear as a massive combinatorial puzzle.

A schedule is valid if and only if no processor is involved in more than one transfer during the same timeslot. The cluster is physically partitioned into two distinct banks: the Alpha bank and the Beta bank. Every transfer connects exactly one Alpha processor to exactly one Beta processor; there are no transfers between processors within the same bank.

To minimize latency, the total number of timeslots allowed for the schedule is strictly limited to $T$, where $T$ is the maximum number of transfers any single processor participates in. You must select an assignment $c_i \in \{1, 2, \dots, T\}$ for every transfer. While the search space of $T^m$ possible assignments is vast, the strict separation between the two banks mathematically guarantees that at least one valid schedule using exactly $T$ timeslots always exists.

You must navigate this search space to output `YES` followed by one valid assignment.

## Input
The first line contains three integers $n_A$, $n_B$, and $m$ (1 ≤ $n_A$, $n_B$ ≤ 100,000, 0 ≤ $m$ ≤ 400,000), representing the number of Alpha processors, the number of Beta processors, and the total number of transfers.
The next $m$ lines each contain two integers $u$ and $v$ (1 ≤ $u$ ≤ $n_A$, 1 ≤ $v$ ≤ $n_B$), indicating a transfer between Alpha processor $u$ and Beta processor $v$.

## Output
Print `YES` on the first line.
On the second line, print $m$ space-separated integers, where the $i$-th integer is the timeslot $c_i \in \{1, \dots, T\}$ assigned to the $i$-th transfer (in the order the transfers appear in the input). If there are multiple valid schedules, you may output any of them.

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
