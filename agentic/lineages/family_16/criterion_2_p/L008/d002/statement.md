# Problem B — Expedition Pipeline

Time limit: 1 s   Memory limit: 256 MB

## Description

An expedition needs to survey **j** distinct sectors using exactly **two** rovers. Every sector must be mapped by the Radar Rover first and then drilled by the Sampling Rover. For each sector, you are given its mapping duration and its drilling duration. 

You must assign a unique priority rank from 1 (highest) to **j** (lowest) to each sector. The expedition then proceeds according to these operational rules:

- The Radar Rover processes the sectors one by one, always choosing the unmapped sector with the highest priority.
- The Sampling Rover processes the sectors one by one. It can only drill a sector after the Radar Rover has completely finished mapping it. Whenever the Sampling Rover is ready to begin a new sector, it always chooses the waiting (already mapped) sector with the highest priority.
- Each rover can only operate in one sector at a time. Once a rover begins an operation on a sector, it must finish it without interruption.
- Neither rover can remain idle if there is an eligible sector ready for it to process.

Determine the priority assignment that minimizes the time at which all sectors are completely finished. Report that smallest possible finish time.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the durations for a sector with the Radar Rover and the Sampling Rover.

## Output

Print a single integer: the smallest possible time at which all sectors are finished.

## Examples

### Example 1

**Input**
```
3
3 2
2 4
1 3
```

**Output**
```
10
```

### Example 2

**Input**
```
1
5 3
```

**Output**
```
8
```

### Example 3

**Input**
```
3
2 2
2 2
2 2
```

**Output**
```
8
```

## Note

In Example 2, the single sector takes 5 with the Radar Rover then 3 with the Sampling Rover, finishing at time 8.