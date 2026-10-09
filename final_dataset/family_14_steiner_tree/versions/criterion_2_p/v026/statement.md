# Phase 3: Synchronization Energy

Time limit: 2 s
Memory limit: 256 MB

## Description

The facility's emergency response protocol consists of four automated phases:

1. **Phase 1 (Detection)**: The system initializes **n** hardware modules (numbered 1 to n) and a fixed infrastructure of **m** bidirectional power relays. The infrastructure connects all modules such that there are exactly **n − 1** relays, and between any two modules there is exactly one valid sequence of relays connecting them.
2. **Phase 2 (Flagging)**: A diagnostic scan identifies exactly **t** modules that require immediate synchronization.
3. **Phase 3 (Synchronization - Your Task)**: The central system must power on a subset of the relays. The powered-on relays must form a connected network that links all **t** flagged modules together (this network may route through unflagged modules). Each relay requires a specific energy expenditure to power on, and the total energy is the sum of the energy requirements for all powered-on relays. The system must calculate the absolute minimum total energy required.
4. **Phase 4 (Purge)**: The synchronized modules execute a distributed memory purge.

Your program is responsible for Phase 3. Given the infrastructure layout and the list of flagged modules from Phase 2, calculate the minimum total energy expenditure required to complete Phase 3.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1).
The second line contains **t** distinct integers: the identifiers of the flagged modules.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000): a relay connecting module u to module v requiring w units of energy to power on. The relays form the infrastructure described in Phase 1.

## Output

Print a single integer: the minimum total energy required to link all flagged modules.

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
