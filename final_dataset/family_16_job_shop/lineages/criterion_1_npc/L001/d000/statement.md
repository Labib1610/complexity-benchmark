# Problem A — Document Processing

Time limit: 5 s   Memory limit: 256 MB

## Description

A government office has **m** officials and must process **j** documents. Each document requires a fixed sequence of reviews; each review must be performed by a specific official for a given number of hours. The rules are:

- The reviews of a document must occur in their listed order (a review starts only after the previous review of the same document has finished).
- Each official processes only one review at a time.
- Once started, a review runs to completion (no interruption).

Schedule all reviews so that the time at which the **last** review finishes is as small as possible. Report that smallest possible finish time.

## Input

The first line contains two integers **j** and **m** (1 ≤ j ≤ 10, 1 ≤ m ≤ 10).
Each of the next **j** lines describes one document: an integer **o** (the number of reviews) followed by **o** pairs of integers `official duration` (1 ≤ official ≤ m, 1 ≤ duration ≤ 1000), listing the document's reviews in order.
The total number of reviews across all documents is at most 50.

## Output

Print a single integer: the smallest possible time at which all documents are finished.

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

In Example 1, two identical documents each pass through officials 1, 2, 3 (2 hours each); the second document trails the first through the pipeline and finishes at time 8. In Example 3 the two documents use different officials and run in parallel, finishing at time 4.
