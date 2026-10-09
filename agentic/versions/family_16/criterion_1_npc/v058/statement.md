# Problem A — Shipyard Refitting

Time limit: 5 s   Memory limit: 256 MB

## Description

The naval yard consists of **m** distinct specialized bays. Currently, **j** ships are docked, awaiting modifications. 

Each ship has a specific blueprint of upgrades that must be applied. A blueprint lists a series of steps. Each step dictates a particular bay that must be used and the exact number of uninterrupted hours the step will take. 

The physical nature of the work means that a ship's steps must be performed in the exact sequence given in its blueprint. A step can only commence after the immediately preceding step for that ship is completely finished.

Additionally, each bay is limited in space and can only house a single ship at any moment. Once a bay begins executing a step for a ship, it must conclude that step before it can accept another ship or before the ship can move on.

Given these operational rules, calculate the minimum total hours required from the moment work begins until all ships have fully completed their blueprints.

## Input

The first line contains two integers **j** and **m** (1 ≤ j ≤ 10, 1 ≤ m ≤ 10).
Each of the next **j** lines provides the blueprint for one ship: an integer **p** (the number of steps) followed by **p** pairs of integers `bay duration` (1 ≤ bay ≤ m, 1 ≤ duration ≤ 1000), listing the ship's steps in chronological order.
The total number of steps across all ships is at most 50.

## Output

Print a single integer: the smallest possible number of hours required for all ships to complete all their steps.

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

In Example 1, two identical ships each require bay 1, then 2, then 3 (each taking 2 hours). The second ship trails the first through the bays, with its final step concluding at hour 8. In Example 3, the two ships require different bays and proceed in parallel, concluding at hour 4.
