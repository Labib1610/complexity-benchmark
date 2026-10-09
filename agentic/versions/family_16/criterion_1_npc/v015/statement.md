# Problem A — Plant Assembly Operations

Time limit: 5 s   Memory limit: 256 MB

## Description

A manufacturing plant operates **m** specialized assembly stations. The production team must fulfill a batch of **j** product orders. Each order consists of a sequence of manufacturing stages that must be completed in their listed order; a stage cannot begin until the preceding stage of that same order has completely finished. A stage requires the dedicated use of one specific assembly station, and once started, must run to completion without interruption for its required number of minutes. A station can only handle one stage from one order at any given time. The plant manager needs to know the shortest possible duration required to fully complete all orders.

## Input

The first line contains two integers **j** and **m** (1 ≤ j ≤ 10, 1 ≤ m ≤ 10), representing the number of product orders and the number of assembly stations, respectively.
Each of the following **j** lines describes one product order. The line begins with an integer **o**, the number of manufacturing stages in that order. This is followed by **o** pairs of integers, where each pair specifies the required assembly station (from 1 to m) and the duration in minutes (from 1 to 1000) for that stage, in the exact order they must be performed.
The total number of manufacturing stages across all orders will not exceed 50.

## Output

Print a single integer: the minimum number of minutes required to finish all stages of all product orders.

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

In Example 1, two identical product orders each pass through assembly stations 1, 2, and 3 (2 minutes each); the second order trails the first through the stations and finishes at minute 8. In Example 3, the two product orders use different stations and run in parallel, finishing at minute 4.
