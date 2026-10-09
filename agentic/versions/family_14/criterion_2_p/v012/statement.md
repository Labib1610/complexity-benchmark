# Problem B — Priority Campus Communications

Time limit: 2 s   Memory limit: 256 MB

## Description

A campus consists of **n** facilities, numbered 1 through **n**. You are provided a list of **m** potential communication links that can be activated. Each link joins a specific pair of facilities and requires a certain cost to activate.

The layout of these potential links follows strict planning rules:
1. There are exactly **m = n − 1** potential links in total across the campus.
2. It is possible for a message to travel between any two facilities in the campus by hopping across one or more of these potential links.

A number of facilities, **t**, are designated as priority centers. Your task is to activate a subset of the potential links so that every priority center can exchange messages with every other priority center. Messages can be routed through non-priority facilities if necessary.

Determine the minimum total cost of the links you must activate to ensure all priority centers are mutually connected.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ n, 1 ≤ n ≤ 200000, m = n − 1).
The second line contains **t** distinct integers: the identification numbers of the priority centers.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), indicating a potential link between facility **u** and facility **v** with an activation cost of **w**. It is guaranteed that the links follow the planning rules described above.

## Output

Print a single integer representing the minimum total cost to activate links such that all priority centers can communicate with each other.

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

In Example 1, the priority centers 1 and 4 can only communicate if the messages pass through facilities 2 and 3. Therefore, all three available links (costs 5, 1, and 2) must be activated, giving a total cost of 8.
In Example 2, there is only one priority center, so no links need to be activated and the total cost is 0.
