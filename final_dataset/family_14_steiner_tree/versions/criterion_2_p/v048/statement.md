# Orbital Station Power Grid

Time limit: 2 s   Memory limit: 256 MB

## Description

The station's automated recovery protocol executes in three distinct phases to restore functionality after a critical failure. 

**Phase 1: Topology Discovery.** 
The diagnostic swarm has already mapped the station's communication grid. It identified **n** data relays (indexed 1 through **n**) and **m = n - 1** fiber links. The grid was designed without redundant connections, meaning exactly one valid sequence of links exists between any pair of relays. The results of this phase are provided to you as input.

**Phase 2: Mesh Isolation (Your Task).** 
A synchronization mesh must be established that includes **t** specific priority relays. You must select a subset of fiber links to activate so that all **t** priority relays can transmit data to one another exclusively through the activated links (possibly passing through other non-priority relays). Activating a link requires a certain calibration latency. You must determine the absolute minimum total calibration latency of the activated links that satisfies this requirement.

**Phase 3: Budget Allocation.** 
The system will take the single integer value you compute in Phase 2, reserve that exact amount of latency in the global scheduler, and begin the reboot sequence.

Your objective is to implement the logic for Phase 2.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1).
The second line contains **t** distinct integers: the identifiers of the priority relays.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), representing a fiber link between relay **u** and relay **v** that requires **w** units of calibration latency to activate.

## Output

Print a single integer: the minimum total calibration latency required for Phase 2, which will be passed to Phase 3.

## Examples

### Example 1

**Input**
```
4 3 2
1 4
1 2 5
2 3 1
3 4 2
```

**Output**
```
8
```

### Example 2

**Input**
```
5 4 1
3
1 2 4
2 3 6
3 4 2
4 5 9
```

**Output**
```
0
```

### Example 3

**Input**
```
3 2 3
1 2 3
1 2 4
2 3 5
```

**Output**
```
9
```
