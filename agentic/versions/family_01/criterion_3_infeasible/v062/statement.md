# Diagnostic Pipeline: Mutual Coupling Identification

Time limit: 2 s   Memory limit: 256 MB

In an automated system health diagnostic pipeline, hardware modules are monitored for operational interference. The overall diagnostic workflow consists of three main phases:

1. **Link Ingestion**: The system registers all pairwise mutual couplings observed between $n$ numbered modules (indexed $1$ through $n$).
2. **Cluster Identification (Current Stage)**: The pipeline isolates three distinct modules $a, b, c$ ($a < b < c$) that form a complete mutual coupling loop—meaning module $a$ couples with $b$, $a$ couples with $c$, and $b$ couples with $c$. To maintain reproducible diagnostic logs, the system must select the lexicographically smallest triple $(a, b, c)$ (minimizing $a$, then $b$, then $c$).
3. **Targeted Calibration**: Once identified, the isolated module triple is passed to the phase-alignment controller for sequential frequency suppression.

You are tasked with implementing Stage 2 of this diagnostic pipeline. Given the logged pairwise couplings from Stage 1, identify and report the target triple $(a, b, c)$.

## Input
The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2\cdot 10^5)$), representing the number of modules and the total number of logged pairwise mutual couplings, respectively.

Each of the following $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \neq v$), indicating a recorded pairwise mutual coupling between module $u$ and module $v$.

It is guaranteed that at least one valid triple of mutually coupled modules exists.

## Output
Output a single line containing three space-separated integers $a$, $b$, and $c$ ($a < b < c$) corresponding to the lexicographically smallest triple of mutually coupled modules.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
2 4
3 4
```
Output:
```
1 2 3
```

## Example 2
Input:
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```
Output:
```
1 2 4
```
