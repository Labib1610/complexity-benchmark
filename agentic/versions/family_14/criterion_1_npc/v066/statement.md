# Automated Factory Commissioning

Time limit: 5 s   Memory limit: 256 MB

## Description

The commissioning of a fully automated manufacturing facility proceeds in three distinct phases:

**Phase 1: Asset Placement.** The heavy machinery is installed. Exactly **n** robotic stations are secured to the factory floor. Of these, a specific subset of **t** stations are designated as *assembly anchors*, which will coordinate the main production lines. This phase is already complete.

**Phase 2: Synchronization Routing (Your Task).** Before the factory can operate, all assembly anchors must be linked together to share real-time telemetry. There are **m** pre-installed conduits, each running between a pair of stations. Wiring a conduit with fiber-optic cable requires a specific number of labor hours. To complete this phase, you must choose a set of conduits to wire such that every assembly anchor can exchange data with every other assembly anchor, either directly or through a sequence of wired conduits. You may route connections through any of the other non-anchor stations if doing so reduces the total labor required. 

**Phase 3: Firmware Flashing.** Once the synchronization network is established, the anchors receive their operating software. This phase will be handled automatically by the central server once Phase 2 is finished.

Your objective is to determine the minimum total labor hours required to complete Phase 2.

## Input

The first line provides three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2): the total number of stations, the number of available conduits, and the number of assembly anchors.

The second line contains **t** distinct integers representing the identifiers of the assembly anchors.

Each of the subsequent **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), indicating a conduit between station **u** and station **v** that requires **w** labor hours to wire.

It is guaranteed that the available conduits are sufficient to link all the assembly anchors.

## Output

Output a single integer: the minimum total labor hours required to link all assembly anchors.

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

In Example 1, wiring the conduits that meet at the non-anchor station 4 requires 3 labor hours (1+1+1). Linking the assembly anchors directly without using station 4 as a relay would require at least 4 labor hours. In Example 3, with only a single assembly anchor, no conduits need to be wired.
