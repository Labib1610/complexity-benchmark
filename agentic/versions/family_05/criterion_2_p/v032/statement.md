# Problem B — Orbital Synchronization

Time limit: 2 s   Memory limit: 256 MB

## Description

A constellation of $k$ satellites must be synchronized. An operational link requires three components: a ground station (numbered 1 to $k$), an encryption key (numbered 1 to $k$), and a satellite (numbered 1 to $k$).

You are provided with a catalog of $t$ tested links, each specified as a triplet $(x, y, z)$ representing a ground station, an encryption key, and a satellite. Your goal is to select exactly $k$ links from this catalog to form a complete network. 

To form a complete network, the selected subset of $k$ links must be perfectly balanced: every ground station, every encryption key, and every satellite must be utilized in exactly one of the chosen links. Evaluating every possible subset of size $k$ from the catalog involves a vast number of combinations, so you must carefully determine if a valid configuration exists. 

Hardware constraints dictate that any tested link involving a particular ground station will always use the same encryption key, and no two ground stations are paired with the same encryption key. You must sift through the available options to find a selection of links that satisfies all requirements.

## Input

The first line contains two integers $k$ and $t$ ($1 \le k \le 1200$, $0 \le t \le k \cdot k$): the quantity of each component type and the number of tested links in the catalog.

Each of the next $t$ lines contains three integers $x$, $y$, and $z$ ($1 \le x, y, z \le k$), defining a tested link between ground station $x$, encryption key $y$, and satellite $z$. No link appears more than once. As dictated by the hardware constraints, all links in the input for a specific ground station will feature the same encryption key, and different ground stations will feature different encryption keys.

## Output

If a valid selection of $k$ links exists that forms a complete network, print `YES` on the first line. Then, output $k$ lines, each containing the three integers $x\ y\ z$ of one selected link (in any order). Any valid selection is accepted.

If no valid selection exists, print `NO`.

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
