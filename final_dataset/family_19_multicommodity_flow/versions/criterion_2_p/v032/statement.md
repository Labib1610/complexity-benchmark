# Cargo Assignment over a Supply Network

Time limit: 2 s   Memory limit: 256 MB

## Description
A logistics network consists of a set of facilities connected by one-way transit links. You are tasked with determining an exact integer load for every link in the network. For each link, you must choose an integer value between 0 and its maximum limit, inclusive. Because every link can independently take any integer value in this range, the number of possible network configurations grows as the product of the limits, leading to an exponentially large search space. Your goal is to systematically explore these combinations to find a single valid configuration of loads that satisfies a system of strict local rules.

The rules for a valid configuration are as follows:
- There are $k$ different types of cargo to manage. However, for this specific operational window, $k$ is always strictly equal to 1.
- At the origin facility, the sum of loads on all outgoing links minus the sum of loads on all incoming links must equal exactly $d$.
- At the destination facility, the sum of loads on all incoming links minus the sum of loads on all outgoing links must equal exactly $d$.
- At every other facility in the network, the sum of incoming loads must exactly equal the sum of outgoing loads.

You must either provide a valid integer assignment for all links that fulfills these requirements, or determine that no such configuration exists in the entire search space.

## Input
The first line contains three integers $n$, $m$, and $k$, representing the number of facilities, the number of transit links, and the number of cargo types (where $k = 1$).
The second line contains three integers $s$, $t$, and $d$, representing the origin facility, the destination facility, and the required total quantity to transfer.
The following $m$ lines each contain three integers $u$, $v$, and $L$, indicating a one-way transit link from facility $u$ to facility $v$ with a maximum load limit of $L$.

## Output
If a valid configuration exists, print `YES` on the first line, followed by a second line containing $m$ integers representing the assigned load for each link in the order they were given in the input. If no configuration satisfies all rules, print `NO`.

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
