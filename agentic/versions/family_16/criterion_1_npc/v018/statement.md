# Problem A — Facility Coordination

Time limit: 5 s   Memory limit: 256 MB

## Description

A facility operates **m** fabrication units. It receives **j** manufacturing orders. Each manufacturing order dictates a specific sequence of phases. For every phase, the order specifies exactly which fabrication unit is required and how many time units the phase will take to complete.

The execution of these phases is subject to the following strict conditions:
- **Sequential dependence:** The phases of any single order must be carried out in the exact sequence provided. A phase may only begin after the immediately preceding phase for that same order has completely finished.
- **Unit exclusivity:** Any given fabrication unit can only be occupied by a single phase at any moment.
- **Uninterrupted execution:** Once a phase begins on a fabrication unit, it cannot be paused, preempted, or transferred. It must run continuously until its required time units have elapsed.

Your task is to coordinate the timing of all phases across the facility. Determine the earliest possible time at which all phases of all manufacturing orders can be completely finished.

## Input

The first line contains two integers **j** and **m** (1 ≤ j ≤ 10, 1 ≤ m ≤ 10), representing the number of manufacturing orders and fabrication units, respectively.
Each of the subsequent **j** lines details a single order. The line begins with an integer **o** (the number of phases in the order), followed by **o** pairs of integers. Each pair consists of `unit duration` (1 ≤ unit ≤ m, 1 ≤ duration ≤ 1000), indicating the required fabrication unit and the time units needed for that phase. The phases are listed in the order they must be executed.
The total number of phases across all orders combined will not exceed 50.

## Output

Print a single integer: the minimum possible time at which all orders are completely finished.

## Examples

### Example 1

**Input**
```
2 3
3 1 2 2 2 3 2
3 1 2 2 2 3 2
```

**Output**
```
8
```

### Example 2

**Input**
```
1 3
3 1 5 2 3 3 2
```

**Output**
```
10
```

### Example 3

**Input**
```
2 3
1 1 4
1 2 3
```

**Output**
```
4
```

## Note

In Example 1, two identical manufacturing orders each pass through fabrication units 1, 2, and 3 (taking 2 time units each). The second order trails the first through the sequence and finishes at time 8. In Example 3, the two orders require different fabrication units and run simultaneously, finishing at time 4.
