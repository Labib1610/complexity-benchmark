# Problem C — Insufficient Window: Diagnostic Code

Time limit: 2 s   Memory limit: 256 MB

## Description

A spacecraft must process **j** telemetry packets. Each packet requires two sequential operations: encryption (operation 1) and broadcasting (operation 2). 
Every packet must first be completely encrypted before its broadcasting can begin. 
The encryption unit can only encrypt one packet at a time. 
The broadcast antenna can only broadcast one packet at a time. 

All packets must be fully processed within a strict window of **T** microseconds.

You are given **j** and **T**, as well as the encryption time **p1** and broadcasting time **p2** for each packet.
For every test case in this problem, it is guaranteed that it is mathematically impossible to process all packets within the window **T**, regardless of the order in which they are handled. Your objective is to output a diagnostic code that proves this impossibility.

Due to the inputs provided, exactly one of the following two proofs of impossibility will be valid. Output the one that applies:

- **Individual packet violation:** A single packet's combined encryption and broadcasting time is strictly greater than **T**. Print `JOB i`, where **i** is the 1-based index of the packet.
- **Component saturation:** The total time required by a single component (either the encryption unit or the broadcast antenna) to perform its operation across all packets is strictly greater than **T**. Print `LOAD c`, where **c** is `1` if the encryption unit's total time exceeds **T**, and **c** is `2` if the broadcast antenna's total time exceeds **T**.

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the time required to encrypt and broadcast a packet, respectively.

## Output

Print a single line containing either `JOB i` (where packet **i**'s combined time exceeds **T**) or `LOAD c` (where component **c**'s total time exceeds **T**).

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

In Example 1, packet 1 requires 70 + 60 = 130 microseconds, which exceeds the 100-microsecond window. Thus, `JOB 1` is the correct diagnostic code. 
In Example 2, no single packet exceeds 150 microseconds. However, the encryption unit must perform 50 + 50 + 50 + 50 = 200 microseconds of work, which exceeds the window. Thus, `LOAD 1` is the correct diagnostic code.
