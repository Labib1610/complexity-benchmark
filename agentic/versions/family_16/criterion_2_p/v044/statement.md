# Problem B — Cargo Sequence

Time limit: 1 s   Memory limit: 256 MB

## Description

A logistics facility must process a batch of **j** shipping containers. You must establish a strict total ordering of the containers. Any of the **j**! possible permutations is a valid configuration, and your goal is to find one that minimizes the facility's overall completion time.

Each container must pass through a security scan and then a mechanical loading phase. The system's dynamics are governed by the following rules:

- Both the scanner and the loader process all containers strictly according to the single total ordering you establish.
- Each phase handles only one container at a time. The scanner and loader are distinct mechanisms and can operate simultaneously on different containers.
- A container can begin mechanical loading only after its own security scan is entirely finished.
- If the loader finishes a container, it cannot proceed until the next container in the ordering has completed its scan.

You must evaluate this configuration space and determine the minimum possible elapsed time from the start of the first scan until all containers have finished mechanical loading.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the security scan time and mechanical loading time of a container, respectively.

## Output

Print a single integer: the smallest possible elapsed time from the start of the first scan until all containers have finished mechanical loading.

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

In Example 2, the single container takes 5 for the security scan then 3 for mechanical loading, finishing at time 8.
