# Broadcast Synchronization

Time limit: 5 s   Memory limit: 256 MB

## Description

A film crew is broadcasting an event from a stadium equipped with **n** junction boxes, numbered 1 to **n**. Certain pairs of junction boxes can be connected by laying a fiber-optic cable, which incurs a specific setup cost based on distance and routing difficulty.

The crew has mounted cameras at **t** specific junction boxes. To perfectly synchronize the video feeds, all **t** camera boxes must be linked into a single continuous communication network. The synchronization signal can pass through any junction box, meaning the crew is free to route cables through any of the remaining **n** - **t** boxes if it results in a cheaper overall network, or they can ignore them entirely.

Determine the lowest possible total setup cost to lay down a network of cables that connects all **t** camera boxes.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2), representing the total number of junction boxes, the number of possible cable routes, and the number of camera boxes, respectively.

The second line contains **t** distinct integers: the numerical IDs of the junction boxes where cameras are mounted.

Each of the following **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), indicating that a cable can be laid between junction box **u** and junction box **v** for a setup cost of **w**.

It is guaranteed that the available cable routes are sufficient to connect all camera boxes.

## Output

Print a single integer: the minimum total setup cost to connect all camera boxes together.

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

In Example 1, routing cables through the unused junction box 4 costs 1 + 1 + 1 = 3. This is cheaper than connecting the three camera boxes directly to each other, which would cost at least 4. In Example 3, there is only one camera box, so it is already synchronized with itself and no cables need to be laid.
