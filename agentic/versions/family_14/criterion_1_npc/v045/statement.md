# Problem A — Deep-Sea Integration

Time limit: 5 s   Memory limit: 256 MB

## Description

A deep-sea research facility consists of several habitat modules (numbered starting from 1). The facility is built within a designated trench that contains exactly 100 viable anchor points, meaning the total number of installed modules will never exceed this capacity.

A subset of these modules house life-support cores. Due to fluid circulation limits, a single integrated network can support a maximum of 10 life-support cores. The goal is to establish a unified life-support network so that every core is connected to every other core, either directly or via intermediate modules. You achieve this by deploying reinforced umbilical tubes between pairs of modules.

Some modules do not have life-support cores and serve only as observation posts. You are permitted to route the network through these observation posts if it results in a more cost-effective overall design, or you may bypass them entirely.

Each potential umbilical tube has a specific material expense associated with it. A single tube's expense is at least 1 and will never exceed the maximum insured value of 1,000,000 credits.

Find a configuration of umbilical tubes that interconnects all life-support cores while minimizing the total material expense.

## Input

The first line contains three integers **n**, **m**, and **t**.
- **n** is the total number of habitat modules (a positive integer up to the trench capacity).
- **m** is the number of potential umbilical tubes (a non-negative integer up to the maximum possible number of distinct pairs of modules).
- **t** is the number of life-support cores (a positive integer up to the circulation limit).

The second line contains **t** distinct integers: the identifiers of the modules equipped with life-support cores.

Each of the next **m** lines contains three integers **u**, **v**, and **w**, describing a potential tube between module **u** and module **v** (distinct identifiers from 1 to **n**) with a material expense of **w** (a positive integer up to the maximum insured value).

The available tube options are guaranteed to be sufficient to interconnect all life-support cores.

## Output

Print a single integer: the minimum total material expense to interconnect all life-support cores.

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

In Example 1, routing the network through the observation post at module 4 (which costs 1+1+1 = 3) is cheaper than connecting the three life-support cores directly (which would cost 4). In Example 3, there is only one life-support core, so no umbilical tubes are necessary.
