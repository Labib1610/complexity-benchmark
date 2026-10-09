# Problem A — Pneumatic Routing

Time limit: 5 s
Memory limit: 256 MB

## Description

A massive hospital complex consists of **n** departments, numbered 1 to **n**. To expedite the transport of physical samples and supplies, the administration is planning to install a pneumatic tube system.

The engineering team has identified **m** potential tube segments that can be constructed. Each segment links two different departments and requires a specific installation cost. Once a segment is constructed, transport capsules can travel through it in either direction.

The hospital has designated **t** priority departments that absolutely must be able to send capsules to one another. Capsules do not need a direct segment between two priority departments; they can be routed through the sorting stations of any other departments. Any two departments can successfully exchange capsules as long as there is a sequence of constructed tubes connecting them.

You are authorized to construct any combination of the potential tube segments, including those linking non-priority departments, if it results in a more cost-effective overall design. 

Determine the minimum total installation cost required to ensure that a capsule originating in any of the **t** priority departments can reach any other priority department.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers representing the identifiers of the priority departments.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), indicating that a tube segment can be constructed between department **u** and department **v** for an installation cost of **w**.
The provided potential segments are always sufficient to ensure all priority departments can be linked.

## Output

Print a single integer: the minimum total installation cost required.

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

In Example 1, constructing segments between departments 1 and 4, 2 and 4, and 3 and 4 costs 1 + 1 + 1 = 3. This allows a capsule from any of the three priority departments (1, 2, and 3) to reach any other by routing through department 4. This is more cost-effective than building segments directly between the priority departments, which would cost at least 4. 

In Example 3, there is only one priority department, so no segments need to be constructed.
