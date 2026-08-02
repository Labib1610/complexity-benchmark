# Shift Roster Audit Pipeline — Infeasibility Certificate

**Time limit:** 2 s  
**Memory limit:** 256 MB

### Description

An enterprise shift-management system processes employee schedules through a multi-stage validation pipeline:

1. **Ingestion Stage:** Reads employee records and lists of incompatible worker pairs.
2. **Infeasibility Certificate Stage (Current Task):** Searches for structural proof that a two-shift roster is impossible. Specifically, it searches for a set of three distinct employees who are all mutually incompatible with one another. When such a set exists, allocating them across only two shifts is impossible because at least two of them would inevitably share a shift.
3. **Resolution Stage:** Routes the certificate to HR coordinators to adjust worker availability.

You are tasked with implementing **Stage 2**. Given the worker compatibility records, find three workers $a, b, c$ (with $a < b < c$) such that every pair among them is mutually incompatible ($a$ with $b$, $a$ with $c$, and $b$ with $c$). To ensure consistent logging across pipeline runs, if there are multiple such triplets, you must select the lexicographically smallest one (the one with the smallest $a$; if tied, the smallest $b$; if still tied, the smallest $c$).

It is guaranteed that at least one such triplet exists in the input data.

### Input

The first line contains two integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2\cdot 10^5)$), representing the number of workers (numbered $1$ through $n$) and the number of incompatible worker pairs, respectively.

Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n, u \neq v$), indicating that worker $u$ and worker $v$ are mutually incompatible.

It is guaranteed that at least one group of three mutually incompatible workers exists.

### Output

Print three space-separated integers $a$, $b$, and $c$ on a single line such that $a < b < c$, representing the lexicographically smallest triplet of mutually incompatible workers.

### Example 1

**Input:**
```
4 5
1 2
1 3
2 3
2 4
3 4
```

**Output:**
```
1 2 3
```

### Example 2

**Input:**
```
5 6
1 2
1 4
2 4
3 4
3 5
4 5
```

**Output:**
```
1 2 4
```
