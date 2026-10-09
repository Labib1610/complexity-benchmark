# Problem A — Greenhouse Allocation

Time limit: 2 s   Memory limit: 256 MB

You are managing an experimental botanical research facility. You need to assign $n$ distinct plant species to exactly one of $3$ available climate-controlled greenhouses (labeled 1, 2, and 3).

Certain pairs of plant species are known to release biochemicals that are mutually toxic; these pairs cannot be assigned to the same greenhouse. You are given a list of $m$ such mutually toxic pairs.

To ensure the viability of the facility, your assignment must satisfy all of the following operational constraints:
1. **Toxicity Isolation**: No two plant species from a mutually toxic pair may be assigned to the same greenhouse.
2. **Water Supply**: Each plant species requires exactly 10 liters of water per day. Each greenhouse can supply a maximum of 450 liters of water per day. The total daily water consumption of the species assigned to any single greenhouse must not exceed this limit.
3. **Filtration Budget**: Every mutually toxic pair assigned to different greenhouses consumes exactly 1 unit of the facility's centralized filtration budget. The total filtration units consumed by all such pairs must not exceed the maximum budget of 800 units.
4. **Conservation of Species**: Every species must be assigned to exactly one greenhouse, meaning the sum of the number of assigned species across all three greenhouses must equal $n$.

Determine if there exists a greenhouse assignment for all $n$ species that satisfies all the operational constraints.

## Input
The first line contains two integers $n$ and $m$ — the number of plant species and the number of mutually toxic pairs ($1 \le n \le 40$, $0 \le m \le n(n-1)/2$).
Each of the next $m$ lines contains two integers $u$ and $v$ — a mutually toxic pair.

## Output
If no valid assignment exists that satisfies all constraints, print a single line containing `NO`.
Otherwise, print `YES` on the first line. On the second line, print $n$ integers $g_1, g_2, \dots, g_n$ (each in $\{1, 2, 3\}$), where $g_i$ is the greenhouse assigned to species $i$. Any valid assignment is accepted.

## Example 1
Input:
```
4 5
1 2
1 3
2 3
1 4
2 4
```
Output:
```
YES
1 2 3 3
```

## Example 2
Input:
```
4 6
1 2
1 3
1 4
2 3
2 4
3 4
```
Output:
```
NO
```
