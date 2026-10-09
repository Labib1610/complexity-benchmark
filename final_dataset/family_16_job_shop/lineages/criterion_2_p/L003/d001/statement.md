# Problem B — Two-Stage Assembly

Time limit: 1 s   Memory limit: 256 MB

## Description

A manufacturing facility receives a batch of **j** distinct production requests. Each request undergoes a two-step procedure: it requires fabrication, and subsequently, assembly.

The facility operates under the following structural rules:
- The fabrication unit works on one request at a time, processing the batch continuously in an order of your choosing.
- The assembly unit works on one request at a time.
- As soon as the fabrication unit completely finishes a request, that request is placed at the back of a staging line.
- The assembly unit continually takes the request at the front of the staging line and works on it. If the staging line is empty, the assembly unit simply waits until a fabricated request arrives.

For each request, the duration required for fabrication and the duration required for assembly are provided. Based on these rules, you must establish the initial order for the fabrication unit that minimizes the total elapsed time from the moment the first request begins fabrication to the moment the final request is fully completed by the assembly unit. Output this minimum possible completion time.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the durations required for a request in the fabrication unit and the assembly unit, respectively.

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

In Example 2, the single request takes 5 in the fabrication unit and then 3 in the assembly unit, finishing at time 8.