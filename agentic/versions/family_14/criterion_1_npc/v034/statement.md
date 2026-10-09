# Problem A — Establishing the Command Network

Time limit: 5 s
Memory limit: 256 MB

## Description

A research facility consists of several modules. Certain pairs of modules share a dormant communication interface. You can activate any such interface by paying a specific fee, which allows two-way data to stream between the two modules.

The facility's administration has designated a specific subset of modules as priority command centers. Your task is to ensure that data can successfully stream between every pair of priority command centers. Data can be passed along through any sequence of active interfaces and intermediate modules. You may choose to activate interfaces involving non-priority modules if doing so provides a cheaper way to pass data between the priority ones, or you may ignore non-priority modules entirely.

Determine the lowest total fee required to activate a set of interfaces such that all priority command centers can stream data to one another.

## Input

The first line contains three integers **n**, **m**, and **t**. The total number of modules **n** is between 1 and the facility's maximum architectural capacity of 100. The number of available interfaces **m** ranges from 0 up to the theoretical limit where every pair of modules shares one, which is **n**·(**n**−1)/2. The number of priority command centers **t** ranges from 1 up to the maximum number of executive overrides, which is 10.

The second line contains **t** distinct integers: the identifiers of the priority command centers.

Each of the next **m** lines contains three integers **u**, **v**, and **w**. These indicate that the distinct modules **u** and **v** (both between 1 and **n**) share a dormant interface that requires an activation fee of **w**. The fee is at least 1 and capped at the administrative limit of 1000000.

It is guaranteed that the available interfaces are sufficient to achieve the goal.

## Output

Print a single integer: the lowest total fee to activate a valid set of interfaces.

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

In Example 1, passing data through the non-priority module 4 (which costs 1+1+1 = 3) is cheaper than activating interfaces to link the three priority command centers directly (which would cost 2+2 = 4). In Example 3, there is only one priority command center, so no interfaces need to be activated.
