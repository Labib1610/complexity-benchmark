# Problem A — Private Data Exchange

Time limit: 5 s   Memory limit: 256 MB

## Description

A logistics company operates facilities in **n** cities (numbered 1 to **n**). Following a recent acquisition, they must establish a continuous private data exchange network that links **t** specific critical facilities. 

The telecommunications provider offers dedicated point-to-point leased lines between certain pairs of facilities, each with a known monthly lease cost. The company may lease any subset of these available lines. They can route the data exchange through other non-critical facilities if it results in a cheaper overall network. The network is successfully established as long as there is a path of leased lines connecting every critical facility to every other critical facility. 

Determine the minimum total monthly lease cost of the chosen lines required to link all **t** critical facilities.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers: the facility IDs of the critical facilities.
Each of the following **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), indicating that a dedicated leased line can be established between facility **u** and facility **v** for a monthly lease cost of **w**.
It is guaranteed that the available lines are sufficient to link all critical facilities.

## Output

Print a single integer: the minimum total monthly lease cost of the chosen lines to establish the network linking all critical facilities.

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

In Example 1, routing the network through the non-critical facility 4 incurs a total lease cost of 1+1+1 = 3, which is more cost-effective than linking the three critical facilities directly (which would cost 4). In Example 3, there is only one critical facility, so no leased lines are required.
