# Problem B — Spaceport Clearance

Time limit: 1 s   Memory limit: 256 MB

## Description

You are managing the arrival of **j** starships. Each starship has an atmospheric entry duration (**p1**) and a landing duration (**p2**).

You must arrange all **j** starships into a single sequence. Let the chosen sequence of starships be placed into positions $1, 2, \dots, j$, where $p1_i$ and $p2_i$ are the durations for the starship assigned to position $i$.

For your chosen sequence, the timeline value $T(k)$ at any position $k$ ($1 \le k \le j$) is defined as:

$T(k) = \sum_{i=1}^{k} p1_i + \sum_{i=k}^{j} p2_i$

Note that the durations for the starship at index $k$ are included in both sums. 

The overall clearance time of your sequence is the maximum value of $T(k)$ over all possible choices of $k$ from $1$ to $j$. 

Find an ordering of the starships that makes their overall clearance time as small as possible, and report this smallest possible time.

## Input

The first line contains a single integer **j** (1 ≤ j ≤ 200000).
Each of the next **j** lines contains two integers **p1** and **p2** (1 ≤ p1, p2 ≤ 1000000): the atmospheric entry duration and the landing duration of a starship.

## Output

Print a single integer: the smallest possible overall clearance time.

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

In Example 2, there is only 1 starship. For the only position $k=1$, $T(1) = p1_1 + p2_1 = 5 + 3 = 8$. The clearance time is 8.