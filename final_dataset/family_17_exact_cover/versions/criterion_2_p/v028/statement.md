# Problem B — Symbiotic Habitat Allocation

Time limit: 2 s   Memory limit: 256 MB

## Description
A major conservation initiative aims to preserve a delicate ecosystem consisting of night-blooming flora and their associated fauna. The collection holds a specific number of distinct flower species, identified by sequential tags starting from 1. There is an exactly equal number of distinct moth species, identified by sequential tags continuing immediately after the highest flower tag.

To ensure the survival of all collected species, researchers must establish a series of isolated greenhouse habitats. Each habitat must contain exactly two species: one flower and one moth. However, a habitat will only thrive if its two inhabitants are biologically compatible. Extensive field observations have produced a registry of viable pairings between specific flowers and specific moths. This registry contains numerous viable pairings, often with a single flower species compatible with multiple moth species and vice versa. The frequency or order of these documented pairings has no bearing on their viability; unlisted pairings are strictly non-viable.

The conservation directive mandates that every single flower species and every single moth species in the collection must be placed into a thriving habitat. Consequently, researchers must select a set of viable pairings from the registry such that each flower species and each moth species is assigned to exactly one habitat. No species can be left out, and no species can be placed in more than one habitat.

Determine if it is possible to fulfill this directive using the provided registry of viable pairings. If an allocation exists that encompasses all species exactly once, output it. Otherwise, indicate that the collection cannot be fully preserved under these conditions.

## Input
The first line provides two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), representing the number of flower species (which is also the number of moth species) and the number of viable pairings in the registry, respectively.
The following $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), indicating that flower species $a$ and moth species $b$ are biologically compatible.

## Output
If a complete and valid allocation is possible, print `YES` on the first line, followed by $q$ lines each containing the two integers of a selected pairing. If no such allocation exists, print `NO`.

## Example

### Input
```
3 5
1 4
1 5
2 5
3 5
3 6
```

### Output
```
YES
1 4
2 5
3 6
```
