# Problem A — Component Testing

Time limit: 5 s   Memory limit: 256 MB

## Description

A quality assurance facility has **m** test stations and must evaluate **j** components. The testing procedures are highly regular and predetermined. Each component follows a strict progression of diagnostic checks; each check must be performed at a specific station for a fixed number of minutes.

To ensure accurate diagnostics, the following strict sequential constraints apply:
- A component's checks must be performed in their exact listed order. A component can only begin its next check after the current one has fully concluded.
- Each test station is highly specialized and focuses on exactly one check at a time.
- Once a station begins a check, the procedure runs continuously to completion without any interruption.

Because the progress of each component is entirely deterministic once the station access order is decided, you can carefully coordinate the access. Determine the earliest possible time at which all components have completed all their required checks.

## Input

The first line contains two integers **j** and **m** (1 ≤ j ≤ 10, 1 ≤ m ≤ 10).
Each of the next **j** lines describes the progression for one component: an integer **o** (the number of checks) followed by **o** pairs of integers `station duration` (1 ≤ station ≤ m, 1 ≤ duration ≤ 1000), listing the component's checks in their required order.
The total number of checks across all components is at most 50.

## Output

Print a single integer: the earliest possible time at which all components are completely evaluated.

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

In Example 1, two identical components each pass through stations 1, 2, and 3 (taking 2 minutes each); the second component can seamlessly follow the first through the sequence, finishing at time 8. In Example 3, the two components require different stations and can be evaluated simultaneously, finishing at time 4.
