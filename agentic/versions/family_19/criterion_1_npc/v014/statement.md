# Multi-Good Logistics Planning over a Shared Network

Time limit: 5 s   Memory limit: 256 MB

## Description
A logistics network consists of $n$ distribution centers connected by $m$ one-way transit corridors. Each corridor has a physical limit on the total number of shipping units it can process in a single operational window. This limit restricts the aggregate traffic on that corridor across all goods. 

There are $k$ different types of goods to be transported. For each good, a fixed number of indivisible shipping units must be relocated from a specific source center to a specific target center. All goods must be shipped simultaneously within the same operational window. Because the corridors are shared, the units of different goods traveling through the same corridor collectively consume its available processing limit. 

When goods pass through any center other than their designated source or target, they cannot be stored or consumed: the number of units of a specific good arriving at the center must exactly equal the number of units of that same good departing from it. At a good's source center, exactly its required shipment size must be sent out into the network, and at its target center, exactly that shipment size must be received. 

Determine whether it is possible to route all required units of all goods through the network in a single operational window such that no corridor's processing limit is exceeded by the combined traffic it carries. If it is possible, provide a valid routing plan.

## Input
The first line contains three integers $n$, $m$, and $k$, representing the number of centers, corridors, and goods.
The following $k$ lines each contain three integers $s_i$, $t_i$, and $d_i$, specifying the source center, target center, and the required number of units for the $i$-th good.
The next $m$ lines each contain three integers $u$, $v$, and $c$, indicating a one-way corridor from center $u$ to center $v$ with a processing limit of $c$ units.

## Output
If a valid routing plan exists, print `YES` on the first line. Then, print $k$ lines. The $i$-th of these lines should contain $m$ non-negative integers, where the $j$-th integer represents the number of units of the $i$-th good routed through the $j$-th corridor (in the order the corridors were given in the input).
If no such plan is possible, print `NO`.

## Example

**Input:**
```
4 5 2
1 4 2
1 3 1
1 2 2
2 3 1
3 4 2
1 4 1
2 4 1
```

**Output:**
```
YES
1 0 0 1 1
1 1 0 0 0
```
