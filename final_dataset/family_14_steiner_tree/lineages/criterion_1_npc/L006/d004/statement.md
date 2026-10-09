# Problem A — Relative Observability

Time limit: 5 s   Memory limit: 256 MB

## Description

A data science team is analyzing a system of $n$ unknown scalar variables, indexed 1 through $n$. The team is particularly interested in a specific subset of $t$ target variables. 

Their objective is to determine the exact relative differences between all pairs of these $t$ target variables. 

Initially, none of the variables are known, and no relative differences can be deduced. However, the team can purchase access to a set of $m$ potential pairwise measurements. Purchasing a measurement between variable $u$ and variable $v$ provides the exact value of their difference (which gives both $x_u - x_v$ and $x_v - x_u$). Differences are additive: if the relative difference between $A$ and $B$ is known, and the relative difference between $B$ and $C$ is known, then the relative difference between $A$ and $C$ can be deduced. 

The team is allowed to purchase measurements involving non-target variables, as long as these measurements help deduce the required differences between the target variables. 

Each available measurement has a fixed data-acquisition cost, denoted by $w$. The total cost incurred by the team is the sum of the acquisition costs of the distinct measurements they choose to purchase. 

Determine the minimum total data-acquisition cost required to select and purchase a combination of measurements such that the relative differences between all $t$ target variables can be deduced.

## Input

The first line provides three integers $n$, $m$, and $t$ (1 ≤ $t$ ≤ 10, 1 ≤ $n$ ≤ 100, 0 ≤ $m$ ≤ $n$·($n$−1)/2).
The second line lists $t$ distinct integers representing the indices of the target variables.
Each of the subsequent $m$ lines specifies an available measurement using three integers $u$, $v$, and $w$ (1 ≤ $u$, $v$ ≤ $n$, $u$ ≠ $v$, 1 ≤ $w$ ≤ 1000000). This indicates a measurement between variable $u$ and variable $v$ with an acquisition cost of $w$.
It is guaranteed that the available measurements are sufficient to deduce all pairwise differences among the target variables.

## Output

Print a single integer: the minimum total data-acquisition cost required to ensure all pairwise differences between the target variables can be deduced.

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

In Example 1, purchasing the measurements that involve the non-target variable 4 (which require costs of 1, 1, and 1; total cost = 3) is more efficient than purchasing the measurements directly between the three target variables (which would result in a total cost of 4). Variable 4 acts as an intermediate relay. 
In Example 3, there is only a single target variable, so there are no pairwise differences that need to be deduced. No measurements need to be purchased, resulting in a total cost of 0.