# Problem A — Bureaucratic Bottleneck

Time limit: 5 s   Memory limit: 256 MB

## Description

You are managing the approval process for **j** critical dossiers. Your agency consists of **m** specialized departments. Each dossier requires a strict sequence of reviews; each review must be conducted by a specific department and takes a fixed number of hours.

The rules of the agency are absolute:
- A dossier's reviews must be completed in the exact order specified. A review cannot begin until the dossier's previous review has fully concluded.
- Each department can only process one dossier at any given time.
- Once a department begins a review, they must work on it continuously until it is finished. No interruptions are allowed.
- Between reviews, a dossier can sit in a secure pending tray indefinitely.

You must orchestrate all reviews such that the time at which every single dossier has completed its final review is minimized. Report this minimum completion time.

## Input

The first line contains two integers **j** and **m** (1 ≤ j ≤ 10, 1 ≤ m ≤ 10).
Each of the next **j** lines details the requirements for one dossier: an integer **o** (the number of reviews) followed by **o** pairs of integers `department duration` (1 ≤ department ≤ m, 1 ≤ duration ≤ 1000), listing the dossier's reviews in order.
The total number of reviews across all dossiers is at most 50.

## Output

Print a single integer: the earliest possible time (in hours) at which all dossiers are fully approved.

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

In Example 1, two identical dossiers each require departments 1, 2, and 3 in sequence (for 2 hours each); the second dossier trails the first through the departments and finishes at 8 hours. In Example 3, the two dossiers require different departments and can be reviewed in parallel, finishing at 4 hours.
