# Problem B — Canal Convoy

Time limit: 1 s   Memory limit: 256 MB

## Description

A fleet of **j** vessels must be organized for a canal crossing. You must arrange the fleet into a strict sequence, determining exactly which vessel is first, second, and so on.

For each vessel, the crossing involves two sectors: the Alpha sector and the Beta sector. You are provided the transit time through the Alpha sector, **t1**, and the transit time through the Beta sector, **t2**, for each vessel.

A safety protocol defines the *exposure rating* of the fleet based on your chosen sequence. To evaluate this rating, the protocol considers every position $k$ (where $k$ ranges from $1$ to $j$) in your sequence as a potential 'pivot'. 

For a specific pivot position $k$, its *chain duration* is calculated as:
- The sum of the Alpha sector transit times of all vessels from position $1$ up to position $k$ of your sequence (inclusive).
- PLUS the sum of the Beta sector transit times of all vessels from position $k$ up to position $j$ of your sequence (inclusive).

The *exposure rating* of the entire fleet sequence is defined as the maximum *chain duration* calculated among all $j$ possible choices for the pivot position $k$.

Your task is to determine the optimal sequence of the fleet that minimizes this overall *exposure rating*.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the next **j** lines contains exactly 2 integers **t1** and **t2** (1 ≤ t1, t2 ≤ 1000000): the Alpha sector transit time and the Beta sector transit time of a vessel.

## Output

Print a single integer: the smallest possible *exposure rating* you can achieve by optimally sequencing the fleet.

## Examples

### Example 1

**Input**
```
3
3 2
2 4
1 3
```

**Output**
```
10
```

### Example 2

**Input**
```
1
5 3
```

**Output**
```
8
```

### Example 3

**Input**
```
3
2 2
2 2
2 2
```

**Output**
```
8
```

## Note

In Example 2, there is only one vessel ($j=1$). The only possible pivot is $k=1$. The chain duration for $k=1$ is the Alpha transit time of the first vessel (5) plus the Beta transit time from position 1 onwards (3). The exposure rating is therefore 5 + 3 = 8.