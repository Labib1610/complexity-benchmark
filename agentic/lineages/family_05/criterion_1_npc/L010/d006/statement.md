# Problem A — Deep Space Relays

Time limit: 5 s   Memory limit: 256 MB

## Description

You are designing a communication array and must select exactly $k$ relay configurations from a provided catalog.

You are given a log of $t$ candidate relays. Each candidate is specified by a triplet of positive integers $(a, b, c)$.

To prevent signal interference, the $k$ chosen relays must satisfy a strict global isolation metric. Let $S_1$ be the set of the first parameters of the chosen relays, $S_2$ be the set of their second parameters, and $S_3$ be the set of their third parameters. The selection is valid if and only if the product of the cardinalities (number of unique elements) of these three sets is exactly $k^3$:

$$ |S_1| \times |S_2| \times |S_3| = k^3 $$

Determine whether it is possible to select exactly $k$ valid relays from the log. If it is, output the $k$ chosen relays.

## Input

The first line contains two integers $k$ and $t$ ($1 \le k \le 22$, $0 \le t \le k^3$), denoting the required number of relays and the total number of candidate relays in the log. 

The next $t$ lines each contain three integers $a$, $b$, and $c$, detailing a candidate relay. Each parameter of a candidate relay is a positive integer that does not exceed $k$. No relay appears more than once in the log.

## Output

If a valid selection of $k$ relays is possible, print `YES` on the first line. Then, print $k$ lines, each containing the three integers $a$ $b$ $c$ of a chosen relay. The chosen relays can be printed in any order. Any valid selection will be accepted.

If no such selection is possible, print `NO`.

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

In Example 2, the two candidate relays are $(1, 1, 1)$ and $(2, 1, 2)$. If we select both of them ($k=2$), the sets of unique parameters are:
- $S_1 = \{1, 2\}$, so $|S_1| = 2$.
- $S_2 = \{1\}$, so $|S_2| = 1$.
- $S_3 = \{1, 2\}$, so $|S_3| = 2$.

The product of their cardinalities is $2 \times 1 \times 2 = 4$. Since $4$ is not equal to $2^3 = 8$, they do not satisfy the isolation condition. It is impossible to select 2 relays that satisfy the requirement.