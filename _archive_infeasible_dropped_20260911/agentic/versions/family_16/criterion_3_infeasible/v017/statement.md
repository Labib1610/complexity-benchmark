# Problem C — Impossible Deadline: Certify It

Time limit: 2 s   Memory limit: 256 MB

## Description

A software company is deploying an update consisting of **j** independent modules. Each module must first be compiled on a single build server (Phase 1), and then verified on a single testing server (Phase 2). Each server can process only one module at a time. A module reaches the testing server only after its compilation is completely finished.

The company has scheduled a strict deployment window of exactly **T** minutes. Every module must be fully verified by the end of this window.

For every input in this scenario, it is guaranteed that the deployment window cannot be met, regardless of the order in which modules are processed. Your task is not to find a schedule, but to prove the window is impossible by providing a short failure record that the system can check directly against the input.

Exactly one of the following reasons always applies. Print the one that holds:

- **Sequential bottleneck.** If a single module's combined compilation and verification time exceeds **T**, that module cannot finish within the window even if processed immediately. Print `JOB i`, where **i** (1-based index) is the module.
- **Server overload.** A server processes modules sequentially, so it requires at least the sum of all its assigned processing times. If the total work on the build server (or the testing server) exceeds **T**, the window is impossible. Print `LOAD c`, where **c** is 1 for the build server or 2 for the testing server, and the total processing time on server **c** exceeds **T**.

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the compilation time and verification time of a module.

## Output

Print a single line: `JOB i` (a module whose p1 + p2 exceeds T) or `LOAD c` (a server c whose total load exceeds T).

## Examples

### Example 1

**Input**
```
3 100
70 60
2 2
3 4
```

**Output**
```
JOB 1
```

### Example 2

**Input**
```
4 150
50 1
50 1
50 1
50 1
```

**Output**
```
LOAD 1
```

## Note

In Example 1, module 1 needs 70 + 60 = 130 > 100 minutes in sequence, so `JOB 1` proves the window is impossible. In Example 2, no single module exceeds 150 minutes, but the build server must process 50+50+50+50 = 200 > 150 minutes of work in total, so `LOAD 1` is the correct output.
