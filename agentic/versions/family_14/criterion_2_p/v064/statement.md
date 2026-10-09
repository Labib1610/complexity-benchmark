# Minimum Activation Fee for Secure Routing

Time limit: 2 s   Memory limit: 256 MB

## Description

A corporate infrastructure consists of **n** regional offices. To establish secure communications, the corporation has physically laid **m** dedicated point-to-point fiber connections between certain pairs of offices. The connections are laid out such that between any two offices, there is exactly one sequence of connections that can link them.

Each connection has a specific activation fee. A new high-security project involves **t** specific offices. These **t** offices must all be able to exchange data with each other using only activated connections. Intermediate offices along the routes do not need to be part of the project, but connections routing through them can be activated to bridge the required offices.

You must select which connections to activate to satisfy this communication requirement for the lowest possible total activation fee.

## Input

The first line provides three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1), representing the number of offices, the number of available connections, and the number of project offices.
The second line provides **t** distinct integers representing the identifiers of the project offices.
Each of the following **m** lines provides three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), indicating a fiber connection between office **u** and office **v** with an activation fee of **w**.

## Output

Output a single integer representing the minimum total activation fee required to connect all **t** project offices.

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

In Example 1, the project offices 1 and 4 can only communicate by routing through offices 2 and 3, meaning all three connections (fees 5, 1, and 2) must be activated for a total of 8. In Example 2, the project only involves a single office, so no connections need to be activated.
