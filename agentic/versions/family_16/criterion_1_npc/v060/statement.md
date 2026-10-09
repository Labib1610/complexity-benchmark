# Problem A — Alchemical Synthesis

Time limit: 5 s   Memory limit: 256 MB

## Description

The Royal Academy of Alchemy has **m** specialized enchanted apparatuses and needs to brew **j** complex potions. Every potion requires a strict sequence of brewing stages. Each stage must be performed using a specific apparatus for a precise number of minutes. The fundamental laws of alchemy dictate:

- A potion's stages must be executed in the exact order prescribed. A stage can only commence after the preceding stage for that specific potion has fully concluded, as the liquid must be carefully transferred between apparatuses.
- An apparatus can only process one potion at a time. Attempting to use the same apparatus for multiple potions simultaneously would result in catastrophic contamination.
- Once a brewing stage is initiated, it must proceed continuously until its required duration is met. Interrupting a stage ruins the potion.

The Head Alchemist wants to complete the entire batch of potions as early as possible. Determine a schedule for all stages that minimizes the time at which the final stage of the final potion is completed, and report this completion time.

## Input

The first line contains two integers **j** and **m** (1 ≤ j ≤ 10, 1 ≤ m ≤ 10).
Each of the following **j** lines details the recipe for one potion: an integer **o** (the number of stages), followed by **o** pairs of integers `apparatus duration` (1 ≤ apparatus ≤ m, 1 ≤ duration ≤ 1000), representing the potion's stages in their required sequence.
The total number of stages across all potions does not exceed 50.

## Output

Output a single integer: the earliest possible time at which all potions have finished their final brewing stage.

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

In Example 1, two identical potions each undergo stages in apparatuses 1, 2, and 3 (requiring 2 minutes each). The second potion follows the first through the sequence and is completed at minute 8. In Example 3, the two potions require different apparatuses and can be brewed simultaneously, finishing at minute 4.
