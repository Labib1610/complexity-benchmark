# Synthesis Pipeline

Time limit: 2 s
Memory limit: 256 MB

## Description

An experimental apparatus consists of **n** sealed chambers, numbered 1 to **n**. Within this apparatus, exactly **t** specific chambers contain reactive agents. For a successful experiment, all **t** of these agents must be able to freely mix with one another.

You are given a list of **m** available connecting tubes. Each tube connects two chambers and requires a specific amount of energy to unseal. Once unsealed, fluid can flow through the tube in either direction. You may unseal any combination of the available tubes. The agents will successfully mix if, for every pair of chambers containing an agent, fluid can travel between them through a series of unsealed tubes. Chambers without reactive agents can safely serve as transit junctions.

Your objective is to determine the minimum total energy required to unseal a set of tubes that allows all **t** reactive agents to mix.

To ensure the experiment is theoretically possible, the apparatus was designed such that it has exactly **m** = **n** - 1 available tubes, and unsealing all of them would provide a continuous fluid route between any two chambers in the entire system.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ **t** ≤ **n**, 1 ≤ **n** ≤ 200000, **m** = **n** - 1).
The second line contains **t** distinct integers: the identifiers of the chambers containing reactive agents.
Each of the next **m** lines provides three integers **u**, **v**, and **w** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**, 1 ≤ **w** ≤ 1000000), representing an available tube between chamber **u** and chamber **v** that requires **w** energy to unseal.
It is guaranteed that unsealing all **m** tubes allows fluid to travel between any two of the **n** chambers.

## Output

Print a single integer: the minimum total energy required to allow all **t** reactive agents to mix.

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
