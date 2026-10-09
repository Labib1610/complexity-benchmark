# Problem B — Synchronization Protocol

Time limit: 2 s   Memory limit: 256 MB

## Description

The manufacturing floor contains **n** robotic assemblies (numbered 1 to **n**). To coordinate their movements, **m** bidirectional calibration channels have been installed between specific pairs of assemblies. The layout of these channels is strictly structured: for any pair of assemblies, there is exactly one valid sequence of channels that routes a signal between them without using the same channel more than once.

Each channel has a specific activation cost associated with its calibration hardware. 

A recent firmware update dictates that a specific subset of **t** assemblies, designated as *primary*, must be able to synchronize their clocks. Synchronization is achieved if every primary assembly can exchange signals with every other primary assembly. Signals can be passed through intermediate assemblies (whether they are primary or not) as long as the channels connecting them are activated.

Your objective is to determine the absolute minimum total activation cost required to activate a set of channels that allows all primary assemblies to synchronize.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ **t** ≤ **n**, 1 ≤ **n** ≤ 200000, **m** = **n** − 1).
The second line contains **t** distinct integers: the identifiers of the primary assemblies.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**, 1 ≤ **w** ≤ 1000000), indicating that a calibration channel connects assembly **u** and assembly **v** with an activation cost of **w**. The channels connect all assemblies following the strict structure described.

## Output

Print a single integer: the minimum total activation cost for a valid configuration of channels that allows all primary assemblies to synchronize.

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
