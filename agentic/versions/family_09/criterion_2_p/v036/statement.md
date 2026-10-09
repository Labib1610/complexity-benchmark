# Microservice Test Environment

Time limit: 2 s   Memory limit: 256 MB

## Description

A software system consists of **n** microservices (numbered 1 to **n**). The system registry lists **m** known data races, each occurring between a specific pair of microservices if they run in the same environment.

Every data race involves one service acting as an initiator and one service acting as a processor. Consequently, a data race only ever occurs between an initiator and a processor; two initiators never race with each other, and two processors never race with each other. The registry does not record which role each microservice plays, but you may deduce this from the race reports.

You need to provision a single testing environment containing exactly **k** microservices. To ensure stability, the chosen group must be completely free of data races (no two services in the group can have a race). 

Given the target size **k**, determine whether a race-free group of exactly **k** microservices can be selected, and if so, identify one such group.

## Input

The first line contains three integers **n**, **m**, and **k** (1 ≤ n ≤ 100000, 0 ≤ m ≤ 400000, 1 ≤ k ≤ n).
Each of the following **m** lines contains two integers **u** and **v** (1 ≤ u, v ≤ n, u ≠ v), representing a data race between microservice **u** and microservice **v**. 
No pair is listed more than once. The input is guaranteed to follow the initiator-processor structure described above.

## Output

If a race-free group of exactly **k** microservices exists, output `YES` on the first line. On the second line, output **k** distinct integers representing the microservices in the group, separated by spaces. If multiple valid groups exist, any of them is accepted.

If no such group can be formed, output `NO`.

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
