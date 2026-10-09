# Problem A — Concurrent Resource Transit over a Shared Compartment Network

Time limit: 5 s   Memory limit: 256 MB

## Description
A space station operates an asymmetric network of compartments linked by one-way transfer tubes. Each tube has a maximum threshold on how many sealed canisters can transit through it per maintenance cycle, regardless of their contents. This threshold reflects the tube's structural tolerance and cannot be exceeded.

In the current cycle, there are several distinct resource types to relocate. Each resource type has its own source compartment, its own target compartment, and a firm requirement—expressed in whole canisters—that must be fully relocated during this single cycle. Crucially, all resource types utilize the same network of tubes: a tube's threshold applies to the combined canister count of every resource type passing through it. Thus, different resources compete for the shared structural tolerance even though they are otherwise independent. Canister counts are indivisible; the number of canisters of any given resource type sent through any given tube is a non-negative integer.

Canisters are neither created nor destroyed at any compartment that is neither a resource type's source nor its target: for each resource type individually, the number of canisters of that type entering an intermediate compartment must exactly equal the number leaving it. At a resource type's source, the net outflow of that type equals its required quantity, and at its target, the net inflow equals that quantity. 

To comply with station safety protocols, the following architectural conditions are guaranteed:
1. The sum of the tube connection counts (incoming plus outgoing) across all $n$ compartments is exactly $2m$.
2. For any valid transit plan, the total aggregate number of canisters entering all compartments combined will exactly equal the total aggregate number of canisters leaving all compartments combined.

Generate a transit plan that relocates every resource type's full requirement while respecting every tube's shared threshold, or determine that the network cannot support all relocations simultaneously in one cycle. (Relocating any single resource type alone may be trivial; the difficulty is that the resources must coexist within the shared thresholds.)

## Input
Line 1: Three integers $n$, $m$, and $k$, representing the number of compartments, transfer tubes, and resource types, respectively.
Next $k$ lines: Three integers $s_i$, $t_i$, and $d_i$, representing the source compartment, target compartment, and required canister quantity for resource type $i$.
Next $m$ lines: Three integers $u$, $v$, and $cap$, representing a one-way transfer tube from compartment $u$ to compartment $v$ with a maximum threshold of $cap$ canisters.

## Output
If a valid transit plan exists, print `YES` on the first line. Then print $k$ lines, each containing $m$ integers. The $j$-th integer on the $i$-th line should represent the number of canisters of resource type $i$ sent through the $j$-th transfer tube (in the order they appeared in the input).
If no such plan exists, print `NO`.

## Example

**Input:**
```
4 5 2
1 4 10
2 3 5
1 2 10
2 4 10
1 3 5
3 4 5
2 3 5
```

**Output:**
```
YES
5 5 5 5 0
0 0 0 0 5
```
