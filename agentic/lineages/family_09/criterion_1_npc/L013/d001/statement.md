# Problem A — Safe Concurrent Execution

Time limit: 5 s   Memory limit: 256 MB

## Description

A server environment has **n** background processes available, numbered 1 through **n**. The system administrator needs to select exactly **k** distinct processes to run concurrently.

The system features **m** exclusive hardware locks. Each lock is hardwired to exactly two specific processes; if either of those two processes is chosen to execute, it will request that shared lock. 
A concurrent execution configuration is considered safe if and only if no hardware lock is requested by more than one executing process. If both processes that share a lock are executed concurrently, they will both request it, causing a deadlock.

Given the **n** processes and the configurations of the **m** hardware locks, determine whether it is possible to select exactly **k** processes for safe concurrent execution. If a safe configuration is possible, you must provide one valid selection of processes.

## Input

The first line of the input contains three integers **n**, **m**, and **k** (1 ≤ **n** ≤ 46, 0 ≤ **m** ≤ **n**·(**n**−1)/2, 1 ≤ **k** ≤ **n**).
The next **m** lines each contain two integers **u** and **v** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**), representing the two processes that share a specific hardware lock.
The order of the two processes on a line does not matter, and no lock's pair of processes is listed more than once.

## Output

If a safe concurrent execution of exactly **k** processes can be configured, print `YES` on the first line. On the second line, print **k** distinct integers representing the process numbers to execute, separated by spaces. If there are multiple valid selections, any one will be accepted.

If no such selection is possible, print `NO`.

## Examples

### Example 1

**Input**
```
4 4 3
1 2
1 3
2 3
3 4
```

**Output**
```
NO
```

### Example 2

**Input**
```
5 2 3
1 2
3 4
```

**Output**
```
YES
1 3 5
```

### Example 3

**Input**
```
3 3 1
1 2
2 3
1 3
```

**Output**
```
YES
1
```