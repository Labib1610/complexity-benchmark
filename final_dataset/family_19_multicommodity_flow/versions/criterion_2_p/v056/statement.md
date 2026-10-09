# Energy Grid Distribution Configuration

Time limit: 2 s   Memory limit: 256 MB

## Description
An energy distribution grid consists of a set of substations connected by directional transmission cables. You are tasked with determining an exact integer power flow for every cable in the grid. For each cable, you must choose an integer value between 0 and its maximum capacity, inclusive. Because every cable can independently take any integer value in this range, the number of possible grid configurations grows as the product of the capacities, creating a massive search space. Your goal is to systematically explore these combinations to find a single valid configuration of power flows that satisfies a system of strict local rules.

The rules for a valid configuration are as follows:
- There are $k$ different types of energy to manage. However, for this specific operational window, $k$ is always strictly equal to 1.
- At the generator substation, the sum of flows on all outgoing cables minus the sum of flows on all incoming cables must equal exactly $d$.
- At the consumer substation, the sum of flows on all incoming cables minus the sum of flows on all outgoing cables must equal exactly $d$.
- At every other substation in the grid, the sum of incoming flows must exactly equal the sum of outgoing flows.

To ensure the grid operates within stable theoretical limits, all test cases are guaranteed to satisfy the following structural constraints:
- **Phase Divisibility:** The total power demand $d$ is perfectly divisible by the number of energy types $k$.
- **Capacity Domination:** For any given transmission cable, its individual maximum capacity $L$ is bounded from above by the total sum of the maximum capacities of all $m$ cables in the network.

You must either provide a valid integer assignment for all cables that fulfills these requirements, or determine that no such configuration exists in the entire search space.

## Input
The first line contains three integers $n$, $m$, and $k$, representing the number of substations, the number of transmission cables, and the number of energy types (where $k = 1$).
The second line contains three integers $s$, $t$, and $d$, representing the generator substation, the consumer substation, and the required total power to transfer.
The following $m$ lines each contain three integers $u$, $v$, and $L$, indicating a directional transmission cable from substation $u$ to substation $v$ with a maximum capacity of $L$.

## Output
If a valid configuration exists, print `YES` on the first line, followed by a second line containing $m$ integers representing the assigned flow for each cable in the order they were given in the input. If no configuration satisfies all rules, print `NO`.

## Example 1

### Input
```text
4 5 1
1 4 8
1 2 5
1 3 5
2 3 2
2 4 4
3 4 5
```

### Output
```text
YES
4 4 0 4 4
```
