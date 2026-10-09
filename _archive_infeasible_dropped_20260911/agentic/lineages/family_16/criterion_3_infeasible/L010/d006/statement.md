# Problem C — Impossible Deployment: Certify It

Time limit: 2 s   Memory limit: 256 MB

## Description

A deployment engine generates a linear script consisting of exactly **T** sequential instructions, indexed from $1$ to $T$. A script manages **j** distinct applications. For each application $i$, the script must include exactly **p1** setup routines and exactly **p2** teardown routines.

To be executable, the generated script must satisfy three structural properties:
1. **Lifecycle Ordering:** For any single application $i$, all of its setup routines must be assigned to strictly earlier instruction indices than any of its teardown routines.
2. **Setup Capacity:** Any given instruction in the script can host at most one setup routine, regardless of which application it belongs to.
3. **Teardown Capacity:** Any given instruction in the script can host at most one teardown routine, regardless of which application it belongs to.
*(Note: A single instruction may simultaneously host one setup routine and one teardown routine, provided this does not violate the Lifecycle Ordering rule for their respective applications.)*

Every provided configuration represents an impossible script—there is no valid way to assign the routines to the $T$ instructions that satisfies all properties. Instead of attempting to generate the script, your task is to identify the bottleneck that proves the configuration is unachievable, providing a short certificate the engine can verify.

Exactly one of the following foundational requirements is broken. Output the applicable certificate:

- **Lifecycle Failure:** For some application $i$, there is no way to place its $p1$ setup and $p2$ teardown routines within $T$ instructions that satisfies the Lifecycle Ordering property. Output `JOB i` (where $i$ is the 1-based index of the application).
- **Setup Congestion:** There is no way to place the required setup routines for all $j$ applications within $T$ instructions that satisfies the Setup Capacity property. Output `LOAD 1`.
- **Teardown Congestion:** There is no way to place the required teardown routines for all $j$ applications within $T$ instructions that satisfies the Teardown Capacity property. Output `LOAD 2`.

You are guaranteed that exactly one of these requirements will be broken for the given input.

## Input

The first line contains two integers **j** and **T** (1 ≤ j ≤ 200000, 1 ≤ T ≤ 1000000000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the number of setup routines and teardown routines required for that application.

## Output

Print a single line: `JOB i` (for a lifecycle bottleneck) or `LOAD c` (for a congestion bottleneck, where **c** is 1 for setup congestion or 2 for teardown congestion).

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

In Example 1, application 1 requires 70 setup routines and 60 teardown routines. There is no way to place these into 100 instructions such that all setups occur strictly before all teardowns, breaking the Lifecycle Ordering property. Thus `JOB 1` is the correct proof of impossibility. 

In Example 2, no single application breaks Lifecycle Ordering. However, the applications require 50, 50, 50, and 50 setup routines respectively. There is no way to place these 200 setup routines into 150 instructions such that each instruction contains at most one setup routine, breaking the Setup Capacity property. Thus `LOAD 1` is the correct output.