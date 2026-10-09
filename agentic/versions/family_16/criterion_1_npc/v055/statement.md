# Problem A — Culinary Coordination

Time limit: 5 s   Memory limit: 256 MB

## Description

A catering kitchen is divided into **m** specialized culinary stations to prepare **j** recipes. 

Each recipe dictates a strict sequence of preparations. Each preparation requires the use of a specific culinary station for an exact number of minutes. A preparation cannot be paused or interrupted once it has begun. 

A recipe's sequence must be followed exactly: a preparation can only begin after the recipe's preceding preparation has entirely concluded. Furthermore, each culinary station is equipped to handle only one preparation at a time. 

The executive chef must coordinate the schedule to minimize the total time required. Determine the earliest possible minute when the final preparation for the last remaining recipe is completed.

## Input

The first line contains two integers **j** and **m** (1 ≤ j ≤ 10, 1 ≤ m ≤ 10).
Each of the next **j** lines describes one recipe: an integer **o** (the number of preparations) followed by **o** pairs of integers `station duration` (1 ≤ station ≤ m, 1 ≤ duration ≤ 1000), listing the recipe's preparations in chronological order.
The total number of preparations across all recipes is at most 50.

## Output

Print a single integer: the earliest possible time at which all recipes are fully prepared.

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

In Example 1, two identical recipes each pass through stations 1, 2, and 3 (2 minutes each); the second recipe trails the first through the stations and finishes at minute 8. In Example 3, the two recipes use different stations and run in parallel, finishing at minute 4.
