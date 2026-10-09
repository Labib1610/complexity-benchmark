# Problem A — Signature Dining

Time limit: 5 s
Memory limit: 256 MB

## Description

A culinary team is finalizing a set of signature dining experiences. The experience is divided into three distinct phases. For each phase, the kitchen has developed exactly $k$ recipes, indexed from $1$ to $k$. In total, there are $3k$ distinct recipes ($k$ for Phase 1, $k$ for Phase 2, and $k$ for Phase 3).

Not all recipes flow well together. The chefs have compiled a catalog of approved flavor progressions. Each progression is defined by a trio of indices $(x, y, z)$, indicating that recipe $x$ from Phase 1, recipe $y$ from Phase 2, and recipe $z$ from Phase 3 can be served sequentially. 

To ensure no recipe goes to waste and production remains balanced, the kitchen operates under a strict inventory rule: they prepare exactly one batch of each of the $3k$ distinct recipes. When a progression $(x, y, z)$ is selected for the menu, it fully consumes the prepared batches of recipe $x$ from Phase 1, recipe $y$ from Phase 2, and recipe $z$ from Phase 3. 

You must choose exactly $k$ progressions from the approved catalog such that the kitchen's entire inventory is completely depleted. In other words, across your chosen progressions, every recipe from every phase must be consumed exactly once. 

Determine whether this is possible, and if so, report one valid selection of progressions.

## Input

The first line contains two integers $k$ and $t$ ($1 \le k \le 22$, $0 \le t \le k \cdot k \cdot k$): the number of recipes per phase and the number of approved progressions in the catalog.
Each of the next $t$ lines contains three integers $x$, $y$, $z$ ($1 \le x, y, z \le k$), representing an approved progression. No progression is listed more than once.

## Output

If a valid selection of $k$ progressions exists, print `YES` on the first line. Then, print $k$ lines, each containing the three integers $x$ $y$ $z$ of one chosen progression. Any valid selection that depletes the inventory is accepted; the progressions may be printed in any order.

If no valid selection exists, print `NO`.

## Examples

### Example 1

**Input**
```
2 3
1 1 1
1 2 2
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
2 1 2
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

## Note

In Example 2, both approved progressions require recipe 1 from Phase 2. Because only one batch of this recipe is prepared, selecting both progressions is impossible, leaving recipe 2 from Phase 2 forever unconsumed.
