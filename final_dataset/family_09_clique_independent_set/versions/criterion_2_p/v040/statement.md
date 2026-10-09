# Problem B — Sandbox Activation

Time limit: 2 s   Memory limit: 256 MB

## Description

The automated deployment pipeline for a distributed system operates in three sequential phases:

**Phase 1 (Scanning):** A static analyzer inspects $n$ software modules (numbered 1 to $n$) and identifies $m$ pairs of modules that exhibit overlapping memory access, referred to as *interferences*. Because of the system's architecture, every interference strictly occurs between a module responsible for routing and a module responsible for storage. (The analyzer does not record which role each module plays; you only receive the list of interferences, but this structural property is guaranteed to hold).

**Phase 2 (Selection - Your Task):** Given the total number of modules $n$, the $m$ interferences, and a target capacity $k$, you must select exactly $k$ modules to run concurrently. To ensure stability, no two selected modules can have an interference between them.

**Phase 3 (Deployment):** The sandbox orchestrator takes your selected $k$ modules, provisions their isolated environments, and executes the integration test suite.

Your objective is to implement the logic for Phase 2. Determine if a valid selection of exactly $k$ modules exists, and if so, provide one.

## Input

The first line contains three integers $n$, $m$, and $k$ ($1 \le n \le 100000$, $0 \le m \le 400000$, $1 \le k \le n$).
Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), representing an interference between module $u$ and module $v$. No interference is listed more than once. It is guaranteed that the interferences strictly follow the routing-and-storage structure described in Phase 1.

## Output

If a valid selection of $k$ modules exists, print `YES` on the first line. On the second line, print $k$ distinct module numbers that form such a selection, separated by spaces. Any valid selection of exactly $k$ modules with no interferences among them is accepted.

If no such selection is possible, print `NO`.

## Examples

### Example 1

**Input**
```
4 4 2
1 3
1 4
2 3
2 4
```

**Output**
```
YES
1 2
```

### Example 2

**Input**
```
5 0 5
```

**Output**
```
YES
1 2 3 4 5
```

### Example 3

**Input**
```
4 4 3
1 3
1 4
2 3
2 4
```

**Output**
```
NO
```

## Note

In Example 1, modules 1 and 2 do not interfere with each other, so they can be selected together.
In Example 3, the maximum number of modules that can be selected without any interferences is 2, so a selection of 3 is impossible.
