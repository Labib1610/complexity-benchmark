# Problem A — Frequency Allocation for Relay Networks

Time limit: 5 s   Memory limit: 256 MB

## Description
A communications network consists of **n** relay stations and **m** bidirectional data links.
The network topology is uniform: every relay station is an endpoint for exactly **K** data links, where **K** = 2**m**/**n**.
To prevent signal interference, each data link must be assigned a single frequency band. There are exactly **K** distinct frequency bands available, numbered 1 to **K**.

Interference occurs if any two data links connected to the same relay station operate on the same frequency band. Therefore, all **K** links connected to a given station must be assigned mutually distinct frequency bands. (Because there are exactly **K** links per station and exactly **K** bands available, every station must see every band exactly once). The physical distance of the links and their capacities do not affect the allocation.

It is guaranteed by the network's design that **m** ≤ 3000. 

Given the network topology, determine if it is possible to assign a frequency band to each data link under these conditions.

## Input
The first line contains two integers **n** and **m** (**n** is even, **m** = 3**n**/2, 2 ≤ **n** ≤ 2000).
Each of the following **m** lines contains two integers u and v (1 ≤ u < v ≤ **n**), representing a data link between station u and station v.

## Output
If a valid assignment exists, print `YES` on the first line. On the second line, print **m** integers, each between 1 and **K**, representing the frequency band assigned to each link in the order they appear in the input.
Otherwise, print `NO`.

## Example
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
YES
1 2 3 3 2 1
```
