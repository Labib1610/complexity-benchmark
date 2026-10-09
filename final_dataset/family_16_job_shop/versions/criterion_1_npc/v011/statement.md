# Problem A — Bureaucratic Bottleneck

Time limit: 5 s   Memory limit: 256 MB

## Description

The Grand Council consists of **m** distinct Magistrates. The council has received **j** petitions that require approval.

Each petition has a strict bureaucratic path it must follow, consisting of a sequence of review steps. Each review step requires a specific Magistrate to dedicate a given number of hours to that petition. The procedures dictate the following:

- A petition's review steps must be completed in the exact sequence listed. A petition can only advance to its next review step after the previous review step for that same petition has finished.
- Each Magistrate can only examine one petition at a time.
- Once a Magistrate begins a review step, they must work on it continuously until that step is entirely finished (no interruptions).

Arrange the timing of all reviews so that the hour when the **last** review step concludes is as small as possible. Report this earliest possible completion hour.

## Input

The first line contains two integers **j** and **m** (1 ≤ j ≤ 10, 1 ≤ m ≤ 10).
Each of the next **j** lines describes one petition: an integer **o** (the number of review steps) followed by **o** pairs of integers `magistrate hours` (1 ≤ magistrate ≤ m, 1 ≤ hours ≤ 1000), listing the petition's review steps in order.
The total number of review steps across all petitions is at most 50.

## Output

Print a single integer: the smallest possible hour at which all petitions are finished.

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

In Example 1, two identical petitions each pass through Magistrates 1, 2, and 3 (2 hours each); the second petition trails the first through the process and finishes at hour 8. In Example 3, the two petitions require different Magistrates and are reviewed in parallel, finishing at hour 4.
