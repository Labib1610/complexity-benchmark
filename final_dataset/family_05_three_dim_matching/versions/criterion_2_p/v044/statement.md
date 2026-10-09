# Problem B — Network Triad Activation

Time limit: 2 s   Memory limit: 256 MB

## Description

A secure communications array consists of $3k$ discrete components divided into three distinct pools, each containing exactly $k$ elements:
- $k$ Data Sources, numbered 1 to $k$,
- $k$ Encryption Modules, numbered 1 to $k$,
- $k$ Transmission Channels, numbered 1 to $k$.

To initialize the array, you must select exactly $k$ active routing triads. A routing triad is a specific combination of one Data Source, one Encryption Module, and one Transmission Channel. 

You are provided with a list of $t$ viable triads that have passed signal integrity testing. Your objective is to select a subset of exactly $k$ triads from this list such that every Data Source, every Encryption Module, and every Transmission Channel is included in exactly one selected triad. 

Due to the manufacturer's physical architecture, each Data Source is hardwired to a single Encryption Module, and no two Data Sources are wired to the same module. Consequently, in all viable triads involving a particular Data Source, the Encryption Module is always the same unique device.

The number of ways to choose $k$ triads from $t$ possibilities grows rapidly, and finding a valid non-overlapping configuration requires navigating a massive search space of potential subsets. Determine if a valid configuration exists, and if so, report one such set of $k$ triads.

## Input

The first line contains two integers $k$ and $t$ (1 ≤ $k$ ≤ 1200, 0 ≤ $t$ ≤ $k \cdot k$): the number of components in each pool and the number of viable routing triads.

Each of the next $t$ lines contains three integers $x$, $y$, and $z$ (1 ≤ $x, y, z$ ≤ $k$), representing a viable triad connecting Data Source $x$, Encryption Module $y$, and Transmission Channel $z$. No triad is listed more than once. In the given list, every appearance of a specific $x$ is always accompanied by the same $y$, and distinct values of $x$ are always accompanied by distinct values of $y$.

## Output

If a valid selection of $k$ routing triads exists, print `YES` on the first line. Then, print $k$ lines, each containing the three integers `x y z` of one chosen triad (in any order). Any valid selection is accepted.

If no valid configuration exists, print `NO`.

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
