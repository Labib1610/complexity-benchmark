# Problem A — Core Network Integration

Time limit: 5 s   Memory limit: 256 MB

## Description

A campus network consists of **n** sites (numbered 1 through **n**). Certain pairs of sites share a potential cabling link, which requires a specific cost to activate. Out of the **n** sites, a highly restricted subset of **t** sites are designated as *required* sites. These required sites represent the primary infrastructure and must all end up in the same connected group, meaning every required site must be able to communicate with every other required site via some sequence of activated links. The remaining sites are optional; they may be safely ignored, or they may be used as relays if routing through them is cheaper than connecting the required sites directly.

Because the number of required sites **t** is extremely small (at most 10), the mandatory connections are highly localized. You might consider simply finding the cheapest direct route between each pair of required sites and activating all links on those routes. However, when routes merge at an optional site, the shared links only need to be paid for once. Therefore, you can often achieve a lower total cost by carefully selecting a few optional sites to act as branching hubs.

Your task is to determine the absolute minimum total cost to activate a set of links such that all **t** required sites are connected.

## Input

The first line contains three integers **n**, **m**, and **t** (1 ≤ **t** ≤ 10, 1 ≤ **n** ≤ 100, 0 ≤ **m** ≤ **n**·(**n**−1)/2).
The second line contains **t** distinct integers: the identifiers of the required sites.
Each of the next **m** lines contains three integers **u**, **v**, and **w** (1 ≤ **u**, **v** ≤ **n**, **u** ≠ **v**, 1 ≤ **w** ≤ 1000000), representing a potential cabling link between site **u** and site **v** with an activation cost of **w**.
It is guaranteed that the provided links are sufficient to connect all required sites.

## Output

Print a single integer: the minimum total cost to connect all required sites.

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

In Example 1, routing the connections through the optional relay site 4 (which costs 1+1+1 = 3) is cheaper than joining the three required sites using only their direct links (which would cost 4). In Example 3, there is only one required site, so no cabling is needed.
