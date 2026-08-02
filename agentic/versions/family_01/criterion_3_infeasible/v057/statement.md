# Enterprise Access Control — Security Conflict Audit Pipeline

**Time limit:** 2 s  
**Memory limit:** 256 MB

### Description

In a high-security facility, technical staff members (numbered $1$ through $n$) are routinely assigned to facility maintenance tasks across two physically separated operational zones. To prevent collusion and satisfy regulatory security policies, specific pairs of personnel are designated as restricted together—meaning no two individuals in a restricted pair may be assigned to work in the same operational zone simultaneously.

When attempting to distribute personnel across the two zones, an unresolvable access deadlock occurs if there is a group of three distinct engineers $a, b, c$ such that every pair among them is restricted from sharing a zone. Under such a condition, allocating these three individuals across only two available zones inevitably forces at least two restricted workers into the same location.

Your task is to implement the security audit tool that detects this specific failure condition. Given the records of restricted personnel pairs, find three individuals $a, b, c$ with $a < b < c$ such that $a$ and $b$ are restricted together, $a$ and $c$ are restricted together, and $b$ and $c$ are restricted together.

To ensure deterministic diagnostic logging, if multiple such triplets exist, you must identify the lexicographically smallest one (minimizing $a$ first; if tied, minimizing $b$; if still tied, minimizing $c$).

It is guaranteed that at least one such triplet exists in the input data.

### Input

The first line contains two space-separated integers $n$ and $m$ ($3 \le n \le 2000$, $3 \le m \le \min(n(n-1)/2, 2\cdot 10^5)$), representing the number of personnel and the number of restricted pairs, respectively.

Each of the next $m$ lines contains two space-separated integers $u$ and $v$ ($1 \le u, v \le n, u \neq v$), indicating that staff member $u$ and staff member $v$ are restricted from being assigned to the same operational zone.

### Output

Print three space-separated integers $a$, $b$, and $c$ on a single line such that $a < b < c$, representing the lexicographically smallest triplet of mutually restricted personnel.

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
