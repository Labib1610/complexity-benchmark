# Problem B — Full-Scale Operator/Chassis Deployment

Time limit: 2 s   Memory limit: 256 MB

## Description
The agency oversees a fleet of technical assets divided into two equal-sized groups. The first group consists of command operators, assigned sequential IDs starting from 1. The second group consists of drone chassis, assigned sequential IDs in the block immediately following the operators.

Operational protocols dictate that an operator and a drone chassis can only be paired if their specific combination has passed safety testing. The log contains all permitted operator-chassis combinations. During an operation, a selected set of these combinations is activated. To prevent interference, a valid deployment must ensure that no individual operator and no individual chassis is part of more than one activated combination.

The planners are preparing for a full-scale exercise. For this exercise, every single operator and every single chassis must be engaged simultaneously. Your task is to determine whether there exists a valid deployment of tested combinations that achieves this complete engagement. If possible, generate the roster of activated combinations; otherwise, report that the requirements cannot be met.

## Input
The first line contains two integers $q$ and $t$. The integer $q$ is the total headcount of operators; the facility requires at least a single operator and has a maximum capacity of 100,000. The integer $t$ is the number of tested combinations; the testing database can be completely empty or contain up to a maximum limit of 400,000 entries.

The next $t$ lines each detail one tested combination using two integers $a$ and $b$. The first integer $a$ is an operator ID (ranging from 1 up to the total headcount of operators). The second integer $b$ is a chassis ID (ranging from the ID immediately following the highest operator ID, up to exactly double the operator headcount).

## Output
If a full-scale deployment is possible, print `YES` on the first line, followed by $q$ lines each containing the two IDs of an activated combination. Any valid deployment will be accepted. If it is impossible, print `NO`.

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
