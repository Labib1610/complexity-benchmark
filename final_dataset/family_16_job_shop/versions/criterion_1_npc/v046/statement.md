# Problem A — Custom Fabrication Timeline

Time limit: 5 s   Memory limit: 256 MB

## Description

A custom fabrication facility operates **m** specialized workstations to build **j** unique products. Building a product requires completing a strict sequence of fabrication steps. Each step must be performed at a designated workstation and requires a precise amount of continuous time to complete.

The facility's timeline must satisfy several physical constraints:
- For any single product, its steps must be executed in the exact order specified. A step cannot begin until the preceding step for that same product has completely finished.
- Each workstation has the capacity to process only one step at any given moment.
- Once a workstation begins a step, the process cannot be paused, swapped, or interrupted until the required time has fully elapsed.

Your task is to schedule all steps across all workstations to minimize the total time required. Determine the earliest possible moment when the final step of the final product is completed.

## Input

The first line provides two integers **j** and **m** (1 ≤ j ≤ 10, 1 ≤ m ≤ 10), representing the number of products and workstations, respectively.
The following **j** lines each define the sequence of steps for a single product. A line starts with an integer **o**, the total number of steps for this product. This is followed by **o** pairs of integers formatted as `workstation duration` (1 ≤ workstation ≤ m, 1 ≤ duration ≤ 1000). These pairs dictate the exact chronological order in which the steps must occur.
The total number of steps across all products combined will not exceed 50.

## Output

Output a single integer representing the minimum possible time at which every product is fully completed.

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

In Example 1, two identical products both require workstations 1, 2, and 3 in sequence (taking 2 time units on each). The second product follows the first through the sequence and completes at time 8. In Example 3, the two products utilize different workstations and can be processed simultaneously, allowing them to finish at time 4.
