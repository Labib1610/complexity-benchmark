# Problem B — Minimal Active Swap Budget

Time limit: 2 s   Memory limit: 256 MB

## Description

You are configuring a system of **n** fluid reservoirs, numbered 1 to **n**, and **m** bidirectional mixing pipes. Each pipe connects two distinct reservoirs and has an associated maintenance cost.

A subset of reservoirs **S** is considered *fully mixable* if, using only the active mixing pipes that connect two reservoirs both in **S**, a substance introduced into any reservoir in **S** can eventually reach every other reservoir in **S**. (A subset containing exactly one reservoir is inherently fully mixable). Initially, the full set of **n** reservoirs is fully mixable.

You may simplify the system by performing a sequence of reservoir sealings. In a single step, you permanently seal exactly one reservoir, which safely drops any mixing pipes connected to it. However, your sealing sequence must satisfy two strict safety regulations:
1. You may never seal any of the **t** *critical reservoirs*, as they are required for the final system.
2. After every individual sealing step, the subset of remaining unsealed reservoirs must still be *fully mixable*. If sealing a reservoir would leave the remaining unsealed reservoirs unable to share substances between some pair of remaining unsealed reservoirs using only the remaining pipes, that reservoir cannot be sealed at that time.

You can stop the sealing process at any point, including making no sealings at all. Your objective is to determine the minimum possible total maintenance cost of the mixing pipes that remain active in the system when you finish.

## Input

The first line provides three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1).
The second line provides **t** distinct integers representing the indices of the critical reservoirs.
Each of the subsequent **m** lines provides three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), indicating a mixing pipe between reservoir **u** and reservoir **v** with a maintenance cost of **w**.

## Output

Output a single integer representing the minimum possible total maintenance cost of the remaining mixing pipes after a valid sequence of sealings.

## Examples

### Example 1

**Input**
```
4 3 2
1 4
1 2 5
2 3 1
3 4 2
```

**Output**
```
8
```

### Example 2

**Input**
```
5 4 1
3
1 2 4
2 3 6
3 4 2
4 5 9
```

**Output**
```
0
```

### Example 3

**Input**
```
3 2 3
1 2 3
1 2 4
2 3 5
```

**Output**
```
9
```