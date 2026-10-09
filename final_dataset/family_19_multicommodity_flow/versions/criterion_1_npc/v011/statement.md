# Problem A — Seasonal Wildlife Relocation

Time limit: 5 s
Memory limit: 256 MB

## Description
A conservation network consists of a set of wildlife reserves connected by one-way ecological corridors. During the annual migration season, animals move between these reserves. Each corridor has a strict ecological carrying capacity, representing the maximum total number of animals that can travel through it in a single season. This limit applies to the sum of all animals, regardless of their species.

This season, there are several distinct species that need to be relocated. Each species has a specific starting reserve, a designated target reserve, and an exact number of individuals that must successfully complete the journey. The carrying capacity of the corridors is shared among all species, meaning different species simultaneously compete for the same passage limits. Since we are tracking individual animals, the number of animals of any species using a corridor must be a non-negative whole number.

Animals do not settle in intermediate reserves. For every species, the number of individuals arriving at any reserve (other than their starting or target reserve) must exactly equal the number of individuals departing from it. At a species' starting reserve, the outgoing count minus the incoming count must equal its required relocation number. Similarly, at the target reserve, the net incoming count must equal this relocation number.

Determine if there is a valid movement plan that successfully relocates all individuals of every species without exceeding the carrying capacity of any corridor.

## Input
Line 1: Three integers $n$ (number of reserves), $m$ (number of corridors), and $k$ (number of species).
Next $k$ lines: Three integers $s_i$ (starting reserve), $t_i$ (target reserve), and $d_i$ (number of individuals to relocate) for the $i$-th species.
Next $m$ lines: Three integers $u$, $v$, and $cap$, representing a one-way corridor from reserve $u$ to reserve $v$ with a carrying capacity of $cap$ animals.

## Output
If a valid relocation plan exists, print `YES`. Then, print $k$ lines, each containing $m$ integers. The $i$-th line should list the number of individuals of species $i$ passing through each of the $m$ corridors, in the exact order the corridors were given in the input.
If no such plan is possible, print `NO`.

## Example

**Input:**
```
4 5 2
1 4 2
2 3 1
1 2 2
2 4 1
1 3 1
3 4 2
2 3 1
```

**Output:**
```
YES
1 1 1 1 0
0 0 0 0 1
```
