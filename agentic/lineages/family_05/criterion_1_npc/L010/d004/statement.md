# Problem A — Deep Space Relays

Time limit: 5 s   Memory limit: 256 MB

## Description

You are designing a communication array and must select exactly $k$ relay configurations from a provided catalog.

You are given a log of $t$ candidate relays. Each candidate is specified by a triplet of integers $(x, y, z)$, where each integer is between $1$ and $k$ inclusive.

To prevent signal interference, the $k$ chosen relays must be completely mutually isolated. Two relays are considered mutually isolated if they do not share any parameter values in the same position. Specifically, for any two distinct chosen relays $(x_1, y_1, z_1)$ and $(x_2, y_2, z_2)$, it must be true that $x_1 \neq x_2$, and $y_1 \neq y_2$, and $z_1 \neq z_2$.

Determine whether it is possible to select exactly $k$ mutually isolated relays from the log. If it is, output the $k$ chosen relays.

## Input

The first line contains two integers $k$ and $t$ ($1 \le k \le 22$, $0 \le t \le k^3$), denoting the required number of relays (which is also the upper bound for any parameter) and the total number of candidate relays in the log.
The next $t$ lines each contain three integers $x$, $y$, and $z$ ($1 \le x, y, z \le k$), detailing a candidate relay. No relay appears more than once in the log.

## Output

If a valid selection of $k$ relays is possible, print `YES` on the first line. Then, print $k$ lines, each containing the three integers $x$ $y$ $z$ of a chosen relay. The chosen relays can be printed in any order. Any valid selection will be accepted.

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

In Example 2, both candidate relays have $1$ as their second integer (i.e., $y_1 = y_2 = 1$). Therefore, they are not mutually isolated. It is impossible to select 2 relays that satisfy the isolation condition.