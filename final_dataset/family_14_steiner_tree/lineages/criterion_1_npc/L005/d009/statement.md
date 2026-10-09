# Problem A — Autonomous Subsystem Isolation

Time limit: 5 s   Memory limit: 256 MB

## Description

You are designing the architecture for $n$ microservices. 

You can purchase bilateral integration modules. Each module connects exactly two distinct microservices, $u$ and $v$. 

A subset of microservices $S$ is defined as *autonomous* if every purchased integration module that connects to at least one microservice in $S$ actually has BOTH of its endpoints in $S$. (In other words, no purchased module crosses the boundary between $S$ and the rest of the system).

A specific subset of $t$ microservices are designated as *core*. Your task is to purchase a subset of available modules such that the following condition is satisfied:
Any autonomous subset of microservices must either contain ALL $t$ core microservices, or NONE of the $t$ core microservices. 
(It must be logically impossible for an autonomous subset to contain some, but not all, of the core microservices).

You are given a list of $m$ available modules, each with a one-time purchase cost $w$. Determine the minimum total cost of a subset of modules that satisfies this requirement.

## Input

The first line provides three integers $n$, $m$, and $t$ (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line lists $t$ distinct integers representing the indices of the core microservices (1-indexed).
The following $m$ lines each contain three integers $u$, $v$, and $w$ (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1,000,000). These represent an available module connecting microservices $u$ and $v$ that can be purchased for a cost of $w$.
It is guaranteed that it is possible to satisfy the requirement using the available modules.

## Output

Output a single integer representing the minimum total cost of a subset of modules that satisfies the condition.

## Examples

### Example 1

**Input**
```
4 6 3
1 2 3
1 4 1
2 4 1
3 4 1
1 2 2
2 3 2
1 3 2
```

**Output**
```
3
```

### Example 2

**Input**
```
4 4 3
1 2 3
1 2 1
2 3 1
1 4 10
3 4 10
```

**Output**
```
2
```

### Example 3

**Input**
```
3 2 1
1
1 2 5
2 3 5
```

**Output**
```
0
```

## Note

In Example 1, the core microservices are 1, 2, and 3. By purchasing the modules (1, 4), (2, 4), and (3, 4) for a total cost of 1+1+1=3, the only autonomous subsets of microservices are the empty set and the entire set of all 4 microservices. Both of these contain either all or none of the core microservices. If we had only purchased (1, 2), then the subset {1, 2} would be autonomous. But it contains core microservices 1 and 2, while missing 3, which violates the requirement. 

In Example 2, by purchasing modules (1, 2) and (2, 3) for a cost of 1+1=2, the autonomous subsets are $\emptyset$, $\{4\}$, $\{1, 2, 3\}$, and $\{1, 2, 3, 4\}$. Every one of these subsets contains either all 3 core microservices or none of them. Microservice 4 remains isolated, which is perfectly valid since it is not a core microservice.

In Example 3, there is only one core microservice. Any subset of microservices will either contain this 1 core microservice (which is "ALL" of them) or not contain it (which is "NONE" of them). Thus, the requirement is vacuously satisfied without purchasing any modules, resulting in a cost of 0.