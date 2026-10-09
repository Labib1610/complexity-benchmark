# Problem A — Workshop Scheduling

Time limit: 5 s   Memory limit: 256 MB

## Description

A custom workshop has **m** specialized workstations and must fulfill **j** bespoke orders. Each order requires a fixed sequence of crafting steps, as physical dependencies dictate the order of construction; each step must be performed at a specific workstation for a given number of hours. The operating rules are:

- The steps of an order must be performed strictly in their listed sequence (a step begins only after the prior step of the exact same order is completed).
- Each workstation accommodates only one step at any given moment, to prevent tool interference.
- Once initiated, a step proceeds without interruption until it is done, because partially finished materials cannot be left exposed.

Coordinate all crafting steps so that the hour at which the **final** step concludes is as early as possible, allowing the workshop to ship the entire batch of orders together. Report that earliest possible completion hour.

## Input

The first line contains two integers **j** and **m** (1 ≤ j ≤ 10, 1 ≤ m ≤ 10).
Each of the next **j** lines describes one order: an integer **o** (the number of crafting steps) followed by **o** pairs of integers `workstation hours` (1 ≤ workstation ≤ m, 1 ≤ hours ≤ 1000), listing the order's steps in their required sequence.
The total number of crafting steps across all orders is at most 50.

## Output

Print a single integer: the earliest possible hour at which all orders are completely finished.

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

In Example 1, two identical orders each pass through workstations 1, 2, 3 (2 hours each); the second order trails the first through the sequence and finishes at hour 8. In Example 3 the two orders use different workstations and run in parallel, finishing at hour 4.
