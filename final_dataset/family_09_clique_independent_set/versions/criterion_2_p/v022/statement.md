# Subsystem Activation Protocol

Time limit: 2 s   Memory limit: 256 MB

## Description

You are configuring a distributed network of **n** relays, numbered 1 to **n**. Your objective is to bring exactly **k** relays online, while keeping the others offline.

The network is subject to **m** hardware conflicts. Each conflict is a pair of relays that draw from the same power bus; if both relays in a conflict pair are brought online simultaneously, the system will overload. Therefore, your chosen set of **k** relays must not contain any conflicting pairs.

Because you must select exactly **k** relays from a pool of **n**, the total number of possible configurations is vast. Blindly evaluating all combinations is impossible within the time limit. You must determine if there is any valid selection of exactly **k** relays.

The network architecture strictly separates the relays into two distinct power grids. Conflicts only ever occur between a relay on the first grid and a relay on the second grid. Two relays on the same grid will never conflict. The specific grid assignment of each relay is internal and not provided in the input, but the conflict list is guaranteed to adhere to this strict separation.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 100000, 0 ≤ m ≤ 400000, 1 ≤ k ≤ n).
Each of the next **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v), representing a conflict between relay **u** and relay **v**. No conflict is listed twice, and all conflicts are guaranteed to follow the two-grid separation described above.

## Output

If a safe activation of exactly **k** relays exists, print `YES` on the first line, then on the second line print **k** distinct relay numbers to bring online, separated by spaces. Any valid set of **k** non-conflicting relays is accepted.

If no such set exists, print `NO`.

## Examples

### Example 1

**Input**
```
4 4 2
1 3
1 4
2 3
2 4
```

**Output**
```
YES
1 2
```

### Example 2

**Input**
```
5 0 5
```

**Output**
```
YES
1 2 3 4 5
```

### Example 3

**Input**
```
4 4 3
1 3
1 4
2 3
2 4
```

**Output**
```
NO
```
