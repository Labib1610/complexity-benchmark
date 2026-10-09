# Port Clearance Pipeline

Time limit: 1 s   Memory limit: 256 MB

## Description

A shipping port receives **j** freight containers that require clearance. Each container must first pass through an automated security scanner, and subsequently be reviewed by an inspector. 

The clearance process strictly adheres to the following rules:
- You must establish a single processing sequence for all containers.
- The scanner processes the containers in your chosen sequence, handling only one container at a time.
- The inspector reviews the containers in that exact same sequence, handling only one container at a time.
- The inspector can only begin reviewing a specific container once the scanner has fully completed its scan of that container.

Determine the sequence that minimizes the total time required until the final container completes its inspection, and output this minimum time.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200,000).
Each of the next **j** lines contains two integers **s** and **i** (1 ≤ s, i ≤ 1,000,000): the time required for the scanner and the time required for the inspector to process the container, respectively.

## Output

Print a single integer: the smallest possible time at which all containers have finished inspection.

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

In Example 2, the single container takes 5 time units in the scanner and then 3 time units with the inspector, finishing at time 8.
