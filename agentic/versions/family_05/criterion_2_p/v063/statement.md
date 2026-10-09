# Problem B — Orbital Synchronization

Time limit: 2 s   Memory limit: 256 MB

## Description

A space agency is deploying a constellation of $k$ satellites. To establish a fully operational network, exactly $k$ communication links must be activated. A single link requires three distinct components: a ground station, an encryption key, and a satellite. 

You are given a catalog of $t$ successfully tested links. Each entry in the catalog is a triplet $(x, y, z)$ specifying the ground station, the encryption key, and the satellite involved. 

Your objective is to choose exactly $k$ links from this catalog to form a complete, balanced network. In a complete network, every individual ground station, every encryption key, and every satellite must be utilized in exactly one active link. 

Due to strict hardware manufacturing constraints, a specific ground station is permanently hardwired to use exactly one specific encryption key. Furthermore, no two ground stations are hardwired to the same encryption key. You must analyze the catalog and find a selection of links that fulfills all requirements.

## Input

The first line contains two integers $k$ and $t$. The quantity of each component type, $k$, is at least one and will not exceed the number of months in a century. The catalog contains a non-negative number of tested links, $t$, which is bounded by the maximum theoretical limit of testing every ground station with every satellite.

Each of the subsequent $t$ lines provides three integers $x$, $y$, and $z$, representing a tested link between ground station $x$, encryption key $y$, and satellite $z$. Component IDs are numbered starting from 1 up to the total component count $k$. No link is listed more than once. Adhering to the hardware constraints, all catalog entries involving a given ground station will always feature the identical encryption key, and different ground stations will always feature distinct encryption keys.

## Output

If it is possible to select $k$ links that form a complete network, output `YES` on the first line. Then, output $k$ lines, each containing the three integers $x\ y\ z$ of one chosen link. The links can be printed in any order. Any valid selection is acceptable.

If no such configuration is possible, output `NO`.

## Examples

### Example 1

**Input**
```
2 3
1 1 1
1 1 2
2 2 2
```

**Output**
```
YES
1 1 1
2 2 2
```

### Example 2

**Input**
```
2 2
1 1 1
2 2 1
```

**Output**
```
NO
```

### Example 3

**Input**
```
1 1
1 1 1
```

**Output**
```
YES
1 1 1
```
