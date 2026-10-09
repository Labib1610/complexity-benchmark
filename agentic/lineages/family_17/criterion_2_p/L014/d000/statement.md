# Problem B — Comprehensive Controller/Platform Pairing

Time limit: 2 s   Memory limit: 256 MB

## Description
The directorate manages a fleet of specialized assets divided into two categories of equal size. The first category comprises controllers, which are assigned consecutive identification numbers starting from 1. The second category consists of platforms, which receive identification numbers in the block immediately following the controllers.

Operational protocols dictate that a controller and a platform can only interface if their specific pairing has passed rigorous testing. The resulting certification log contains all permitted controller-platform combinations. During an operation, a selected set of these certified combinations is activated. To prevent command conflicts, a valid configuration must ensure that no individual controller and no individual platform is part of more than one activated combination.

The planners are now preparing for a major drill. For this exercise, the remote segment must be fully committed. Your task is to determine whether there exists a valid configuration of certified combinations that successfully engages every single controller and every single platform simultaneously. If such a complete commitment is possible, you must generate the roster of activated combinations; otherwise, you must report that the requirements cannot be met.

## Input
The first line contains two integers $q$ and $t$ ($1 \le q \le 100000$, $0 \le t \le 400000$), where $q$ is the number of controllers, and $t$ is the number of certified combinations.
The next $t$ lines each contain two integers $a$ and $b$ ($1 \le a \le q < b \le 2q$), representing a certified combination between controller $a$ and platform $b$.

## Output
If a complete commitment is possible, print `YES` on the first line, followed by $q$ lines each containing the two identification numbers of one activated combination. Any valid configuration will be accepted. If it is impossible, print `NO`.

## Example

### Input
```text
3 4
1 4
1 6
2 5
3 4
```

### Output
```text
YES
1 6
2 5
3 4
```
