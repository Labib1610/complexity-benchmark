# System Integration (Dual Architecture)

Time limit: 2 s   Memory limit: 256 MB

## Description

You are configuring a processing cluster from a pool of $n$ available hardware modules, numbered 1 to $n$. The modules were manufactured using two different proprietary architectures. You do not have the documentation to tell which module uses which architecture.

However, you have an error log of $m$ hardware conflicts. Each conflict indicates that two specific modules cannot communicate. Because of the way the architectures were designed, conflicts *only* ever occur between a module of the first architecture and a module of the second architecture. Two modules of the same architecture will never conflict with each other.

Your goal is to build a completely stable cluster of exactly $k$ modules. A cluster is considered stable if no two modules within it have a hardware conflict.

The system allocates exactly 10 bytes per module in a registry with a maximum size of 1,000,000 bytes, establishing the upper limit for the number of modules. The error log uses exactly 8 bytes per conflict record in a file with a maximum size of 3,200,000 bytes, establishing the upper limit for the number of conflicts.

Given the pool of modules, the conflict log, and the target size $k$, determine if it is possible to select exactly $k$ modules that form a stable cluster, and if so, list them.

## Input

The first line contains three integers $n$, $m$, and $k$. 
- The number of modules $n$ is at least 1 and at most the registry limit derived above. 
- The number of conflicts $m$ is at least 0 and at most the error log limit derived above. 
- The target size $k$ is between 1 and $n$ inclusive.

Each of the next $m$ lines contains two integers $u$ and $v$ ($1 \le u, v \le n$, $u \ne v$), representing a hardware conflict between module $u$ and module $v$. No conflict is listed more than once. The conflicts strictly follow the dual-architecture property described above.

## Output

If a stable cluster of exactly $k$ modules can be formed, print `YES` on the first line. On the second line, print $k$ distinct module numbers that form such a cluster, separated by spaces. Any valid cluster is accepted.

If no such cluster exists, print `NO`.

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

In Example 1, modules 1 and 2 do not conflict with each other (they must share the same architecture), so they can safely form a stable cluster of size 2. 
In Example 3, the largest possible stable cluster contains only 2 modules, making a cluster of 3 impossible.
