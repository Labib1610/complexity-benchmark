# Problem A — Expedition Logistics

Time limit: 5 s   Memory limit: 256 MB

## Description

A deep-space research vessel is hosting an expedition. The ship has $L$ specialized laboratory modules and carries $R$ researchers. 

Each researcher has a strict sequence of experiments they must conduct. Each experiment must be performed in a specific laboratory module for a predetermined number of cycles. The following protocols are enforced:

- A researcher must conduct their experiments in the exact order specified in their sequence. A researcher can only begin an experiment after their previous experiment has completely finished.
- Each laboratory module is isolated and can only host a single experiment at any given time.
- Once an experiment begins in a laboratory, it must run continuously until it is finished. It cannot be paused, interrupted, or relocated.

The central computer needs to coordinate the itineraries of all researchers. Determine the earliest possible cycle by which all researchers can have completed all of their experiments.

## Input

The first line contains two integers $R$ and $L$. The expedition team consists of at least one researcher, up to the maximum capacity of the ship's 10-person crew capsule. The vessel is equipped with at least one, and up to 10 specialized laboratory modules, matching the number of main power conduits.

Each of the next $R$ lines describes the itinerary for one researcher. A line begins with an integer $E$ (the number of experiments for this researcher), followed by $E$ pairs of integers. Each pair represents an experiment and consists of a `laboratory_id` (from 1 to $L$) and a `duration` in cycles, listing the researcher's sequence of experiments in order. 

The central computer allocates a maximum of 50 data-drives for the entire mission. Since each experiment permanently consumes exactly one data-drive, the total number of experiments across all researchers will never exceed 50. Furthermore, an experiment takes at least 1 cycle. The reactor's thermal limit prevents any single experiment from lasting more than 1000 cycles.

## Output

Print a single integer: the minimum possible number of cycles required for all researchers to complete their sequences of experiments.

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

In Example 1, two researchers have identical itineraries passing through laboratories 1, 2, and 3 (requiring 2 cycles each). The second researcher trails the first through the sequence and finishes their final experiment after 8 cycles. In Example 3, the two researchers use different laboratories and conduct their experiments in parallel, finishing after 4 cycles.
