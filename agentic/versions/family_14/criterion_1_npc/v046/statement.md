# Problem A — Secure Compliance Network

Time limit: 5 s   Memory limit: 256 MB

## Description

A financial firm operates **n** regional offices, numbered 1 through **n**. To comply with new regulations, a specific subset of **t** offices must share a secure, continuous communication network. 

A telecommunications provider offers **m** potential point-to-point links between specific pairs of offices, each carrying a fixed installation fee. You may select any combination of these links. The network is compliant as long as all **t** regulated offices can transmit data to one another, whether directly or by passing data through intermediate offices. Any of the remaining unregulated offices can serve as these intermediate routing points if leasing links through them reduces the overall expense. 

Determine the minimum total installation fee required to establish a compliant network connecting all **t** regulated offices.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers: the identifiers of the regulated offices.
Each of the following **m** lines provides three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), indicating a potential link between office **u** and office **v** with an installation fee of **w**.
It is guaranteed that the available links are sufficient to connect all regulated offices.

## Output

Print a single integer: the minimum total installation fee to connect all regulated offices.

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

In Example 1, routing the network through the unregulated office 4 incurs a fee of 1+1+1 = 3, which is cheaper than linking the three regulated offices directly (which would cost 4). In Example 3, there is only one regulated office, so no links are needed.
