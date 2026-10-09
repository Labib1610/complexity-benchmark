# Problem A — Command Center Routing

Time limit: 5 s   Memory limit: 256 MB

## Description

A communication network is composed of **n** relay stations (identified by integers 1 through **n**). Between specific pairs of these stations, it is possible to construct a bidirectional transmission corridor. Each potential corridor has an associated resource expenditure required for its construction.

Within this network, exactly **t** of the stations are designated as command centers. A functional network configuration dictates that every command center must be able to exchange data with every other command center. This exchange can occur directly or be routed through any number of established corridors. Stations that are not command centers do not share this requirement; they may be left entirely disconnected, or they may be incorporated into the configuration as intermediate routing points.

Your task is to calculate the minimum total resource expenditure needed to construct a set of corridors that achieves a functional network configuration.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers: the identifiers of the command centers.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), representing a potential corridor between stations **u** and **v** requiring a resource expenditure of **w**.
The provided potential corridors are guaranteed to be sufficient to establish a functional network configuration.

## Output

Print a single integer: the minimum total resource expenditure required to construct a valid configuration.

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

In Example 1, routing through station 4 (which is not a command center) requires an expenditure of 1+1+1 = 3, which is more efficient than connecting the three command centers directly (which would require an expenditure of 4). In Example 3, there is only one command center, so no corridors need to be constructed.
