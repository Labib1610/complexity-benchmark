# Problem A — Deep Space Relays

Time limit: 5 s   Memory limit: 256 MB

## Description

You are designing a communication array and must select exactly $k$ relay configurations from a provided catalog.

You are given a log of $t$ candidate relays. Each candidate is specified by a triplet of positive integers $(a, b, c)$.

To prevent signal interference, the chosen relays must satisfy a strict global isolation metric. For any relay with parameters $(a, b, c)$, its three *resonance signatures* are defined as $2^{a-1}$, $2^{b-1}$, and $2^{c-1}$. 

A selection of exactly $k$ relays is valid if and only if the sum of the first resonance signatures across all $k$ chosen relays equals exactly $2^k - 1$, the sum of the second resonance signatures equals exactly $2^k - 1$, and the sum of the third resonance signatures equals exactly $2^k - 1$.

Determine whether it is possible to select exactly $k$ valid relays from the log. If it is, output the $k$ chosen relays.

## Input

The first line contains two integers $k$ and $t$ ($1 \le k \le 22$, $0 \le t \le k^3$), denoting the required number of relays and the total number of candidate relays in the log. 

The next $t$ lines each contain three integers $a$, $b$, and $c$, detailing a candidate relay. Each parameter of a candidate relay is a positive integer that does not exceed $k$ ($1 \le a, b, c \le k$). No relay appears more than once in the log.

## Output

If a valid selection of exactly $k$ relays is possible, print `YES` on the first line. Then, print $k$ lines, each containing the three integers $a$ $b$ $c$ of a chosen relay. The chosen relays can be printed in any order. Any valid selection will be accepted.

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

In Example 2, the two candidate relays are $(1, 1, 1)$ and $(2, 1, 2)$. If we select both of them ($k=2$), the sums of their resonance signatures are:
- First parameters: $2^{1-1} + 2^{2-1} = 1 + 2 = 3$.
- Second parameters: $2^{1-1} + 2^{1-1} = 1 + 1 = 2$.
- Third parameters: $2^{1-1} + 2^{2-1} = 1 + 2 = 3$.

The target sum is $2^k - 1 = 3$. Because the sum of the second resonance signatures is $2$ rather than $3$, this selection is invalid. It is impossible to select 2 relays that satisfy the requirement.