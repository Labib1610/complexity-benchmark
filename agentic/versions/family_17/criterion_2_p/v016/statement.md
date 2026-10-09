# Complete Asset Synchronization

Time limit: 2 s   Memory limit: 256 MB

## Description
The operations division needs to synchronize a fleet of remote assets. The fleet consists of $q$ controllers, assigned sequential ID numbers from $1$ to $q$, and $q$ platforms, assigned sequential ID numbers from $q+1$ to $2q$.

A complete synchrony plan must pair each controller with exactly one platform, such that all $2q$ assets are actively paired simultaneously. No asset can be left unassigned, and no asset can participate in more than one pair.

You are provided with a list of $t$ hardware-certified pairs. A controller and a platform can only be synchronized if their specific pairing appears on this list. The order and redundancy of this list do not matter, only which exact pairings are certified.

To comply with the division's signal interference protocols, the certified list is guaranteed to satisfy two strict conditions:
- **Signal Delta Constraint:** For any certified pair, the difference between the platform's ID and the controller's ID is at least $1$ and at most $2q - 1$.
- **Bandwidth Ceiling:** The sum of the two ID numbers in any certified pair will never exceed $3q$.

Determine if there is a valid synchrony plan that uses only certified pairs and includes every single asset exactly once. If such a plan exists, output the pairings. Otherwise, report that it is not possible.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), representing the number of controllers (and platforms) and the number of certified pairs, respectively.
Each of the following $t$ lines contains two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), representing a certified pair consisting of controller $a$ and platform $b$.

## Output
If a complete synchrony plan is possible, print `YES` on the first line, followed by $q$ lines. Each of these $q$ lines must contain the two integers $a$ and $b$ of a chosen pair.
If no such plan is possible, print `NO`.

## Example

### Input
```
3 4
1 4
2 5
3 6
1 5
```

### Output
```
YES
1 4
2 5
3 6
```
