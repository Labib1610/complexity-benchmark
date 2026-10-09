# Priority Site Connectivity

Time limit: 2 s   Memory limit: 256 MB

## Description

An infrastructure project defines **n** substations, indexed from 1 to **n**. You are provided with a list of **t** substations designated as priority locations. There are also **m** proposed communication lines, each connecting a pair of substations for a specific resource cost. 

The proposed lines are arranged such that a signal can be routed between any two substations via exactly one unique sequence of lines.

Your task is to determine the minimum total resource cost required to activate a subset of lines such that all priority substations can communicate with one another, either directly or by relaying through other substations.

## Input

The first line contains three integers **n**, **m**, and **t**. The total number of substations **n** is at least 1 and restricted by the network capacity of 200000. The number of proposed lines **m** is exactly **n** - 1. The number of priority substations **t** is at least 1 and at most **n**.

The second line contains **t** distinct integers: the indices of the priority substations.

The following **m** lines each contain three integers **u**, **v**, and **w**. These specify a proposed line between substation **u** and substation **v** (with **u** and **v** being distinct integers from 1 to **n**) having a resource cost of **w** (an integer from 1 to the maximum component budget of 1000000).

## Output

Print a single integer representing the minimum total resource cost required to link all priority substations.

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

## Note

In Example 1 the priority substations 1 and 4 are joined only through 2 and 3, so all three lines (5+1+2 = 8) are needed. In Example 2 there is one priority substation, so no lines are needed.