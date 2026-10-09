# Phase II: Backbone Commissioning

Time limit: 5 s   Memory limit: 256 MB

## Description

A regional authority is executing a three-phase infrastructure upgrade across a network of **n** distinct sites. 

Phase I consisted of an extensive terrain survey. Surveyors identified **t** mandatory synchronization hubs among the sites. They also mapped out **m** viable segments for laying high-capacity conduit between specific pairs of sites, determining a fixed installation cost for each segment. This survey is now complete and the data has been handed off to you.

Your task is to execute Phase II: Backbone Commissioning. You must select a subset of the viable conduit segments to install such that every mandatory synchronization hub can seamlessly transmit data to every other mandatory hub. Transmission is possible if there is a continuous sequence of installed conduit segments connecting them. 

The remaining sites (those not designated as mandatory hubs) are classified as routine sites. In Phase II, you are authorized to route the conduit sequence through any routine sites, or bypass them entirely, depending on what minimizes the overall installation expenditure. You must calculate the lowest possible total cost to successfully complete Phase II.

Phase III will later deploy localized wireless meshes at each site. The budget for Phase III is handled independently, so your calculations must only reflect the conduit installation costs incurred during Phase II.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ t ≤ 10, 1 ≤ n ≤ 100, 0 ≤ m ≤ n·(n−1)/2).
The second line contains **t** distinct integers: the identifiers of the mandatory synchronization hubs.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ u, v ≤ n, u ≠ v, 1 ≤ w ≤ 1000000), representing a viable conduit segment connecting site **u** and site **v** with a Phase II installation cost of **w**.
It is guaranteed that the provided segments are sufficient to allow all mandatory hubs to communicate.

## Output

Print a single integer representing the minimum total cost to complete Phase II.

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

In Example 1, completing Phase II by routing the conduit through routine site 4 incurs a cost of 1 + 1 + 1 = 3. This is more economical than linking the three mandatory hubs exclusively among themselves, which would require an expenditure of at least 4. In Example 3, there is only one mandatory hub, so Phase II requires no conduit installations.
