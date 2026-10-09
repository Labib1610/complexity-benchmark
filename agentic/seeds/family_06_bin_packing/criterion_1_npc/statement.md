# Problem A — Cargo Loading

Time limit: 5 s   Memory limit: 256 MB

## Description

A dispatch bay must load **n** indivisible parcels, parcel i of weight w[i], into identical containers of capacity **C**. Each parcel goes wholly into one container and no container may exceed C. The bay wants to minimise how many containers leave the dock, and must report that minimum together with a loading achieving it. Parcel shapes, loading order, and handling time are irrelevant; only weights and capacity bind. Filling containers greedily rarely reaches the true minimum, because a locally sensible placement can waste capacity a different grouping would have used. Report the fewest containers needed and one valid assignment achieving it.

## Input

The first line contains two integers **n** and **C** (1 ≤ n ≤ 28, 1 ≤ C ≤ 1 000 000 000).
The second line contains **n** integers **w[1] … w[n]** (1 ≤ w[i] ≤ C), the item weights.

## Output

On the first line print the minimum number of containers needed.
On the second line print **n** integers where the i-th integer is the container number (from 1 to that minimum) holding item i. Any loading that uses the minimum number of containers and never exceeds capacity C is accepted.

## Examples

### Example 1

**Input**
```
4 10
6 5 4 5
```

**Output**
```
2
1 2 1 2
```

### Example 2

**Input**
```
3 10
7 7 7
```

**Output**
```
3
1 2 3
```

### Example 3

**Input**
```
1 5
5
```

**Output**
```
1
1
```

## Note

In Example 1, two containers suffice: {6, 4} = 10 and {5, 5} = 10. In Example 2, three weight-7 items cannot share a capacity-10 container, so three containers are needed.
