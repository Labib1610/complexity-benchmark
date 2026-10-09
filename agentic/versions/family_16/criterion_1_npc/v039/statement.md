# Problem A — Component Testing Schedule

Time limit: 5 s   Memory limit: 256 MB

## Description

A space agency has **m** testing facilities and must certify **j** spacecraft components. Each component requires a fixed sequence of tests; each test must run at a specific facility for a given number of days. The rules are:

- The tests for a component must run in their listed order (a test starts only after the previous test for the same component has finished, as the component physically moves between facilities).
- Each facility processes only one test at a time (enforced by safety protocols).
- Once started, a test runs to completion (no interruption is allowed during an active test).

Schedule all tests so that the time at which the **last** test finishes is as small as possible. Report that smallest possible finish time.

## Input

The first line contains two integers **j** and **m** (1 ≤ j ≤ 10, 1 ≤ m ≤ 10).
Each of the next **j** lines describes one component: an integer **o** (the number of tests) followed by **o** pairs of integers `facility duration` (1 ≤ facility ≤ m, 1 ≤ duration ≤ 1000), listing the component's tests in order.
The total number of tests across all components is at most 50.

## Output

Print a single integer: the smallest possible time at which all components are fully tested.

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

In Example 1, two identical components each pass through facilities 1, 2, 3 (2 days each); the second component trails the first through the pipeline and finishes at time 8. In Example 3 the two components use different facilities and run in parallel, finishing at time 4.
