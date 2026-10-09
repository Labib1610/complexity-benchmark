# Problem B — Two-Stage Assembly

Time limit: 1 s   Memory limit: 256 MB

## Description

A manufacturing facility receives a batch of **j** distinct production requests. Each request undergoes a two-step procedure: it must first clear the primary fabrication unit, and subsequently, it must clear the secondary assembly unit.

The facility operates under the following structural rules:
- A unit can only work on a single request at any given moment.
- The secondary assembly unit cannot begin work on a request until the primary fabrication unit has completely finished its work on that exact request.
- If the secondary unit is busy, a request that has cleared the primary unit will simply wait until the secondary unit becomes available.
- The facility management dictates a single sequence for all requests. The requests are processed by the primary unit in this sequence, and they must also be processed by the secondary unit in this exact same sequence.

For each request, the duration required in the primary unit and the duration required in the secondary unit are provided. Based on these rules, you must establish the sequence of requests that minimizes the total elapsed time from the moment the first request begins in the primary unit to the moment the final request is fully completed by the secondary unit. Output this minimum possible completion time.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the durations required for a request in the primary fabrication unit and the secondary assembly unit, respectively.

## Output

Print a single integer: the smallest possible time at which all requests are fully completed.

## Examples

### Example 1

**Input**
```
3
3 2
2 4
1 3
```

**Output**
```
10
```

### Example 2

**Input**
```
1
5 3
```

**Output**
```
8
```

### Example 3

**Input**
```
3
2 2
2 2
2 2
```

**Output**
```
8
```

## Note

In Example 2, the single request takes 5 in the primary fabrication unit and then 3 in the secondary assembly unit, finishing at time 8.
