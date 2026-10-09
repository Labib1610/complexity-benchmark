# Archival Restoration

Time limit: 1 s   Memory limit: 256 MB

## Description

An archive has recently acquired **j** ancient manuscripts. You must arrange them into a single initial stack.

A historian and a conservator will process the stack:
- The historian takes the top manuscript from the stack, examines it for its required duration, and drops it into a walled chute. They immediately proceed to the next manuscript in the stack.
- The conservator sits at the bottom of the chute. Whenever the chute contains at least one manuscript and the conservator is free, they pull the manuscript currently at the bottom of the chute, stabilize it for its required duration, and archive it.
- The chute is narrow, meaning documents physically cannot slide past one another.

Determine the initial stack arrangement that minimizes the time at which the conservator finishes archiving the last manuscript. Report this minimum completion time.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the duration required for the historian to examine the manuscript, and the duration required for the conservator to stabilize it, respectively.

## Output

Print a single integer: the smallest possible time at which the conservator finishes archiving the last manuscript.

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

In Example 2, the single manuscript takes 5 units of time to examine and then 3 units of time to stabilize, finishing at time 8.