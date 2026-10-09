# Problem A — Imperial Bureaucracy

Time limit: 5 s   Memory limit: 256 MB

## Description

The Empire is processing **j** legislative decrees. There are **m** senior magistrates, numbered 1 to **m**, who must review them.

Each decree requires a strict sequence of reviews. Each review must be conducted by a specific magistrate and takes a predetermined number of hours. The bureaucratic protocol dictates:

- A decree must progress through its required reviews in the exact order they are listed. A subsequent review for a decree cannot begin until its immediately preceding review has been fully completed.
- A magistrate is capable of focusing on only one review at a time.
- Once a magistrate begins a review, they must work on it continuously until it is finished. They cannot set it aside or be interrupted.

You are tasked with coordinating the magistrates. Determine the earliest possible hour when all decrees have successfully passed their final reviews.

## Input

The first line contains two integers **j** and **m** (1 ≤ j ≤ 10, 1 ≤ m ≤ 10).
Each of the next **j** lines describes one decree: an integer **o** (the number of reviews) followed by **o** pairs of integers `magistrate duration` (1 ≤ magistrate ≤ m, 1 ≤ duration ≤ 1000), listing the decree's reviews in order.
The total number of reviews across all decrees is at most 50.

## Output

Print a single integer: the earliest possible hour at which all decrees are fully reviewed.

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

In Example 1, two identical decrees each pass through magistrates 1, 2, and 3 (2 hours each); the second decree trails the first through the sequence and finishes at hour 8. In Example 3 the two decrees require different magistrates and are reviewed in parallel, finishing at hour 4.
