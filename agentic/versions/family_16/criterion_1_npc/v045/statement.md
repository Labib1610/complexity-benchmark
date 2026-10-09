# Problem A — Assembly Bay Orchestration

Time limit: 5 s   Memory limit: 256 MB

## Description

You are programming the central orchestration module for an automated manufacturing pipeline. Customer requests arrive as a set of work orders, which your module must organize into a timeline before transmitting it to the physical fabrication floor.

The floor is equipped with $m$ specialized workstations. You are tasked with fulfilling $j$ work orders. Every work order consists of a strict sequence of assembly phases. Each phase specifies a target workstation and the exact number of processing cycles it takes. 

The physical constraints of the pipeline are:
- A work order's phases must be executed in the exact order they are specified. A phase cannot commence until the immediately preceding phase of that same work order has fully concluded.
- A workstation can handle at most one assembly phase at any given moment.
- Preemption is impossible; once an assembly phase begins on a workstation, it must run continuously until its required processing cycles are completed.

The factory operates under the following hardware limits that dictate the maximum scale of any given manifest:
- The intake buffer has 20 megabytes of memory. Each work order consumes exactly 2 megabytes, limiting the maximum number of work orders $j$. There is always at least one work order.
- The facility's main electrical breaker provides 500 kilowatts. Every workstation draws exactly 50 kilowatts, determining the maximum number of workstations $m$. There is always at least one workstation.
- The robotic transport system has a daily limit of 150 joint actuations. Because each assembly phase requires exactly 3 actuations to set up, the total number of phases across all work orders combined is strictly bounded.
- The thermal limit of any workstation allows for 5000 seconds of continuous operation. With each processing cycle taking exactly 5 seconds, this caps the maximum cycles a single phase can require. Every phase requires at least one cycle.

Your goal is to orchestrate the start times of all phases such that the entire manifest is completed as early as possible. Determine the minimum possible time at which the final phase of the last remaining work order finishes.

## Input

The first line of input provides two integers: $j$ and $m$.
The subsequent $j$ lines each describe a single work order. A work order line begins with an integer $p$, representing the number of assembly phases in that order. This is followed by $p$ pairs of integers. Each pair indicates the `workstation_id` (an integer from 1 to $m$) and the `cycles` required for that phase. The pairs are listed in the chronological order the phases must be executed.

## Output

Output a single integer representing the earliest possible cycle at which all work orders can be completely finished.

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

In Example 1, two identical work orders each pass through workstations 1, 2, and 3 (taking 2 cycles at each). The second work order trails the first through the workstations, concluding at cycle 8. In Example 3, the two work orders target different workstations and are executed in parallel, finishing at cycle 4.
